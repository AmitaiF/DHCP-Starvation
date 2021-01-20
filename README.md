# DHCP Starvation
A tool for performing a DHCP Starvation.

## Installation

1. Install scapy:
```
pip install scapy
```
2. Download the project. You can download a zip file, or you can clone it:
```
git clone https://github.com/AmitaiF/DHCP-Starvation.git
```

## Usage
1. Navigate to the folder containing the DHCPStarvationNEW.py file.
2. To see help message, run:
```
DHCPStarvationNEW.py -h
```

## What is DHCP Starvation?
DHCP Starvation is an attack that targets DHCP servers. During the attack, the attacker floods a DHCP server with DHCP requests until the server exhausts its supply of IP addresses. Since the DHCP server doesn't have IP addresses to give, new users can't connect to the network. 

## How it works?
1. The program creates 50 fake MAC addresses.
2. For each MAC address we perform a full DHCP Handshake (Discover, Offer, Request and Acknowledgment). By doing so we get 50 IP addresses. In an average LAN network, 50 IP addresses will consume all the available IP addresses.
3. If we ran the program with the -persistent flag, we renew for each MAC address his IP address.