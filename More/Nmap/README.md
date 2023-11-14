# Nmap
> Note, there is now a better and much faster alternative to nmap called [rustscan](https://github.com/RustScan/RustScan). 

## RustScan
For Kali, first install Rust and Cargo
```bash	
curl https://sh.rustup.rs -sSf | sh
```

Then install RustScan

```bash
wget https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb
```

Then run 
```bash
sudo dpkg -i rustscan_2.0.1_amd64.deb
```

Usage
```bash
rustscan -a <ip> 
```

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

**Null Scan**    
A null scan is a type of TCP scan where the TCP header flags are set to 0. This scan is also known as a stealth scan because it does not set any bits in the TCP header. This scan is used to determine firewall rulesets. You can select this scan type by using the `-sN` option.

A lack of reply in a null scan indicates that either the port is open or a firewall is blocking the packet.

**FIN Scan**  
The FIN scan sends a TCP packet with the FIN flag set. You can choose this scan type using the `-sF` option. Similarly, no response will be sent if the TCP port is open. Again, Nmap cannot be sure if the port is open or if a firewall is blocking the traffic related to this TCP port.

However, the target system should respond with an RST if the port is closed.

**Xmas Scan**  
The Xmas scan gets its name after Christmas tree lights. An Xmas scan sets the FIN, PSH, and URG flags simultaneously. You can select Xmas scan with the option `-sX`.

Like the Null scan and FIN scan, if an RST packet is received, it means that the port is closed. Otherwise, it will be reported as open|filtered.

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

# Spoofing and Decoys
In some network setups, you will be able to scan a target system using a spoofed IP address and even a spoofed MAC address. Such a scan is only beneficial in a situation where you can guarantee to capture the response

The following figure shows the attacker launching the command `nmap -S SPOOFED_IP MACHINE_IP`. Consequently, Nmap will craft all the packets using the provided source IP address `SPOOFED_IP`. The target machine will respond to the incoming packets sending the replies to the destination IP address `SPOOFED_IP`. For this scan to work and give accurate results, the attacker needs to monitor the network traffic to analyze the replies.

In general, you expect to specify the network interface using `-e` and to explicitly disable ping scan -Pn. Therefore, instead of `nmap -S SPOOFED_IP MACHINE_IP`, you will need to issue `nmap -e NET_INTERFACE -Pn -S SPOOFED_IP MACHINE_IP` to tell Nmap explicitly which network interface to use and not to expect to receive a ping reply. It is worth repeating that this scan will be useless if the attacker system cannot monitor the network for responses.

When you are on the same subnet as the target machine, you would be able to spoof your MAC address as well. You can specify the source MAC address using `--spoof-mac SPOOFED_MAC`. This address spoofing is only possible if the attacker and the target machine are on the same Ethernet (802.3) network or same WiFi (802.11).

## Decoys
You can launch a decoy scan by specifying a specific or random IP address after `-D`. For example, `nmap -D 10.10.0.1,10.10.0.2,ME MACHINE_IP` will make the scan of MACHINE_IP appear as coming from the IP addresses 10.10.0.1, 10.10.0.2, and then `ME` to indicate that your IP address should appear in the third order. 

Another example command would be `nmap -D 10.10.0.1,10.10.0.2,RND,RND,ME MACHINE_IP`, where the third and fourth source IP addresses are assigned randomly, while the fifth source is going to be the attacker’s IP address. In other words, each time you execute the latter command, you would expect two new random IP addresses to be the third and fourth decoy sources.

So in short, `-S` for make a scan appear as if coming from the source IP address instead of your IP adres, and `-D` for making a scan appear as if coming from the decoy IP addresses (in addition to your IP address).

```bash	
nmap -n -D decoy-ip1,decoy-ip2,your-own-ip,decoy-ip3,decoy-ip4 remote-host-ip
nmap -n -D 192.168.1.5,10.5.1.2,172.1.2.4,3.4.2.1 192.168.1.5

# Or even a better way to hide your IP
nmap -P0 -sI 1.1.1.1:1234 192.1.2.3
```
> Following example, uses an an idle scan technique. It uses port 1234 on 1.1.1.1 IP as as a zombie to scan host – 192.1.2.3:


# Fragmented Packets
You can use the `-f` option to fragment the packets. This option is useful when you want to bypass a firewall that is configured to block fragmented packets. You can also use the `-f` option to bypass IDS/IPS systems that are configured to block fragmented packets.

Adding another `-f` (`-f` `-f` or `-ff`) will split the data into 16 byte-fragments instead of 8. You can change the default value by using the `--mtu`; however, you should always choose a multiple of 8.

# Idle/Zombie Scan
Idle scan is also known as zombie scan. It is a stealth scan technique that allows an attacker to scan a target system without sending packets to the target directly. Instead, the attacker uses a third-party system to send the packets to the target system. The third-party system is called a zombie system. The attacker uses the zombie system to send the packets to the target system and then analyzes the responses from the target system to determine the open ports.

You can run an idle scan using `nmap -sI ZOMBIE_IP MACHINE_IP`, where `ZOMBIE_IP` is the IP address of the idle host (zombie).

# Getting More Details
You might consider adding `--reason` if you want Nmap to provide more details regarding its reasoning and conclusions

Providing the `--reason` flag gives us the explicit reason why Nmap concluded that the system is up or a particular port is open

For more detailed output, you can consider using `-v` for verbose output or `-vv` for even more verbosity.

If `-vv` does not satisfy your curiosity, you can use `-d` for debugging details or `-dd` for even more details. You can guarantee that using `-d` will create an output that extends beyond a single screen.

# Service Detection
Nmap can detect the services running on the target system. This is useful when you want to identify the version of the service running on the target system. You can use `-sV` to enable service detection.

You can control the intensity with `--version-intensity LEVEL` where the level ranges between 0, the lightest, and 9, the most complete. `-sV --version-light` has an intensity of 2, while` -sV --version-all` has an intensity of 9.

It is important to note that using `-sV` will force Nmap to proceed with the TCP 3-way handshake and establish the connection. The connection establishment is necessary because Nmap cannot discover the version without establishing a connection fully and communicating with the listening service. 

> In other words, stealth SYN scan -sS is not possible when -sV option is chosen.

# OS Detection
Nmap can detect the operating system running on the target system. This is useful when you want to identify the operating system running on the target system. You can use `-O` to enable OS detection.

# Trace Route
You can use `--traceroute` to enable trace route. This is useful when you want to identify the path that the packets take to reach the target system.

# Nmap Scripting Engine
Nmap Scripting Engine (NSE) is a powerful feature that allows you to write scripts to automate tasks. NSE is a collection of scripts that are used to automate a variety of tasks. NSE scripts are written in Lua programming language. NSE scripts are located in the directory `/usr/share/nmap/scripts/`.

You can specify to use any or a group of these installed scripts; moreover, you can install other user’s scripts and use them for your scans. 

You can choose to run the scripts in the default category using `--script=default` or simply adding `-sC`.

| Script Category | Description |
|:---:|:---:|
| auth | Authentication related scripts |
| broadcast | Discover hosts by sending broadcast messages |
| brute | Performs brute-force password auditing against logins |
| default | Default scripts, same as -sC |
| discovery | Retrieve accessible information, such as database tables and DNS names |
| dos | Detects servers vulnerable to Denial of Service (DoS) |
| exploit | Attempts to exploit various vulnerable services |
| external | Checks using a third-party service, such as Geoplugin and Virustotal |
| fuzzer | Launch fuzzing attacks |
| intrusive | Intrusive scripts such as brute-force attacks and exploitation |
| malware | Scans for backdoors |
| safe | Safe scripts that won’t crash the target |
| version | Retrieve service versions |
| vuln | Checks for vulnerabilities or exploit vulnerable services |

`-sC` Can recover public keys, retrieve default page titles, etc.

You can also specify the script by name using `--script "SCRIPT-NAME"`. Ex. `http-date` retrieves the http server date and time: 
```bash	
sudo nmap -sS -n --script "http-date" MACHINE_IP
```

# Saving the Output
You can save the output of the scan to a file using `-oN FILENAME`. The output will be saved in normal format. You can also save the output in XML format using `-oX FILENAME`, or even in a grepable format using `-oG FILENAME`.

# Summary
| Scan Type | Example Command |
|:---:|:---:|
| ARP Scan | sudo nmap -PR -sn MACHINE_IP/24 |
| ICMP Echo Scan | sudo nmap -PE -sn MACHINE_IP/24 |
| ICMP Timestamp Scan | sudo nmap -PP -sn MACHINE_IP/24 |
| ICMP Address Mask Scan | sudo nmap -PM -sn MACHINE_IP/24 |
| TCP SYN Ping Scan | sudo nmap -PS22,80,443 -sn MACHINE_IP/30 |
| TCP ACK Ping Scan | sudo nmap -PA22,80,443 -sn MACHINE_IP/30 |
| UDP Ping Scan | sudo nmap -PU53,161,162 -sn MACHINE_IP/30 |
| TCP Connect Scan | nmap -sT MACHINE_IP |
| TCP SYN Scan | sudo nmap -sS MACHINE_IP |
| UDP Scan | sudo nmap -sU MACHINE_IP |
| TCP Null Scan | sudo nmap -sN MACHINE_IP |
| TCP FIN Scan | sudo nmap -sF MACHINE_IP |
| TCP Xmas Scan | sudo nmap -sX MACHINE_IP |
| TCP Maimon Scan | sudo nmap -sM MACHINE_IP |
| TCP ACK Scan | sudo nmap -sA MACHINE_IP |
| TCP Window Scan | sudo nmap -sW MACHINE_IP |
| Custom TCP Scan | sudo nmap --scanflags URGACKPSHRSTSYNFIN MACHINE_IP |
| Spoofed Source IP | sudo nmap -S SPOOFED_IP MACHINE_IP |
| Spoofed MAC Address | --spoof-mac SPOOFED_MAC |
| Decoy Scan | nmap -D DECOY_IP,ME MACHINE_IP |
| Idle (Zombie) Scan | sudo nmap -sI ZOMBIE_IP MACHINE_IP |
| Fragment IP data into 8 bytes | -f |
| Fragment IP data into 16 bytes | -ff |

| Option | Purpose |
|:---:|:---:|
| -n | no DNS lookup |
| -R | reverse-DNS lookup for all hosts |
| -sn | host discovery only |
| -p- | all ports |
| -p1-1023 | scan ports 1 to 1023 |
| -F | 100 most common ports |
| -r | scan ports in consecutive order |
| -T<0-5> | -T0 being the slowest and T5 the fastest |
| --max-rate 50 | rate <= 50 packets/sec |
| --min-rate 15 | rate >= 15 packets/sec |
| --min-parallelism 100 | at least 100 probes in parallel |
| --source-port PORT_NUM | specify source port number |
| --data-length NUM | append random data to reach given length |
| --reason | explains how Nmap made its conclusion |
| -v | verbose |
| -vv | very verbose |
| -d | debugging |
| -dd | more details for debugging |
| -sV | determine service/version info on open ports |
| -sV --version-light | try the most likely probes (2) |
| -sV --version-all | try all available probes (9) |
| -O | detect OS |
| --traceroute | run traceroute to target |
| --script=SCRIPTS | Nmap scripts to run |
| -sC or --script=default | run default scripts |
| -A | equivalent to -sV -O -sC --traceroute |
| -oN | save output in normal format |
| -oG | save output in grepable format |
| -oX | save output in XML format |
| -oA | save output in normal, XML and Grepable formats |