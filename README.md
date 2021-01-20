# DHCP Starvation
A tool for performing a DHCP Starvation.

## Installation

1. Install scapy:
```
pip install scapy
```
2. Download the project. You can download a zip file, or you can clone it:
```
git clone https://github.com/AmitaiF/DHCP-Starvation
```

## Usage
1. Navigate to the folder containing the DHCPStarvationNEW.py file.
2. To see help message, run:
```
DHCPStarvationNEW.py -h
```
## How it works?
1. The program creates 50 fake MAC addresses.
2. For each MAC address we perform a full DHCP Handshake (Discover, Offer, Request and Acknowledgment). By doing so we get 50 IP addresses. In an average LAN network, 50 IP addresses will consume all the available IP addresses.
3. If we ran the program with the -persistent flag, we renew for each MAC address his IP address.