Following is a step by step procedure on running this project effectively:

1. Make sure that you and your victim are on the same network
2. Before Launching MITM.py, it is recommended to first run 'Network Scan.py' to get the IP and MAC addresses of all the hosts on the network.
3. Wait for 4-5 minutes for 'Network Scan.py' to fully execute. After execution, the results will be available in a text file named 'Sniffed_Mac_Addresses.txt'
4. Find your Router's and your target's Ip and MAC addresses
5. In the 'MITM.py' file, in the first arp reply, replace the first IP address with your router's Ip and the MAC address with your router's MAC address.
6. Now In the first arp reply, replace the second IP address with your Victim's IP and the MAC address with your MAC address.
7. First Arp reply should look like this:
8. In the second arp reply, replace the first IP address with your victims's IP and the MAC address with your victim's MAC address.
9. Now In the second arp reply, replace the second IP address with your router's IP and the MAC address with your MAC address.
10. First Arp reply should look like this:
11. Run 'MITM.py' file
12. Open Wireshark or any other packet sniffer and observe the traffic from your victim coming to your computer. 
