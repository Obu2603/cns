def detect_arp_spoofing(ip_mac_table, ip, mac):
    if ip in ip_mac_table:
        if ip_mac_table[ip] != mac:
            return True  
    else:
        ip_mac_table[ip] = mac 
    return False

ip_mac_table = {}

print("=== ARP Packet Simulation ===")
ip = input("Enter sender IP address: ")
mac = input("Enter sender MAC address: ")

if detect_arp_spoofing(ip_mac_table, ip, mac):
    print("ALERT: Potential ARP spoofing detected!")
else:
    print(" No spoofing detected. ARP packet appears normal.")
