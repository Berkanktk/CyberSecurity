# Wireshark

## Introduction
Wireshark, a tool used for creating and analyzing PCAPs (network packet capture files), is commonly used as one of the best packet analysis tools. In this room, we will look at the basics of installing Wireshark and using it to perform basic packet analysis and take a deep look at each common networking protocol.

### MAC Floods
MAC Floods are a tactic commonly used by red teams as a way of actively sniffing packets. MAC Flooding is intended to stress the switch and fill the CAM table. Once the CAM table is filled the switch will no longer accept new MAC addresses and so in order to keep the network alive, the switch will send out packets to all ports of the switch.

Note: This technique should be used with extreme caution and with explicit prior consent.

## ARP Poisoning
ARP Poisoning is another technique used by red teams to actively sniff packets. By ARP Poisoning you can redirect the traffic from the host(s) to the machine you're monitoring from. This technique will not stress network equipment like MAC Flooding however should still be used with caution and only if other techniques like network taps are unavailable.

## Filtering Captures
and - operator: and / &&  
or - operator: or / ||  
equals - operator: eq / ==  
not equal - operator: ne / !=  
greater than - operator: gt /  >  
less than - operator: lt / <  

## Colors
![Wireshark Colors](../../Images/Wireshark-colors.png)

## Basic Filtering
**Filtering by IP**: The first filter we will look at is ip.addr, this filter will allow you to comb through the traffic and only see packets with a specific IP address contained in those packets, whether it be from the source or destination. 

Syntax: `ip.addr == <IP Address>`

**Filtering by SRC and DST**: The second filter will look at is two in one as well as a filter operator: ip.src and ip.dst. These filters allow us to filter the traffic by the source and destination from which the traffic is coming from.

Syntax: `ip.src == <SRC IP Address> and ip.dst == <DST IP Address>`

**Filtering by TCP Protocols**: The last filter allows you to set a port or protocol to filter by and can be handy when trying to keep track of an unusual protocol or port being used.

Wireshark can filter by both port numbers as well as protocol names.

Syntax: `tcp.port eq <Port #> or <Protocol Name>`
Also works for udp


## Packet Dissection
- You can double click on a packet in capture to open its details. Packets consist of 5 to 7 layers based on the OSI model.
- Frame (Layer 1) -- This will show you what frame / packet you are looking at as well as details specific to the Physical layer of the OSI model.
- Source [MAC] (Layer 2) -- This will show you the source and destination MAC Addresses; from the Data Link layer of the OSI model.
- Source [IP] (Layer 3) -- This will show you the source and destination IPv4 Addresses; from the Network layer of the OSI model.
- Protocol (Layer 4) -- This will show you details of the protocol used (UDP/TCP) along with source and destination ports; from the Transport layer of the OSI model.
- Application Protocol (Layer 5) -- This will show details specific to the protocol being used such HTTP, FTP, SMB, etc. From the Application layer of the OSI model.
- Application Data -- This is an extension of layer 5 that can show the application-specific data.

# Usage and filtering

## ARP Traffic
Sort after opcode  
`arp.opcode == 1` - request  
`arp.opcode == 2` - reply  

## ICMP Traffic

### ICMP Traffic Overview
ICMP or Internet Control Message Protocol is used to analyze various nodes on a network. This is most commonly used with utilities like ping and traceroute.

There are a few important things within the packet details that we can take note of first being the type and code of the packet. A type that equals 8 means that it is a request packet, if it is equal to 0 it is a reply packet. When these codes are altered or do not seem correct that is typically a sign of suspicious activity.

There are two other details within the packet that are useful to analyze: timestamp and data. The timestamp can be useful for identifying the time the ping was requested it can also be useful to identify suspicious activity in some cases. We can also look at the data string which will typically just be a random data string.


## TCP Traffic
TCP or Transmission Control Protocol handles the delivery of packets including sequencing and errors.

Red packet = port is closed

### TCP Packet Analysis
The main thing that we want to look for when looking at a TCP packet is the sequence number and acknowledgment number.

## HTTP Traffic
HTTP is one of the most straight forward protocols for packet analysis, the protocol is straight to the point and does not include any handshakes or prerequisites before communication.

Above we can see a sample HTTP packet, looking at an HTTP packet we can easily gather information since the data stream is not encrypted like the HTTP counterpart HTTPS. Some of the important information we can gather from the packet is the Request URI, File Data, Server.

### Practical HTTP Packet Analysis
Export HTTP Object. This feature will allow us to organize all requested URIs in the capture. To use Export HTTP Object navigate to file > Export Objects > HTTP.

Organize the protocols present in a capture the Protocol Hierarchy. Navigate to Statistics > Protocol Hierarchy.

Organize all endpoints and IPs found within a specific capture. Just like the other features, this can be useful to identify where a discrepancy is originating from. To use the Endpoints feature navigate to Statistics > Endpoints.


## DNS Traffic
DNS or Domain Name Service protocol is used to resolves names with IP addresses

There are a couple of things outlined below that you should keep in the back of your mind when analyzing DNS packets.

Query-Response
DNS-Servers Only
UDP

If anyone of these is out of place then the packets should be looked at further and should be considered suspicious.


### DNS Traffic Overview
The first bit of information we can look at is where the query is originating from

We can also look at what it is querying as well, this can be useful with other information to build a story of what happened

## HTTPS Traffic
HTTPS or Hypertext Transfer Protocol Secure can be one of the most annoying protocols to understand from a packet analysis perspective and can be confusing to understand the steps needed to take in order to analyze HTTPS packets.

### HTTPS Traffic Overview
Before sending encrypted information the client and server need to agree upon various steps in order to make a secure tunnel.

Client and server agree on a protocol version
Client and server select a cryptographic algorithm
The client and server can authenticate to each other; this step is optional
Creates a secure tunnel with a public key

### Practical HTTPS Packet Analysis
We can confirm from the packet details that the Application Data is encrypted. 
You can use an RSA key in Wireshark in order to view the data unencrypted. In order to load an RSA key navigate to Edit > Preferences > Protocols > TLS >  [+] . If you are using an older version of Wireshark then this will be SSL instead of TLS. You will need to fill in the various sections on the menu with the following preferences:  

**IP Address**: 127.0.0.1  
**Port**: start_tls  
**Protocol**: http  
**Keyfile**: RSA key location  

