# Networking Models
![OSI vs TCP-IP](/Images/OSIvsTCP-IP.png)
## OSI 
The OSI model, often referred to as ISO/OSI layer model, is a reference model that can be used to describe and define the communication between systems. The reference model has seven individual layers, each with clearly separated tasks.

The term OSI stands for Open Systems Interconnection model, published by the International Telecommunication Union (ITU) and the International Organization for Standardization (ISO). Therefore, the OSI model is often referred to as the ISO/OSI layer model

## TCP-IP
TCP/IP (Transmission Control Protocol/Internet Protocol) is a generic term for many network protocols. The protocols are responsible for the switching and transport of data packets on the Internet. The Internet is entirely based on the TCP/IP protocol family. However, TCP/IP does not only refer to these two protocols but is usually used as a generic term for an entire protocol family.

For example, ICMP (Internet Control Message Protocol) or UDP (User Datagram Protocol) belongs to the protocol family. The protocol family provides the necessary functions for transporting and switching data packets in a private or public network.

## OSI vs TCP/IP
TCP/IP is a communication protocol that allows hosts to connect to the Internet. It refers to the Transmission Control Protocol used in and by applications on the Internet. In contrast to OSI, it allows a lightening of the rules that must be followed, provided that general guidelines are followed.

OSI, on the other hand, is a communication gateway between the network and end-users. The OSI model is usually referred to as the reference model because it is older. It is also known for its strict protocol and limitations.

| Layer | OSI Model | TCP/IP Model | Protocols | Protocol Data Unit | Description |
|---|---|---|---|---|---|
| 7 | Application | Application | FTP, HTTP, Telnet, SMTP, DNS, SSH | Data | Network Process to application |
| 6 | Presentation | Application | JPEG, PNG, MPEG, Sockets, HTML, IMAP | Data | Data representation and encryption |
| 5 | Session | Application | NFS, SQL, PAP, RPC, RTP, API's | Data | Interhost communication |
| 4 | Transport | Transport | TCP, UDP, SSL, TLS | Segment (TCP) / Datagram (UDP) | End-to-end connection and reliability |
| 3 | Network | Internet | IPv4, IPv6, ICMP | Packet | Path determination (Logical addressing) |
| 2 | Data Link | Network Access | ARP, CDP, STP, VLAN, Switch, Bridge | Frame | MAC and LLC (Physical addressing) |
| 1 | Physical | Network Access | Ethernet, WI-FI, CAT, DSL, RJ45, 100Base-TX, Hub, Repeater | Bits | Media, signal and binary transmission |

<details>
<summary><h3>What are Packets and Frames?</h3></summary>

Packets and frames are small pieces of data that, when forming together, make a larger piece of information or message. However, they are two different things in the OSI model. A frame is at layer 2 - the data link layer, meaning there is no such information as IP addresses. Think of this as putting an envelope within an envelope and sending it away. The first envelope will be the packet that you mail, but once it is opened, the envelope within still exists and contains data (this is a frame).

This process is called encapsulation. At this stage, it's safe to assume that when we are talking about anything IP addresses, we are talking about packets. When the encapsulating information is stripped away, we're talking about the frame itself.

Packets are an efficient way of communicating data across networked devices such as those explained in Task 1. Because this data is exchanged in small pieces, there is less chance of bottlenecking occurring across a network than large messages being sent at once.

For example, when loading an image from a website, this image is not sent to your computer as a whole, but rather small pieces where it is reconstructed on your computer. Take the image below as an illustration of this process. The dog's picture is divided into three packets, where it is reconstructed when it reaches the computer to form the final image.

![Packet](../../Images/Packets.png)

Packets have different structures that are dependant upon the type of packet that is being sent. As we'll come on to discuss, networking is full of standards and protocols that act as a set of rules for how the packet is handled on a device. With the Internet predicted to have approximately 50 billion devices connected by the end of 2020, things quickly get out of hand if there is no standardisation.

Let's continue with our example of the Internet Protocol. A packet using this protocol will have a set of headers that contain additional pieces of information to the data that is being sent across a network.

Some notable headers include:
* Time to Live (TTL) - This is a value that is decremented by one each time the packet is forwarded by a router. If the TTL reaches 0, the packet is discarded. This is to prevent packets from being forwarded indefinitely.
* Source and Destination IP - This is the IP address of the sender and the receiver. This is used to identify the source and destination of the packet.
* Checksum - This is a value that is used to check the integrity of the packet. If the checksum is incorrect, the packet is discarded.

</details>

## PDU
In a layered system, devices in a layer exchange data in a different format called a protocol data unit (PDU). For example, when we want to browse a website on the computer, the remote server software first passes the requested data to the application layer. It is processed layer by layer, each layer performing its assigned functions.

![OSI vs TCP-IP](/Images/OSIvsTCP-IP-PDU.png)

During the transmission, each layer adds a header to the PDU from the upper layer, which controls and identifies the packet. This process is called encapsulation. The header and the data together form the PDU for the next layer. The process continues to the Physical Layer or Network Layer, where the data is transmitted to the receiver. The receiver reverses the process and unpacks the data on each layer with the header information. After that, the application finally uses the data. This process continues until all data has been sent and received.

![OSI vs TCP-IP](/Images/Packet-transfer.png)