# DDoS Attack Tool

A simple command-line tool for simulating DDoS attacks using TCP and UDP protocols. This tool is designed for educational purposes only. Please use it responsibly and within the legal boundaries.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Example](#example)
- [Arguments](#arguments)
- [Contact](#contact)

## Features

- Simulate DDoS attacks using TCP or UDP protocols.
- Customize the number of threads for the attack.
- Option to use proxies for the attack.
- Randomly generated IP addresses and MAC addresses for each request.
- Console output using Rich for better visibility.

## Installation

- **To install the tool, clone this repository and run the following command**:

```
git clone https://github.com/hemaabokila/ddos_attack.git
cd ddos_attack
sudo pip install .
```
- **Alternatively, you can manually install the required dependencies**:

```
pip install rich
```
## Usage
- **To run the tool, use the following command**:

```
ddos target <TARGET_IP> --port <TARGET_PORT> --threads <THREAD_COUNT> --attack <TCP/UDP> --proxies proxies.txt
```
## Example
```
ddos 192.168.1.100 -p 80 -a TCP -P proxies.txt
```
## Arguments
- **target: Target IP address (required)**.
- **-p, --port: Target port (required)**.
- **-t, --threads: Number of threads (default: 1000)**.
- **-a, --attack: Type of attack (TCP/UDP, required)**.
- **-P, --proxy-file: proxy file (proxies.txt)**.
## Requirements
- **Python 3.6 or higher**
- **rich library**

## Contact
- **Developed by: Ibrahem abo kila**
- **Email: ibrahemabokila.com**
