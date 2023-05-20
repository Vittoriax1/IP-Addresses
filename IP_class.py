import ipaddress

while True:
    # User input
    ip_address = input("Enter an IPv4 address (or 'exit' to quit): ")

    # Check if the user wants to exit
    if ip_address.lower() == 'exit':
        break

    try:
        # Parse the input IP address
        ip = ipaddress.IPv4Address(ip_address)

        # Determine the class of the IP address
        if ip.is_private:
            ip_class = "Private"
        else:
            first_octet = ip.packed[0]
            if first_octet < 128:
                ip_class = "Class A"
            elif first_octet < 192:
                ip_class = "Class B"
            elif first_octet < 224:
                ip_class = "Class C"
            elif first_octet < 240:
                ip_class = "Class D (Multicast)"
            else:
                ip_class = "Class E (Experimental)"

        # Calculate the network address and subnet mask
        network_address = ipaddress.IPv4Network(ip_address + '/24', strict=False)
        subnet_mask = network_address.netmask

        # Calculate the broadcast address
        broadcast_address = network_address.broadcast_address

        # Calculate the number of hosts
        num_hosts = network_address.num_addresses - 2

        # Print the results
        print("IP Address:", ip_address)
        print("Class:", ip_class)
        print("Network Address:", network_address.network_address)
        print("Subnet Mask:", subnet_mask)
        print("Broadcast Address:", broadcast_address)
        print("Number of Hosts:", num_hosts)
        print("----------------------")
    except ipaddress.AddressValueError:
        print("Invalid IP address. Please try again.")
