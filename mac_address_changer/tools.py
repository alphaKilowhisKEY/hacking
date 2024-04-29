import re
import subprocess

def print_available_commands():
    print("")
    print("Next commands are available:")
    print("[+] list: to list all names of available devices.")
    print("[+] change: to change the name of available device.")
    print("[+] exit: leave the program.")
    print("")

def list_all_names():
    ifconfig_output = subprocess.check_output("ifconfig", shell=True, universal_newlines=True)
    device_names = re.findall(r'^(\w+):', ifconfig_output, re.MULTILINE)
    print("")
    print("Device names:", device_names)
    return device_names

def change_device_name(interface, new_mac):
    subprocess.call(f"ifconfig {interface} down", shell=True)
    subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.call(f"ifconfig {interface} up", shell=True)
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

def check_mac_address_format(mac_address):
    # if the format is "XX:XX:XX:XX:XX:XX"
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    if re.match(pattern, mac_address):
        return True
    else:
        return False    