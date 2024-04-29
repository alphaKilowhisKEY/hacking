import tools as t

is_on = True

while is_on:
    t.print_available_commands()
    names = t.list_all_names()
    user_input = input("[+] ")
    if user_input == "exit":
        is_on = False
    elif user_input == "list":
        t.list_all_names()
    elif user_input == "change":
        interface = input("device name: ")
        if(interface in names):
            new_mac = input("new address: ")
            if(t.check_mac_address_format(new_mac)):
                t.change_device_name(interface, new_mac) 
            else:
                print("Not valid MAC address. Try again.")    
    else:
        print("")            