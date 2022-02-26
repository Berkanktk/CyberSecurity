# OSI vs TCP/IP

OSI refers to Open Systems Interconnection whereas TCP/IP refers to Transmission Control Protocol

| Layer | OSI Model | TCP/IP Model | Protocols | Protocol Data Unit | Description |
|---|---|---|---|---|---|
| 7 | Application | Application | FTP, HTTP, Telnet, SMTP, DNS, SSH | Data | Network Process to application |
| 6 | Presentation | Application | JPEG, PNG, MPEG, Sockets, HTML, IMAP | Data | Data representation and encryption |
| 5 | Session | Application | NFS, SQL, PAP, RPC, RTP, API's | Data | Interhost communication |
| 4 | Transport | Transport | TCP, UDP, SSL, TLS | Segment (TCP) / Datagram (UDP) | End-to-end connection and reliability |
| 3 | Network | Internet | IPv4, IPv6, ICMP | Packet | Path determination (Logical addressing) |
| 2 | Data Link | Network Access | ARP, CDP, STP, VLAN, Switch, Bridge | Frame | MAC and LLC (Physical addressing) |
| 1 | Physical | Network Access | Ethernet, WI-FI, CAT, DSL, RJ45, 100Base-TX, Hub, Repeater | Bits | Media, signal and binary transmission |