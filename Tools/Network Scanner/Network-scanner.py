from scapy.all import *
from scapy.layers.l2 import Ether, ARP

target_ip = "192.168.1.1/24"

print("Started scanning..")

# create ARP packet
arp = ARP(pdst=target_ip)

# create the Ether broadcast packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients
clients = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18 + "MAC")
for client in clients:
    print("{:16}{}".format(client['ip'], client['mac']))
