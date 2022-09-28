# Nmap states
1. **Open**: indicates that a service is listening on the specified port.
2. **Closed**: indicates that no service is listening on the specified port, although the port is accessible. By accessible, we mean that it is reachable and is not blocked by a firewall or other security appliances/programs.
3. **Filtered**: means that Nmap cannot determine if the port is open or closed because the port is not accessible. This state is usually due to a firewall preventing Nmap from reaching that port. Nmap’s packets may be blocked from reaching the port; alternatively, the responses are blocked from reaching Nmap’s host.
4. **Unfiltered**: means that Nmap cannot determine if the port is open or closed, although the port is accessible. This state is encountered when using an ACK scan `sA`.
5. **Open|Filtered**: This means that Nmap cannot determine whether the port is open or filtered.
6. **Closed|Filtered**: This means that Nmap cannot decide whether a port is closed or filtered.

# TCP Header Flags
1. **URG**: Urgent flag indicates that the urgent pointer filed is significant. The urgent pointer indicates that the incoming data is urgent, and that a TCP segment with the URG flag set is processed immediately without consideration of having to wait on previously sent TCP segments.
2. **ACK**: Acknowledgement flag indicates that the acknowledgement number is significant. It is used to acknowledge the receipt of a TCP segment.
3. **PSH**: Push flag asking TCP to pass the data to the application promptly.
4. **RST**: Reset flag is used to reset the connection. Another device, such as a firewall, might send it to tear a TCP connection. This flag is also used when data is sent to a host and there is no service on the receiving end to answer.
5. **SYN**: Synchronize flag is used to initiate a TCP 3-way handshake and synchronize sequence numbers with the other host. The sequence number should be set randomly during TCP connection establishment.
6. **FIN**: The sender has no more data to send.

# Scanning types
We can use `-F` to enable fast mode and decrease the number of scanned ports from 1000 to 100 most common ports.

**TCP Connect**  
If you are **not a privileged** user (root or sudoer), a TCP connect scan is the only possible option to discover open TCP ports.

If we are interested in learning whether the TCP port is open, not establishing a TCP connection. Hence the connection is torn as soon as its state is confirmed by sending a RST/ACK. You can choose to run TCP connect scan using `-sT`.

An open port replies with a SYN/ACK. And finished with a RST/ACK.

**TCP SYN**  
The default scan mode is SYN scan, and it **requires a privileged** (root or sudoer) user to run it. SYN scan does not need to complete the TCP 3-way handshake; instead, it tears down the connection once it receives a response from the server. Because we didn’t establish a TCP connection, this decreases the chances of the scan being logged. We can select this scan type by using the `-sS` option

An open port replies with a SYN/ACK. And finished with a RST.

**UDP Scan**  
UDP is a connectionless protocol, and hence it does not require any handshake for connection establishment. We cannot guarantee that a service listening on a UDP port would respond to our packets.

However, if a UDP packet is sent to a closed port, an ICMP port unreachable error (type 3, code 3) is returned. You can select UDP scan using the `-sU`

# Fine-Tuning Scope and Performance
## Scope  
* port list: `-p22,80,443` will scan ports 22, 80 and 443.
* port range: `-p1-1023` will scan all ports between 1 and 1023 inclusive
* You can request the scan of all ports by using `-p-`, which will scan all 65535 ports.
* If you want to scan the most common 100 ports, add `-F`
* Using `--top-ports 10` will check the ten most common ports.

## Time  
You can control the scan timing using -T<0-5>. -T0 is the slowest (paranoid), while -T5 is the fastest. According to Nmap manual page, there are six templates:

* paranoid (0)
* sneaky (1)
* polite (2)
* normal (3)
* aggressive (4)
* insane (5)

**When they are used**
- `-T0` scans one port at a time and waits 5 minutes between sending each probe
- `-T1` is often used during real engagements where stealth is more important.
- `-T3` is the default in Nmap, if nothing else is specified. 
- `-T5` is the most aggressive in terms of speed; however, this can affect the accuracy of the scan results due to the increased likelihood of packet loss. 
- `-T4` is often used during CTFs and when learning to scan on practice targets
  
To avoid IDS alerts, you might consider -T0 or -T1

## Packet scope  
Alternatively, you can choose to control the packet rate using `--min-rate <number>` and `--max-rate <number>`. For example, `--max-rate 10` or `--max-rate=10` ensures that your scanner is not sending more than ten packets per second.

