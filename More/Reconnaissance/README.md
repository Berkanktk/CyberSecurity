# Passive Reconnaissance
In passive reconnaissance, you rely on publicly available knowledge. It is the knowledge that you can access from publicly available resources without directly engaging with the target. Think of it like you are looking at target territory from afar without stepping foot on that territory.

* `whois` to query WHOIS servers
* `nslookup` to query DNS servers
* `dig` to query DNS servers

**Online services**  
These two online services allow us to collect information about our target without directly connecting to it.
* DNSDumpster
* Shodan.io

Passive reconnaissance activities include many activities, for instance:
* Looking up DNS records of a domain from a public DNS server.
* Checking job ads related to the target website.
* Reading news articles about the target company.

## whois
A WHOIS server listens on TCP port 43 for incoming requests. The domain registrar is responsible for maintaining the WHOIS records for the domain names it is leasing. The WHOIS server replies with various information related to the domain requested. Of particular interest, we can learn:

* Registrar: Via which registrar was the domain name registered?
* Contact info of registrant: Name, organization, address, phone, among other things. (unless made hidden via a privacy service)
* Creation, update, and expiration dates: When was the domain name first registered? When was it last updated? And when does it need to be renewed?
* Name Server: Which server to ask to resolve the domain name?

**Syntax**  
`whois DOMAIN_NAME`

## nslookup
Find the IP address of a domain name using nslookup, which stands for Name Server Look Up. You need to issue the command `nslookup DOMAIN_NAME`

Or, more generally, you can use nslookup OPTIONS DOMAIN_NAME SERVER. These three main parameters are:
* OPTIONS contains the query type as shown in the table below. For instance, you can use `A` for IPv4 addresses and `AAAA` for IPv6 addresses.
* DOMAIN_NAME is the domain name you are looking up.
* SERVER is the DNS server that you want to query. You can choose any local or public DNS server to query. Cloudflare offers `1.1.1.1` and `1.0.0.1`, Google offers `8.8.8.8` and `8.8.4.4`, and Quad9 offers `9.9.9.9` and `149.112.112.112`. There are many more public DNS servers that you can choose from if you want alternatives to your ISP’s DNS servers.
 
| Query type |       Result       |
|:----------:|:------------------:|
|      A     |   IPv4 Addresses   |
|    AAAA    |   IPv6 Addresses   |
|    CNAME   |   Canonical Name   |
|     MX     |    Mail Servers    |
|     SOA    | Start of Authority |
|     TXT    |     TXT Records    |

For instance, `nslookup -type=A berkankutuk.dk 1.1.1.1` (or `nslookup -type=a berkankutuk.dk 1.1.1.1` as it is case-insensitive) can be used to return all the IPv4 addresses used by berkankutuk.dk.

This lookup is helpful to know from a penetration testing perspective. Each of these IP addresses can be further checked for insecurities, assuming they lie within the scope of the penetration test.

Such pieces of information might prove valuable as you continue the passive reconnaissance of your target. You can repeat similar queries for other domain names and try different types, such as `-type=txt`

## dig
For more advanced DNS queries and additional functionality, you can use `dig`, the acronym for “Domain Information Groper”

We can use dig DOMAIN_NAME, but to specify the record type, we would use `dig DOMAIN_NAME TYPE`
* SERVER is the DNS server that you want to query.
* DOMAIN_NAME is the domain name you are looking up.
* TYPE contains the DNS record type, as shown in the table provided earlier.

# Active Reconnaissance
Active reconnaissance requires you to make some kind of contact with your target. This contact can be a phone call or a visit to the target company under some pretence to gather more information, usually as part of social engineering. Alternatively, it can be a direct connection to the target system, whether visiting their website or checking if their firewall has an SSH port open

Examples of active reconnaissance activities include:
* Connecting to one of the company servers such as HTTP, FTP, and SMTP.
* Calling the company in an attempt to get information (social engineering).
* Entering company premises pretending to be a repairman.

Tools
* traceroute
* telnet
* nc

**Important!**  
Considering the invasive nature of active reconnaissance, one can quickly get into legal trouble unless one obtains proper legal authorisation.

## ping
The primary purpose of ping is to check whether you can reach the remote system and that the remote system can reach you back. In other words, initially, this was used to check network connectivity; however, we are more interested in its different uses: checking whether the remote system is online.

In simple terms, the ping command sends a packet to a remote system, and the remote system replies. This way, you can conclude that the remote system is online and that the network is working between the two systems.

If you prefer a pickier definition, the ping is a command that sends an ICMP Echo packet to a remote system. If the remote system is online, and the ping packet was correctly routed and not blocked by any firewall, the remote system should send back an ICMP Echo Reply. Similarly, the ping reply should reach the first system if appropriately routed and not blocked by any firewall.

If the target isn't online, then the message "Destination Host Unreachable" will be shown. 

Generally speaking, when we don’t get a ping reply back, there are a few explanations that would explain why we didn’t get a ping reply, for example:

