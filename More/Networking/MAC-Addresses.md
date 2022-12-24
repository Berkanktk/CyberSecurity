# MAC Addresses
Each host in a network has its own 48-bit (6 octets) Media Access Control (MAC) address, represented in hexadecimal format. MAC is the physical address for our network interfaces. There are several different standards for the MAC address:

* Ethernet (IEEE 802.3)
* Bluetooth (IEEE 802.15)
* WLAN (IEEE 802.11)

This is because the MAC address addresses the physical connection (network card, Bluetooth, or WLAN adapter) of a host. Each network card has its individual MAC address, which is configured once on the manufacturer's hardware side but can always be changed, at least temporarily.

Let's have a look at an example of such a MAC address:

MAC address:

* DE:AD:BE:EF:13:37 
* DE-AD-BE-EF-13-37 
* DEAD.BEEF.1337

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
|----------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Binary         | 1101 1110 | 1010 1101 | 1011 1110 | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex            | DE        | AD        | BE        | EF        | 13        | 37        |

When an IP packet is delivered, it must be addressed on layer 2 to the destination host's physical address or to 
the router / NAT, which is responsible for routing. Each packet has a `sender address` and a `destination address`.

The first half (3 bytes / 24 bit) is the so-called Organization Unique Identifier (OUI) defined by the Institute of 
Electrical and Electronics Engineers (IEEE) for the respective manufacturers. (Ex. DE AD BE)

The last half of the MAC address is called the Individual Address Part or Network Interface Controller (NIC), which 
the manufacturers assign. The manufacturer sets this bit sequence only once and thus ensures that the complete 
address is unique. (Ex. EF 13 37).

If a host with the IP target address is located in the same subnet, the delivery is made directly to the target 
computer's physical address. However, if this host belongs to a different subnet, the Ethernet frame is addressed to 
the MAC address of the responsible router (default gateway). If the Ethernet frame's destination address matches the 
own layer 2 address, the router will forward the frame to the higher layers. Address Resolution Protocol (ARP) is 
used  in IPv4 to determine the MAC addresses associated with the IP addresses.

As with IPv4 addresses, there are also certain reserved areas for the MAC address. These include, for example, the  
local range for the MAC.

| Local Range       |
|-------------------|
| 02:00:00:00:00:00 |
| 06:00:00:00:00:00 |
| 0A:00:00:00:00:00 |
| 0E:00:00:00:00:00 |


Furthermore, the last two bits in the first octet can play another essential role. The last bit can have two states, 
0 and 1, as we already know. The last bit identifies the MAC address as Unicast (0) or Multicast (1). With unicast, 
it  means that the packet sent will reach only one specific host.

## MAC Unicast
| Representation | 1st Octet     | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
|----------------|---------------|-----------|-----------|-----------|-----------|-----------|
| Binary         | 1101 111**0** | 1010 1101 | 1011 1110 | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex            | D**E**        | AD        | BE        | EF        | 13        | 37        |

With multicast, the packet is sent only once to all hosts on the local network, which then decides whether or not to 
accept  the packet based on their configuration. The multicast address is a unique address, just like the broadcast  
address, which has fixed octet values. Broadcast in a network represents a broadcasted call, where data packets are  
transmitted simultaneously from one point to all members of a network. It is mainly used if the address of the  
receiver of the packet is not yet known. An example is the ARP (for MAC addresses) and DHCP (for IPv4 addresses) 
protocols.

The defined values of each octet are marked with a bold text.

## MAC Multicast
| Representation | 1st Octet     | 2nd Octet     | 3rd Octet     | 4th Octet | 5th Octet | 6th Octet |
|----------------|---------------|---------------|---------------|-----------|-----------|-----------|
| Binary         | **0000 0001** | **0000 0000** | **0101 1110** | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex            | **01**        | **00**        | **5E**        | EF        | 13        | 37        |

## MAC Broadcast
| Representation | 1st Octet     | 2nd Octet     | 3rd Octet     | 4th Octet     | 5th Octet     | 6th Octet     |
|----------------|---------------|---------------|---------------|---------------|---------------|---------------|
| Binary         | **1111 1111** | **1111 1111** | **1111 1111** | **1111 1111** | **1111 1111** | **1111 1111** |
| Hex            | **FF**        | **FF**        | **FF**        | **FF**        | **FF**        | **FF**        |

The second last bit in the first octet identifies whether it is a global OUI, defined by the IEEE, or a locally  
administrated MAC address.

## Global OUI
An organizationally unique identifier (OUI) is a 24-bit number that uniquely identifies a vendor, manufacturer, or other organization.

| Representation | 1st Octet     | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
|----------------|---------------|-----------|-----------|-----------|-----------|-----------|
| Binary         | 1101 11**0**0 | 1010 1101 | 1011 1110 | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex            | D**C**        | AD        | BE        | EF        | 13        | 37        |

## Locally Administrated
| Representation | 1st Octet     | 2nd Octet | 3rd Octet | 4th Octet | 5th Octet | 6th Octet |
|----------------|---------------|-----------|-----------|-----------|-----------|-----------|
| Binary         | 1101 11**1**0 | 1010 1101 | 1011 1110 | 1110 1111 | 0001 0011 | 0011 0111 |
| Hex            | D**E**        | AD        | BE        | EF        | 13        | 37        |

# Find Your Mac address
Run the following commands and look for "ether" on Linux and "Physical Address" on Windows
``` bash
# Linux
$ > ifconfig

# Winodows
$ > ipconfig/all
```