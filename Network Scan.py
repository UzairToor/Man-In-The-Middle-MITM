import socket
import ipaddress
from scapy.all import ARP, Ether, srp

def get_my_ip():
    hostname = socket.gethostname()
    device_ip= socket.gethostbyname(hostname)
    return device_ip
def get_my_network(ip_address):
    subnet_mask = '255.255.255.0'  # Replace with your actual Subnet
    network = ipaddress.ip_network(f"{ip_address}/{subnet_mask}", strict=False)
    network_address = network.network_address
    network_variable = str(network_address)
    print(f"You are on the Network: {network_address}")
    return network_variable
def get_mac_address(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = broadcast / arp_request
    result = srp(packet, timeout=2, verbose=False)[0]

    if result:
        return result[0][1].hwsrc
    else:
        return None

Host_Count = 0
ip = get_my_ip()
network = get_my_network(ip)
with open("Sniffed_Mac_Addresses.txt", "a") as file:
    file.write(f"\n|| Hosts for Network: {network} ||\n\n")
    for i in range(1,256):
        ip_address = '.'.join(ip.split('.')[:3]) + '.' + f'{i}'
        mac_address = get_mac_address(ip_address)
        if mac_address:
            Sniffed_Address = f"The MAC address of {ip_address} is {mac_address}"
            print(Sniffed_Address)
            Host_Count+=1
            file.write(f"{Sniffed_Address}\n")

        else:
            print(f"The MAC address of {ip_address} is not found")

print("All Packets Sent")

print(f"Total {Host_Count} hosts are up")