* The destination computer is not responsive; possibly still booting up or turned off, or the OS has crashed.
* It is unplugged from the network, or there is a faulty network device across the path.
* A firewall is configured to block such packets. The firewall might be a piece of software running on the system itself or a separate network appliance. Note that MS Windows firewall blocks ping by default.
* Your system is unplugged from the network.

**Command**  
`ping <host_ip>` - ping an ip  
`ping -c <packets> <host_ip>` - specify number of packets to be sent  
## traceroute
As the name suggests, the traceroute command traces the route taken by the packets from your system to another host. The purpose of a traceroute is to find the IP addresses of the routers or hops that a packet traverses as it goes from your system to a target host. This command also reveals the number of routers between the two systems.

There is no direct way to discover the path from your system to a target system. We rely on ICMP to “trick” the routers into revealing their IP addresses. We can accomplish this by using a small Time To Live (TTL) in the IP header field. Although the T in TTL stands for time, TTL indicates the maximum number of routers/hops that a packet can pass through before being dropped; TTL is not a maximum number of time units. When a router receives a packet, it decrements the TTL by one before passing it to the next router. 

The following figure shows that each time the IP packet passes through a router, its TTL value is decremented by 1. Initially, it leaves the system with a TTL value of 64; it reaches the target system with a TTL value of 60 after passing through 4 routers
![TTL](/Images/TTL.png)

However, if the TTL reaches 0, it will be dropped, and an ICMP Time-to-Live exceeded would be sent to the original sender. Note that some routers are configured not to send such ICMP messages when discarding a packet.

"*" in a traceroute indicates that our system didn’t receive the expected ICMP time exceeded in-transit messages.

 If you are running a traceroute to a system within your network, the route will be unlikely to change. However, we cannot expect the route to remain fixed when the packets need to go via other routers outside our network.

To summarize, we can notice the following:

* The number of hops/routers between your system and the target system depends on the time you are running traceroute. There is no guarantee that your packets will always follow the same route, even if you are on the same network or you repeat the traceroute command within a short time.
* Some routers return a public IP address. You might examine a few of these routers based on the scope of the intended penetration testing.
* Some routers don’t return a reply.

**Commands:**  
`traceroute <ip>` - Linux and MacOS  
`tracert <ip>` - Windows
## telnet
The TELNET (Teletype Network) protocol was developed in 1969 to communicate with a remote system via a command-line interface (CLI). Hence, the command telnet uses the TELNET protocol for remote administration. The default port used by telnet is 23. From a security perspective, telnet sends all the data, including usernames and passwords, in cleartext. Sending in cleartext makes it easy for anyone, who has access to the communication channel, to steal the login credentials. The secure alternative is SSH (Secure SHell) protocol.

Knowing that telnet client relies on the TCP protocol, you can use Telnet to connect to any service and grab its banner. Using `telnet <ip> <port>`, you can connect to any service running on TCP and even exchange a few messages unless it uses encryption.
## netcat
Netcat supports both TCP and UDP protocols. It can function as a client that connects to a listening port; alternatively, it can act as a server that listens on a port of your choice. Hence, it is a convenient tool that you can use as a simple client or server over TCP or UDP.

You can use netcat to listen on a TCP port and connect to a listening port on another system.

On the server system, where you want to open a port and listen on it, you can issue `nc -lp 1234` or better yet, `nc -vnlp 1234`, which is equivalent to `nc -v -l -n -p 1234`. 

| option | meaning |
|:---:|:---:|
| -l | Listen mode |
| -p | Specify the Port number |
| -n | Numeric only; no resolution of hostnames via DNS |
| -v | Verbose output (optional, yet useful to discover any bugs) |
| -vv | Very Verbose (optional) |
| -k | Keep listening after client disconnects |

**Notes:**  
* the option `-p` should appear just before the port number you want to listen on.
* the option `-n` will avoid DNS lookups and warnings.
* port numbers less than 1024 require root privileges to listen on.

**Commands:**  
`nc MACHINE_IP PORT` - connect to a server

Consider the following example. On the server-side, we will listen on port 1234. We can achieve this with the command `nc -vnlp 1234`. In our case, the listening server has the IP address 10.10.118.160, so we can connect to it from the client-side by executing `nc 10.10.118.160 1234`. This setup would echo whatever you type on one side to the other side of the TCP tunnel. 

## Putting it all together
It is easy to put a few of them together via a shell script to build a primitive network and system scanner. You can use traceroute to map the path to the target, ping to check if the target system responds to ICMP Echo, and telnet to check which ports are open and reachable by attempting to connect to them. 

| Command | Example |
|:---:|:---:|
| ping | `ping -c <number> <ip>` on Linux or macOS |
| ping | `ping -n <number> <ip>` on MS Windows |
| traceroute | `traceroute <ip>` on Linux or macOS |
| tracert | `tracert <ip>` on MS Windows |
| telnet | `telnet <ip> <port>` |
| netcat as client | `nc <ip> <port>` |
| netcat as server | `nc -lvnp <port>` |