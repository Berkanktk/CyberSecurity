# Network Types

## Common Terminology
| Network Type | Definition |
|---|---|
| Wide Area Network (WAN) | Internet |
| Local Area Network (LAN) | Internal Networks (Ex: Home or Office) |
| Wireless Local Area Network (WLAN) | Internal Networks accessible over Wi-Fi |
| Virtual Private Network (VPN) | Connects multiple network sites to one LAN |

### WAN
The WAN (Wide Area Network) is commonly referred to as The Internet. When dealing with networking equipment, we'll often have a WAN Address and LAN Address. The WAN one is the address that is generally accessed by the Internet. That being said, it is not inclusive to the Internet; a WAN is just a large number of LANs joined together. Many large companies or government agencies will have an "Internal WAN" (also called Intranet, Airgap Network, etc.). 

Generally speaking, the primary way we identify if the network is a WAN is to use a WAN Specific routing protocol such as BGP and if the IP Schema in use is not within RFC 1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).

### LAN / WLAN
LANs (Local Area Network) and WLANs (Wireless Local Area Network) will typically assign IP Addresses designated for local use:
* RFC 1918
* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16 

In some cases, like some colleges or hotels, you may be assigned a routable (internet) IP Address from joining their LAN, but that is much less common. There's nothing different between a LAN or WLAN, other than WLAN's introduce the ability to transmit data without cables. It is mainly a security designation.

### VPN
There are three main types Virtual Private Networks (VPN), but all three have the same goal of making the user feel as if they were plugged into a different network.

#### Site-To-Site VPN
Both the client and server are Network Devices, typically either Routers or Firewalls, and share entire network ranges. This is most commonly used to join company networks together over the Internet, allowing multiple locations to communicate over the Internet as if they were local.

#### Remote Access VPN
This involves the client's computer creating a virtual interface that behaves as if it is on a client's network. Hack The Box utilizes OpenVPN, which makes a TUN Adapter letting us access the labs. When analyzing these VPNs, an important piece to consider is the routing table that is created when joining the VPN. If the VPN only creates routes for specific networks (ex: 10.10.10.0/24), this is called a Split-Tunnel VPN, meaning the Internet connection is not going out of the VPN. This is great for Hack The Box because it provides access to the Lab without the privacy concern of monitoring your internet connection. However, for a company, split-tunnel VPN's are typically not ideal because if the machine is infected with malware, network-based detection methods will most likely not work as that traffic goes out the Internet.

#### SSL VPN
This is essentially a VPN that is done within our web browser and is becoming increasingly common as web browsers are becoming capable of doing anything. Typically these will stream applications or entire desktop sessions to your web browser. A great example of this would be the HackTheBox Pwnbox.