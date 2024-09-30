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
pip install .
```
- **Alternatively, you can manually install the required dependencies**:

```
pip install rich
```
## Usage
- **To run the tool, use the following command**:

```
ddos --target <TARGET_IP> --port <TARGET_PORT> --threads <THREAD_COUNT> --attack <TCP/UDP>
```
## Example
```
ddos --target 192.168.1.1 --port 80 --threads 1000 --attack TCP
```
## Arguments
- **-t, --target: Target IP address (required)**.
- **-p, --port: Target port (required)**.
- **-n, --threads: Number of threads (default: 1000)**.
- **-a, --attack: Type of attack (TCP/UDP, required)**.
## Requirements
- **Python 3.6 or higher**
- **rich library**
- **License**
- **This project is licensed under the MIT License. See the LICENSE file for more details**.

## Contact
- **Developed by: Ibrahem abo kila**
- **Email: ibrahemabokila.com**