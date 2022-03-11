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
## traceroute
## telnet
## netcat
## Putting it all together