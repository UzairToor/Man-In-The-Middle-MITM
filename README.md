Following is a step by step procedure on running this project effectively:

1. Make sure that you and your victim are on the same network
2. Before Launching MITM.py, it is recommended to first run 'Network Scan.py' to get the IP and MAC addresses of all the hosts on the network.
3. Wait for 4-5 minutes for 'Network Scan.py' to fully execute. After execution, the results will be available in a text file named 'Sniffed_Mac_Addresses.txt'
4. Find your Router's and your target's Ip and MAC addresses
5. In the 'MITM.py' file, in the first arp reply, replace the first IP address with your router's Ip and the MAC address with your router's MAC address.
6. Now In the first arp reply, replace the second IP address with your Victim's IP and the MAC address with your MAC address.
7. First Arp reply should look like this: <br>
   send_arp_reply('192.168.1.1', '38:de:a5:bb:f9:a2', '192.168.1.10', '42:de:c2:08:d9:c9') # First ARP reply <br>
9. In the second arp reply, replace the first IP address with your victims's IP and the MAC address with your victim's MAC address.
10. Now In the second arp reply, replace the second IP address with your router's IP and the MAC address with your MAC address.
11. First Arp reply should look like this: <br>
    send_arp_reply('192.168.1.10', '66:d2:a5:bb:f7:06', '192.168.1.1', '42:de:c2:08:d9:c9') # Second ARP reply <br>
13. Run 'MITM.py' file
14. Open Wireshark or any other packet sniffer and observe the traffic from your victim coming to your computer. 

*Note:* This project is for educational purposes only and should not be used to harm or steal information from anyone without their consent.
