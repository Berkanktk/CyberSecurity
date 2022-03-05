# List of Contents
1. [Concepts](#concepts)
   1. [Hashing](#hashing)
   2. [Encryption](#encryption)
   3. [Encoding](#encoding)
2. [Links](#links)
3. [Services](#services)
4. [Terms](#terms)
5. [Principles and Standards](#principles-and-standards)
   1. [CIA Triad](#cia-triad)
   2. [Principle of privileges](#principles-of-privileges)
   3. [Security Models](#security-models)
   4. [Threat modeling and incidence response](#threat-modeling-and-incidence-response)
   5. [Ethics](#ethics)
   6. [Methodologies](#methodologies)
   7. [Black, grey & white box](#black-grey--white-box)
   8. [ISO27001](#iso27001)
6. [Overview of tools](#overview-of-tools)
7. [Tools (CLI)](#tools-cli)
   1. [Aircrack-ng](#aircrack-ng)
   2. [Gobuster](#gobuster)
   3. [Hashcat](#hashcat)
   4. [Hydra](#hydra)
   5. [John The Ripper](#john-the-ripper)
   6. [Metasploit](#metasploit)
   7. [Nessus](#nessus)
   8. [Netcat](#netcat)
   9. [Nikto](#nikto-2)
   10. [Nmap](#nmap)
8. [Tools (GUI)](#tools-gui)
   1. [Burp Suite](#burp)
   2. [Wireshark](#wireshark)
9.  [Text Editors](#text-editors)
    1.  [Nano](#nano)
    2.  [VIM](#vim)
10. [Linux Commands](#linux-commands)
11. [Steps](#steps)
    1. [Content Discovery](#content-discovery)
    2. [Privilege Escalation](#privilege-escalation)
    3. [Phishing](#phishing)
 1. [Cryptology](#cryptology)
    1. [Steganography](#steganography)
12. [Networking](#networking) 
13. [Vulnerabilities](#vulnerabilities)
    1.  [SQL Injection](#sql-injection)
    2.  [XSS](#xss-cross-site-scripting)
    3.  [Printer Hacking](#printer-hacking-ipp)

# Concepts
## Hashing
Hashing is used for 2 main purposes in Cyber Security. To verify integrity of data, or for verifying passwords. 

plaintext ➡️ hash  
hash ⛔ plaintext

Doing a lookup in a sorted list of hashes that are not salted is quite fast, much much faster than trying to crack the hash. But in case we have to crack, then its done by hashing a large number of different inputs (often rockyou.txt, these are the possible passwords), potentially adding the salt if there is one and comparing it to the target hash. 

Tools like Hashcat and John the Ripper are normally used for this.

## Encryption
### Symetric encryption
plaintext ➡️ 🔑 ➡️ ciphertext  
plaintext ⬅️ 🔑 ⬅️ ciphertext  
(🔑 shared key)

### Asymetric encryption
plaintext ➡️ 🔑 ➡️ ciphertext  
plaintext ⬅️ 🗝 ⬅️ ciphertext  
(🔑 public key, 🗝 private key

Public key to encrypt, private key to decrypt.

## Encoding
Encoded data can be decoded immediately, without keys. It's NOT a form of encryption, it just a way of representing data.

A very popular encoding is Base64

# Links
[AI Generated Photos](https://generated.photos) - 100.000 AI generated faces.    
[Archive.org](https://archive.org/web/) - internet Archieve    
[Bcrypt Generator](https://bcrypt-generator.com) - a simple bcrypt generator     
[Can I use](https://caniuse.com) - provides up-to-date browser support tables for support of front-end web technologies.      
[Cheatography](https://www.cheatography.com/) - over 3,000 free cheat sheets, revision aids and quick references.    
[CodeBeautify](https://codebeautify.org) - code Beautifier, Viewer and converter    
[Common ports](https://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-en-4/ch-ports.html) - a lists of the most common ports    
[Convert Binary](https://www.convertbinary.com) - a wide range of different converters for binary numbers      
[Convertcsv](https://www.convertcsv.com/sql-to-csv.htm) - convert SQL to CSV     
[Crackstation (Rainbow tables)](https://crackstation.net) - hash cracker      
[CSS Reference](https://cssreference.io) - CSS reference    
[CVE Details](https://www.cvedetails.com/) - CVE security vulnerability advanced database.      
[CVE Mitre](https://cve.mitre.org) - list of publicly known cybersecurity vulnerabilities.      
[CyberChef](https://gchq.github.io/CyberChef/) - a web app for encryption, encoding, compression and data analysis.     
[Cybercrime Tracker](https://cybercrime-tracker.net) - monitors and tracks various malware families that are used to perpetrate cyber crimes.  
[dCode](https://www.dcode.fr/en) - dcode.fr has many decoders for a lot of ciphers  
[dehashed](https://www.dehashed.com/) - is a hacked database search engine.      
[DNSDumpster](https://dnsdumpster.com) - free domain research tool that can discover hosts related to a domain    
[ExploitDB](https://www.exploit-db.com) - searchable archive from The Exploit Database.      
[fakenamegenerator](https://www.fakenamegenerator.com) - your randomly generated identity.     
[File Signature](https://www.garykessler.net/library/file_sigs.html) -  a table of file signatures (aka "magic numbers")   
[Google advanced search](https://www.google.dk/advanced_search) - google dorking made easy      
[Google Hacking Database](https://www.exploit-db.com/google-hacking-database) - juicy information found by dorking      
[GTFOBins](https://gtfobins.github.io) - list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.    
[Hash Analyzer](https://www.tunnelsup.com/hash-analyzer/) - tool to identify hash types      
[have i been pwned?](https://haveibeenpwned.com) - check if you have an account that has been compromised in a data breach.      
[hilite.me](http://hilite.me) - converts your code snippets into pretty-printed HTML formats    
[HSV to RGB](https://www.rapidtables.com/convert/color/hsv-to-rgb.html) - HSV to RGB color converter     
[HTML Reference](https://htmlreference.io) - HTML reference    
[HTTrack](https://www.httrack.com) - website copier      
[Image Color Picker](https://imagecolorpicker.com) - select a color and get the HTML Color Code of this pixel     
[k8s-security](https://github.com/kabachook/k8s-security) - kubernetes security notes and best practices.      
[Keybase](https://keybase.io/) - it's open source and powered by public-key cryptography.    
[malc0de](http://malc0de.com/database) - malware search engine.   
[MD5 Online](https://www.md5online.org/md5-decrypt.html) - md5Online offers several tools related to the MD5 cryptographic algorithm.     
[Observatory by Mozilla](https://observatory.mozilla.org)- set of tools to analyze your website.      
[PDF24](https://tools.pdf24.org/) - free and easy to use online PDF tools     
[Ping.eu](https://ping.eu/) - online Ping, Traceroute, DNS lookup, WHOIS and others.      
[pipl](https://pipl.com/) - is the place to find the person behind the email address, social username or phone number.     
[Regex101](https://regex101.com) - online regex tester and debugger: PHP, PCRE, Python, Golang and JavaScript.    
[RegEx Pal](https://www.regexpal.com/) - online regex testing tool + other tools.      
[RegExr](https://regexr.com/) - online tool to learn, build, & test Regular Expressions (RegEx / RegExp).      
[ShellCheck](https://www.shellcheck.net) - finds bugs in your shell scripts.     
[sploitus](https://sploitus.com) - the exploit and tools database.      
[SSL Scanner](http://www.ssltools.com) - analyze website security.      
[Steganographic Decoder](https://futureboy.us/stegano/decinput.html) - decodes the payload that was hidden in a JPEG image or a WAV or AU audio file     
[Subnet Calculator](https://www.calculator.net/ip-subnet-calculator.html) - IPv4 to IPv6 subnet calculator     
[Subnet Cheatsheet](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/) - subnet cheatsheet  
[urlscan.io](https://urlscan.io) - service to scan and analyse websites.      
[urlvoid ](https://www.urlvoid.com) - this service helps you detect potentially malicious websites.      
[ViewDNS](http://viewdns.info) - one source for free DNS related tools and information.      
[VirusTotal](https://www.virustotal.com/gui/home/upload) - analyze suspicious files and URLs to detect types of malware.      
[WebToolHub-LE](https://www.webtoolhub.com/tn561364-link-extractor.aspx) - HTML hyperlink extractor      
[WebToolHub](https://www.webtoolhub.com) - lots of different web tools     
[WHOIS lookup](https://whois.domaintools.com) - best whois lookup    
[Wigle](https://wigle.net) - is a website for collecting information about the different wireless hotspots around the world      

# Services
## Active directory (Windows)
Active Directory is a collection of machines and servers connected inside of domains, that are a collective part of a bigger forest of domains, that make up the Active Directory network. 

Other related terms include: Domain controllers, Trusts & Policies, Services, Authentication & Cloud security.

## Network security
An Intrusion Detection System (IDS) is a system that detects network or system intrusions.  

An Intrusion Detection and Prevention System (IDPS) or simply Intrusion Prevention System (IPS) is a system that can detect and prevent intrusions.

IDS setups can be divided based on their location in the network into:
* Host-based IDS (HIDS)
* Network-based IDS (NIDS)

The host-based IDS (HIDS) is installed on an OS along with the other running applications. This setup will give the HIDS the ability to monitor the traffic going in and out of the host; moreover, it can monitor the processes running on the host.

The network-based IDS (NIDS) is a dedicated appliance or server to monitor the network traffic. The NIDS should be connected so that it can monitor all the network traffic of the network or VLANs we want to protect. This can be achieved by connecting the NIDS to a monitor port on the switch. The NIDS will process the network traffic to detect malicious traffic.

# Terms
**Active reconnaissance** - Directly interacting with the system.  
**Passive reconnaissance** - We rely on publicly available information.   
**IDOR** - IDOR stands for Insecure Direct Object Reference and is a type of access control vulnerability.    
**Proxy** -  `TO BE ADDED`   
**SSL/TLS** - `TO BE ADDED`  
**XSS** - Cross-Site Scripting is a security vulnerability that's typically found in web applications which can be used to execute a malicious script on the target's machine  
**IPP** - Internet Printing Protocol  
**Hash collision** -  When 2 different inputs give the same output  
**Rainbow tables** - A rainbow table is a lookup table of hashes to plaintexts  
**SAM** -  Security Account Manager is a database that is present on computers running Windows that stores user accounts and security descriptors for users on the local computer  
**Ciphertext** - The result of encrypting a plaintext, encrypted data  
**Cipher** - A method of encrypting or decrypting data. Modern ciphers are cryptographic, but there are many non cryptographic ciphers like Caesar.  
**Plaintext** - Data before encryption, often text but not always. Could be a photograph or other file  
**Encryption** - Transforming data into ciphertext, using a cipher.  
**Encoding** - NOT a form of encryption, just a form of data representation like base64. Immediately reversible.  
**Key** - Some information that is needed to correctly decrypt the ciphertext and obtain the plaintext.  
**Passphrase** - Separate to the key, a passphrase is similar to a password and used to protect a key.  
**Asymmetric** encryption - Uses different keys to encrypt and decrypt.  
**Symmetric encryption** - Uses the same key to encrypt and decrypt  
**Brute force** - Attacking cryptography by trying every different password or every different key  
**Cryptanalysis** - Attacking cryptography by finding a weakness in the underlying maths

# Principles and Standards
## CIA Triad
Consisting of three sections: Confidentiality, Integrity and Availability (CIA), this model has quickly become an industry standard today. This model should help determine the value of data that it applies to, and in turn, the attention it needs from the business.  

**Confidentiality**: This element is the protection of data from unauthorized access and misuse
Integrity

**Integrity**: This element is the condition where information is kept accurate and consistent unless authorized changes are made.

**Availability**:  In order for data to be useful, it must be available and accessible by the user.

## Principles of privileges
It is vital to administrate and correctly define the various levels of access to an information technology system individuals require. 

The levels of access given to individuals are determined on two primary factors:
1. The individual's role/function within the organisation
2. The sensitivity of the information being stored on the system

Two key concepts are used to assign and manage the access rights of individuals, two key concepts are used: Privileged Identity Management (PIM) and Privileged Access Management (or PAM for short).

**PIM** is used to translate a user's role within an organisation into an access role on a system. Whereas **PAM** is the management of the privileges a system's access role has, amongst other things.

What is essential when discussing privilege and access controls is the principle of least privilege. Simply, users should be given the minimum amount of privileges, and only those that are absolutely necessary for them to perform their duties. Other people should be able to trust what people write to.

## Security models
### The Bell-La Padula Model
The Bell-La Padula Model is used to achieve confidentiality. This model has a few assumptions, such as an organisation's hierarchical structure it is used in, where everyone's responsibilities/roles are well-defined.

The model works by granting access to pieces of data (called objects) on a strictly need to know basis. This model uses the rule "no write down, no read up".

The Bell LaPadula Model is popular within organisations such as governmental and military.

### Biba Model
The Biba model is arguably the equivalent of the Bell-La Padula model but for the integrity of the CIA triad.

This model applies the rule to objects (data) and subjects (users) that can be summarised as "no write up, no read down". This rule means that subjects can create or write content to objects at or below their level but can only read the contents of objects above the subject's level.

## Threat modeling and incidence response
Threat modelling is the process of reviewing, improving, and testing the security protocols in place in an organisation's information technology infrastructure and services.

The threat modelling process is very similar to a risk assessment made in workplaces for employees and customers. The principles all return to:
* Preparation
* Identification
* Mitigations
* Review
  
It is, however, a complex process that needs constant review and discussion with a dedicated team. An effective threat model includes:

* Threat intelligence
* Asset identification
* Mitigation capabilities
* Risk assessment

To help with this, there are frameworks such as **STRIDE** (Spoofing identity, Tampering with data, Repudiation threats, Information disclosure, Denial of Service and Elevation of privileges) and **PASTA** (Process for Attack Simulation and Threat Analysis)

## Ethics
### Penetration tests
Before a penetration test starts, a formal discussion occurs between the penetration tester and the system owner. Various tools, techniques, and systems to be tested are agreed on. This discussion forms the scope of the penetration testing agreement and will determine the course the penetration test takes.

### Rules of Engagement (ROE)
The ROE is a document that is created at the initial stages of a penetration testing engagement. This document consists of three main sections:
* Permission
* Test scope
* Rules

### Hat categories
Hackers are sorted into three hats, where their ethics and motivations behind their actions determine what hat category they are placed into.
| Hat | Description |
|---|---|
| Black hat | These people are criminals and often seek to damage organisations or gain some form of financial benefit at the cost of others. |
| Grey hat | These people use their skills to benefit others often; however, they do not respect/follow the law or ethical standards at all times. |
| White hat | These hackers are considered the "good people". They remain within the law and use their skills to benefit others. |

## Methodologies
The steps a penetration tester takes during an engagement is known as the methodology. A practical methodology is a smart one, where the steps taken are relevant to the situation at hand.  
All of them have a general theme of the following stages:
| Stage | Description |
|---|---|
| Information Gathering | This stage involves collecting as much publically accessible information about a target/organisation as possible, for example, OSINT and research.  Note: This does not involve scanning any systems. |
| Enumeration/Scanning | This stage involves discovering applications and services running on the systems. For example, finding a web server that may be potentially vulnerable. |
| Exploitation | This stage involves leveraging vulnerabilities discovered on a system or application. This stage can involve the use of public exploits or exploiting application logic. |
| Privilege Escalation | Once you have successfully exploited a system or application (known as a foothold), this stage is the attempt to expand your access to a system. You can escalate horizontally and vertically, where horizontally is accessing another account of the same permission group (i.e. another user), whereas vertically is that of another permission group (i.e. an administrator). |
| Post-exploitation | This stage involves a few sub-stages: 1. What other hosts can be targeted (pivoting) 2. What additional information can we gather from the host now that we are a privileged user 3. Covering your tracks 4. Reporting |

### OSSTMM
The Open Source Security Testing Methodology Manual provides a detailed framework of testing strategies for systems, software, applications, communications and the human aspect of cybersecurity.

### OWASP
The "Open Web Application Security Project" framework is a community-driven and frequently updated framework used solely to test the security of web applications and services.

### NIST Cybersecurity Framework 1.1
The NIST Cybersecurity Framework is a popular framework used to improve an organisations cybersecurity standards and manage the risk of cyber threats.

### NCSC CAF
The Cyber Assessment Framework (CAF) is an extensive framework of fourteen principles used to assess the risk of various cyber threats and an organisation's defences against these

## Black, grey & white box
There are three primary scopes when testing an application or service. 

| Box | Description |
|---|---|
| Black | This testing process is a high-level process where the tester is not given any information about the inner workings of the application or service. |
| Grey | The tester will have some limited knowledge of the internal components of the application or piece of software. |
| White | The tester will have full knowledge of the application and its expected behaviour. |

## ISO27001
ISO (the International Organization for Standardization) is a worldwide federation of national standards bodies (ISO member bodies), where ISO27001 is an international standard on how to manage information security.

ISO/IEC 27001 requires that management:
* Systematically examine the organization's information security risks, taking account of the threats, vulnerabilities, and impacts
* Design and implement a coherent and comprehensive suite of information security controls and/or other forms of risk treatment (such as risk avoidance or risk transfer) to address those risks that are deemed unacceptable; and
* Adopt an overarching management process to ensure that the information security controls continue to meet the organization's information security needs on an ongoing basis.

An ISMS(Information Security Management System) may be certified compliant with ISO/IEC 27001 by a number of Accredited Registrars worldwide.

# Overview of Tools
[Aircrack-ng](https://www.aircrack-ng.org) - is a complete suite of tools to assess WiFi network security  
[Burp Suite](https://portswigger.net/burp) - is a tool for testing web app security, intercepting proxy to replay, inject, scan and fuzz.  
[Gobuster](https://github.com/OJ/gobuster) - is a free and open source directory/file & DNS busting tool written in Go.  
[Hashcat](https://hashcat.net/hashcat/) - is world's fastest and most advanced password recovery utility.  
[Hydra](https://github.com/vanhauser-thc/thc-hydra) - is a parallelized login cracker which supports numerous protocols to attack  
[The Ripper](https://www.openwall.com/john/) - is a fast password cracker, currently available for many flavors of Unix, Windows, and other.  
[Metasploit](https://www.metasploit.com) - is a tool and framework for pentesting, it contains a lot a ready to use exploits.  
[Nano](https://nano-editor.org) - is an easy to use command line text editor    
[Nessus]() - `TO BE ADDED`  
[Netcat](http://netcat.sourceforge.net) - is an utility which reads and writes data across network connections, using the TCP/IP protocol.  
[Nikto 2](https://cirt.net/Nikto2) - is a web server scanner which performs comprehensive tests against web servers for multiple items.  
[Nmap](https://nmap.org) - is a free and open source (license) utility for network discovery and security auditing.  
[Vim](https://www.vim.org) - is a highly configurable text editor.  
[Wireshark](https://www.wireshark.org) - is the world’s foremost and widely-used network protocol analyzer.  

# Tools (CLI)
## Aircrack-ng
`TO BE ADDED`  
https://cheatography.com/itnetsec/cheat-sheets/aircrack-ng-suite/
## Gobuster
GoBuster is a tool used to brute-force URIs (directories and files), DNS subdomains and virtual host names
### Syntax
`gobuster -w wordlist.txt`

### Example:  
`gobuster dir -u http://172.162.39.86 -w /usr/share/wordlists/dirb/megalist.txt` 

### A list of options
`dir` Directory/file brute forcing mode  
`dns` DNS bruteforcing mode

### A list of most useful flags:
`-u` (url) – full target URL (including scheme), or base domain name.  
`-w` (wordlist) – path to the wordlist used for brute forcing (use – for stdin).  
`-a` (user agent string) – specify a user agent string to send in the request header.  
`-e` (print) - Print the full URLs in your console  
`-o` (file) – specify a file name to write the output to.  
`-x` (extensions) – list of extensions to check for, if any.  
`-P` (password) – HTTP Authorization password (Basic Auth only, prompted if missing).  
`-U` (username) – HTTP Authorization username (Basic Auth only).  
`-c <http cookies>` (cookie) - Specify a cookie for simulating your auth  
`-s` (status-codes) - Set status codes that should be interpreted as valid  
`-k` (ssl) - Skip ssl certificate   
`-H` (HTTP) - Specify HTTP header  
## Hashcat
Hashat is a particularly fast, efficient, and versatile hacking tool that assists brute-force attacks by conducting them with hash values of passwords that the tool is guessing or applying.
[Cheatsheet](https://cheatsheet.haax.fr/passcracking-hashfiles/hashcat_cheatsheet/)

### Syntax
`hashcat -m <number> <hash_file> <dict_file>`

### Example 
Dictionary  
`hashcat -m 1800 -a 0 hashed.txt /usr/share/wordlists/rockyou.txt -o output.txt`  
Bruteforce  
`hashcat -m 0 -a 3 -i hashed.txt ?a?a?a?a?a?a?a -o output.txt`

### Flags
`-m` sets the [mode](https://hashcat.net/wiki/doku.php?id=example_hashes)   
`-a` sets the attack mode (0=Straight,1=Combination,3=Bruteforce,6=Hybrid:wlist+mask,7=Hybrid:mask+wlist)  
`-o` output to filename   
`-r` sets rules  
`--status`  keep screen updated   
`--runtime` abort after X seconds   
`--force` sets workload to insane (This can lead to false positives)  
`-i` increment (bruteforce)

### Attack modes
0=Straight  
1=Combination  
3=Bruteforce  
6=Hybrid:wlist+mask  
7=Hybrid:mask+wlist  

### Charsets
`?l`  Lowercase a-z  
`?u`  Uppercase A-Z  
`?d`  Decimals  
`?h`  Hex using lowercase chars    
`?H`  Hex using uppercase chars  
`?s`  Special chars     
`?a`  All (l,u,d,s)  
`?b`  Binary  
## Hydra
Hydra is a tool used to brute-force username and password to different services such as ftp, ssh, telnet, MS-SQL, etc.
### Syntax  
`hydra -options path`  

### Examples:  
Guess SSH credentials using a given username and a list of passwords:  
`hydra -l username -P path/to/wordlist.txt host_ip -t 4 ssh -V`

Guess Telnet credentials using a list of usernames and a single password, specifying a non-standard port and IPv6: 
`hydra -L path/to/usernames.txt -p password -s port -6 host_ip telnet`

Guess FTP credentials using usernames and passwords lists, specifying the number of threads:  
`hydra -L path/to/usernames.txt -P path/to/wordlist.txt -t n_threads host_ip ftp` 

Guess MySQL credentials using a username and a passwords list, exiting when a username/password pair is found:  
`hydra -l username -P path/to/wordlist.txt -f host_ip mysql`

Web form credentials:   
`hydra -l admin -P /usr/share/wordlists/rockyou.txt <ip_adress> http-post-form "/login:username=^USER^&password=^PASS^:F=Username or password invalid" -V`

Guess IMAP credentials on a range of hosts using a list of colon-separated username/password pairs:  
`hydra -C path/to/username_password_pairs.txt imap://[host_range_cidr]`

Guess POP3 credentials on a list of hosts using usernames and passwords lists, exiting when a username/password pair is found:
`hydra -L path/to/usernames.txt -P path/to/wordlist.txt -M path/to/hosts.txt -F pop3`

### A list of most useful options:
`-S` connect via SSL  
`-l` single username  
`-L` wordlist username(s)   
`-p` single password   
`-P` wordlist password(s)    
`-o` FILE write found login/password pairs to FILE instead of stdout  
`-V` verbose mode, see output for every attempt  
`-I` ignore the resume dialog  
`-t <number> `specifies the number of threads to use  
`-u` by default Hydra checks all passwords for one login and then tries the next login. This option loops around the passwords, so the first password is tried on all logins, then the next password.  

## John The Ripper
https://cheatsheet.haax.fr/passcracking-hashfiles/john_cheatsheet/
### SSH Private Key
Hash the private key  
`/root/Tools/'Password Attacks'/john/ssh2john.py id_rsa > hash`

Crack the hash (or a shadow file)
`john hash --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.txt`
## Metasploit
`TO BE ADDED`
## Nessus
`TO BE ADDED`
## Netcat
Netcat aka nc is an extremely versatile tool. It allows users to connect to specific ports and send and receive data. It also allows machines to receive data and connections on specific ports, which makes nc a very popular tool to gain a Reverse Shell.

### Syntax
Computer B (acts as the receiving server):  
`nc -lvnp 6790 > testfile.txt`  
Computer A (acts as the sending client):  
`nc [IP address of computer B] 6790 < testfile.txt`  

### A list of most useful switches:
`-l` Listen to connections (TCP)  
`-v` Enable verbose mode (allows you to see who connected to you)  
`-p` Specify a port to listen to  
`-e` Specify program to execute after connecting to a host  
`-u` Connect to UDP ports    
`-n` Fast scan by disabling DNS resolution  
`-w` Define timeout value  
`-4` IPv4 only   
`-6` IPv6 only  
`>` Server file redirection  
`<` Client file redirection
## Nikto 2 
nikto is a popular web scanning tool that allows users to find common web vulnerabilities. It is commonly used to check for common CVE's such as shellshock, and to get general information about the web server that you're enumerating.

### Syntax
`nikto -h <ip> -port <port>`

### A list of most useful flags:
`-h` Hostname/IP adress  
`-port` Specify ports  
`-nossl` Disable ssl  
`-ssl` Force ssl  
`-id` Specify authentication(username & password)  
`-plugin` Select which plugin to use  
`-update` Update the plugin list  
`--list-plugins`  List all possible plugins to use   
`-output` Output fingerprinted information to a file
## Nmap
Nmap is a utility for network discovery and security auditing.
### Syntax
`nmap -switch1 -switch2 ipaddress`  

Example:  
`nmap -sT -A -p- 172.162.39.86`  

### A list of most useful switches:
TCP scan (Most likely to be filtered)= `-sT`  
TCP Syn Scan (No logging)= `-sS`  
UDP scan (Slow)= `-sU`  

ICMP Scanning (ping sweep) = `-sn`  
Default ping scanning) = `-sP` 
Detect OS = `-O`  
Detect version of services = `-sV`  
Scan with the default nmap scripts = `-sC`  
Disable host discovery and just scan for open ports = `-Pn`  
Change verbosity = `-v`  
Change verbosity level two = `-vv` (It's good practice to *always* increase the verbosity in your scans.)  

Save nmap results in three major formats = `-oA [filename] [target]`  
Save nmap results in a text file = `-oN [filename] [target]`  
Save nmap results in grepable format = `-oG [filename] [target]`  

Aggresive mode (Enable OS detection, version detection, script scanning, and traceroute) = `-A`  
Timing leves (Speed of scans, can make errors) = `-T<Level>` (0-5)  
Port scan (specific)= `-p <port>`   
Port scan (range) = `-p <from>-<to>`  
Port scan (all) = `-p-`  
Activate a script= `—-script=<script_name>`   
Decoy an ip adress =  `-D`  
Fast mode = `-F`
Only open ports = `--open` 

Scan an IPv6 address = `-6` 

Subnet mask with 255.255.255.0 = `<ip>/24`

# Tools (GUI) 
## Burp 
Burp Suite, a framework of web application pentesting tools, is widely regarded as the de facto tool to use when performing web app testing

### Setting up Burp Suite
Download Burp Suite [here](https://portswigger.net/burp/communitydownload)  
Burp Suite requires Java JRE in order to run. Download and install Java [here](https://www.java.com/en/download/)

### Gettin' CA Certified
We need to install a CA certificate as BurpSuite acts as a proxy between your browser and sending it through the internet - It allows the BurpSuite Application to read and send on HTTPS data. 

1. Download [Foxy Proxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/) in order to fully leverage the proxy, we'll have to install the CA certificate included with Burp Suite (otherwise we won't be able to load anything with SSL).
2. Now click on the extension -> Options -> Add -> Fill in the fields with the following values:  
Title = Burp  
Proxy type = HTTP  
Proxy IP adress or DNS name = 127.0.0.1  
Port = 8080  
Username and password is optional.  
1. And hit save.  
2. Finally, click on the FoxyProxy extension icon again and select 'Burp'.
3. With Firefox, navigate to the following address: http://localhost:8080
4. Click on 'CA Certificate' in the top right to download and save the CA Certificate.
5. Now that we've downloaded the CA Certificate, move over to the settings menu in Firefox. Search for 'Certificates' in the search bar.
6. Click on 'View Certificates'. Next, in the Authorities tab click on 'Import' and then OK.

### Overview of Features
* **Proxy** - What allows us to funnel traffic through Burp Suite for further analysis
* **Target** - How we set the scope of our project. We can also use this to effectively create a site map of the application we are testing
* **Intruder** - Incredibly powerful tool for everything from field fuzzing to credential stuffing and more
* **Repeater** - Allows us to 'repeat' requests that have previously been made with or without modification. Often used in a precursor step to fuzzing with the aforementioned Intruder
* **Sequencer** - Analyzes the 'randomness' present in parts of the web app which are intended to be unpredictable. This is commonly used for testing session cookies
* **Decoder** - As the name suggests, Decoder is a tool that allows us to perform various transforms on pieces of data. These transforms vary from decoding/encoding to various bases or URL encoding.
* **Comparer** - Comparer as you might have guessed is a tool we can use to compare different responses or other pieces of data such as site maps or proxy histories (awesome for access control issue testing). This is very similar to the Linux tool diff.
* **Extender** - Similar to adding mods to a game like Minecraft, Extender allows us to add components such as tool integrations, additional scan definitions, and more!
* **Scanner** - Automated web vulnerability scanner that can highlight areas of the application for further manual investigation or possible exploitation with another section of Burp. This feature, while not in the community edition of Burp Suite, is still a key facet of performing a web application test.

### Benefits
1. Requests will by default require our authorization to be sent.
2. We can modify our requests in-line similar to what you might see in a man-in-the-middle attack and then send them on.
3. We can also drop requests we don't want to be sent. This can be useful to see the request attempt after clicking a button or performing another action on the website. 
4. And last but not least, we can send these requests to other tools such as Repeater and Intruder for modification and manipulation to induce vulnerabilities

## Wireshark
`TO BE ADDED`  
https://packetlife.net/media/library/13/Wireshark_Display_Filters.pdf

# Text Editors
## Nano
### Shortcuts
`^G` Display help text.  
`^O` Write the current file to disk  
`^X` Exit nano.  
`^T` Invoke spellc­heck, if installed.  
`^Y` Next screen.  
`^V` Previous screen.  
`^L` Refresh (force redraw) current screen.  
`^J` Justify current paragraph. (Join together broken lines of text until double newline is encoun­tered.)  
`^W` Search for a string or regular expres­sion.  
`^\` Search and replace a string or regular expres­sion  

## Vim
Vim is a free and open-source, screen-based text editor program for Unix

### Modes
Generally speaking, there are three basic modes in Vim:

`Command mode` – allows you to run commands (Default).  
`Insert mode` – allows you to insert/write text.  
`Visual mode` – visual text selector.  

### Basic keybinds
`h` – move the cursor left  
`j` – cursor down  
`k` – cursor up  
`l` – move the cursor right  
`i` – enter the insert mode  
`esc` – enter the command mode  
`$` – move to the end of the line  
`yy` – copy a line  
`p` – paste  
`d` – delete a line  
`x` – cut a character  

### Basic commands:
`:q` – quit  
`:wq` – write & quit  
`:q!` – quit without saving  
`/word` – search for ‘word’ in the document  
`:vimgrep` – grep integration in Vim (allows to search in multiple files)

Find other very usefull commands [here](/More/VIM/README.md), or a full cheatsheet [here](https://vim.rtorr.com).


# Linux Commands 
## ps
Shows the processes for the current shell 

**PID** – the unique process ID   
**TTY** – terminal type that the user is logged into   
**TIME** – amount of CPU in minutes and seconds that the process has been running   
**CMD** – name of the command that launched the process.   


`-a` flag stands for all processes  
`-x` will display all processes even those not associated with the current tty  
`-t` Processes associated with the terminal run
## rm
`-r` Deletes every file in the directory  
`-f` Suppresses all warning prompts 
## mv
Moves files  
Example:
`mv file.txt /tmp`
## top
top command is used to show the Linux processes. It provides a dynamic real-time view of the running system
## kill
Used to kill a process

The most commonly used signals are:

1 (HUP) - Reload a process.  
9 (KILL) - Kill a process.  
15 (TERM) - Gracefully stop a process.

`kill -9 PID_ID`
## find
Syntax: `find where what`

Search for files
`find -name passwords.txt`

Find any file with the extension of ".txt"
`find -name *.txt`

**Location specific options**   
No specification = this folder  
/ = root folder  
. = this folder and its subdirectories  

**Other options**  
`-name` = specify file specific name/descriptions to be found  
`-iname` = Like -name, but the match is case insensitive.  
`-print`  = It prints the pathname of the current file to standard output.  
`-regex`  = True if the whole path of the file matches pattern using expression   
`-type` = With -type, you can use d to only find directories, and f to only find files.  
`-user` = specify owner  
`-size` = specify size
`-perm` = specify permissions

**Time specific**  
min and time. a(acessed), m(modified), c

To put it all together: in order to specify that a file was last accessed more than 30 minutes ago, the option `-amin +30` is used. 

To specify that it was modified less than 7 days ago, the option `-mtime -7` is used. 

When you want to specify that a file was modified within the last 24 hours, the option `-mtime 0` is used.

**Note**  
1. Suppress the output of any possible errors to make the output more readable. This is done by appending `2> /dev/null` to your command. This way, you won’t see any results you’re not allowed to access.
2. The second thing is the `-exec` flag. You can use it in your find command to execute a new command, following the -exec flag, like so: `-exec whoami \;`. (can be used for privilege escalation)
## diff
diff is a command-line utility that allows you to compare two files line by line

Example usage:
`diff a.txt b.txt`
## tail/head
The tail/head command, as the name implies, print the last/first N number of data of the given input

Options:  
`-n <number>` number of lines to show  
`-c <numbers>` number of bytes  
`sort` to sort
## pwd
Find the full Path to our current working directory
## chmod
Chmod allows you to set the different permissions for a file

Example:
`chmod 777 file.txt`

**Permissions**
| Digit    |      Meaning   | 
|----------|:-------------:|
| 1  | That file can be executed |
| 2  | That file can be written to   | 
| 3  | That file can be executed and written to |
| 4  | That file can be read |
| 5  | That file can be read and executed |
| 6  | That file can be written to and read |
| 7  | That file can be read, written to, and executed |

To make a binary file just executable for the owner of the file, you can use:  
`chmod u+x file.txt`
## chown
Change the user and group for any file

`chown user:group file` change user/group  
Example (change the owner):
chown berkan file.txt

`-R` to operate on every file in the directory at once?
## curl
The curl command transfers data to or from a network server, using one of the supported protocols (HTTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, DICT, TELNET, LDAP or FILE). 

Example:
`curl URL`

Another example is saving the output to a file using either:

-o to save the file under a different name  
`curl -o loginpage.html https://tryhackme.com/login`

-O to save the file under the same name:  
`curl -O https://tryhackme.com/login`

Or, you might be interested in fetching the headers silently?  
`curl -I -s https://tryhackme.com`
## wget
The wget command downloads files from HTTP, HTTPS, or FTP connection a network.  

Adding a `-b` switch will allow us to run wget in the background and return the terminal to its initial state.
## apt
apt is a command-line utility for installing, updating, removing, and otherwise managing deb packages
`sudo apt update` This will pull the latest changes from the APT repositories:

`sudo apt upgrade` To upgrade the installed packages to their latest versions

`sudo apt full-upgrade` The difference between **upgrade** and **full-upgrade** is that the later will remove the installed packages if that is needed to upgrade the whole system.

`sudo apt install package_name` Install packages

`sudo apt remove package_name` Remove packages

`sudo apt autoremove` Remove unused packages

`sudo apt list` List packages
## dig
dig command stands for Domain Information Groper. It is used for retrieving information about DNS name servers

`dig [server] [name] [type]`  
`dig google.com` 

Options:  
`-x` Specify IP adress  
`+noall +answer` Detailed information  

Save to a file:  
`dig -f domain_research.txt +short`  
## tar
tar is a command that allows creating, maintain, modify, and extracts files that are archived in the tar format.

The most common example for tar extraction would be:
`tar -xf archive.tar`

`-x` tells tar to extract files from an archive.  
`-f` tells tar that the next argument will be the name of the archive to operate on.
## grep
Search the contents of files for specific values   
`grep "hello world" file.txt`

Search for an ip using regular expressions  
`grep -Eo '[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}'`

**Options**  
`-n` line numbers for every string found  
`-E` regular expressions
## wc
Word count  
`wc -l file.txt` get numbers of entries  

**Options**  
`-l` count number of lines  
`-c` count number of bytes  
`-w` count number of words   
`-m` count number of characters  
## whoami
Find out what user we're currently logged in as
## uname
Prints basic information about the operating system name and system hardware

`uname -a` will print all available information
## ssh
SSH or Secure Shell is a network communication protocol that enables two computers to communicate

Standard use  
`ssh user@ip` and type the password

Specify other ports than 22  
`ssh user@ip -p <port>` and type the password
## hexeditor
Read and modify hex of a file (This tool is also helpful when it comes to CTFs and text is hidden inside a file or when the magic number of a file was altered.)
## gzip
gzip - a file format and a software application used for file compression and decompression. gzip-compressed files have .gz extension.

`gzip filename.txt` compression

Switches:  
`-d` decompression

Example:  
`gzip -d file.gz`
## binwalk
Binwalk allows users to analyze and extract firmware images and helps in identifying code, files, and other information embedded in those, or inside another file
## sudo
Sudo is Linux's 'run as administrator' command

**Options**
`-u <user>` specify user   
`-su` change to root
`-l` list current sudo priviliges   
## hashid
Hashid will analyze and output the potential algorithm that is used to hash your input.  
`hashid hash`
## shasums
**Find SHA1 hash for a file**  
`sha1sum file.txt`

**Find MD5 hash for a file**  
`md5sum file.txt`
## base64
Decrypt base64  
`base64 -d file.txt`
## gpg
Gpg encrypt a file  
`gpg -c data.txt`  
Enter keyphrase

Decrypt the file  
`gpg -d data.txt.gpg`  
Enter keyphrase
## hexdump
hexdump is used to filter and display the specified files, or standard input in a human readable specified format.  

**Syntax**  
hd {options} {files}

**Options**  
`-c` One-byte character display.   
`-C` Canonical hex + ASCII display.
## exiftool
Is a command-line application for reading, writing and editing meta information in a wide variety of files.

Install with:  
`sudo apt install libimage-exiftool-perl`

Usage  
`exiftool file.jpeg`
## fcrackzip 
Is a password cracker that runs on .zip files 

Install  
`sudo apt-get install fcrackzip`

Usage  
`fcrackzip -vbDp <wordlist path> <filepath>`

**Options**  
`-b` for using brute force algorithms.   
`-D` for using a dictionary.  
`-v` for verbose mode.  
`-p` for using a string as a password.
## adduser & addgroup
The syntax for both of these commands are `adduser username` and `addgroup groupname`.

Add a user to a group  
`usermod -a -G <groups seperated by commas> <user>`
## Operators
`>` is the operator for output redirection. Meaning that you can redirect the output of any command to a file  
`>>` does mainly the same thing as >, with one key difference. >> appends the output of a command to a file, instead of erasing it.

# Steps
## Content Discovery
### Manual
1. Check the robots file for disallowed/hiddenpages  
2. Check favicon to find the website frameworks (only works if the website developer doesn't replace this with a custom one)  
Run this to find its md5 hash:  
`curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum`  
Check [this](https://wiki.owasp.org/index.php/OWASP_favicon_database) database to find the framework.

1. Check the sitemap file for disallowed/hidden files

2. Curl HTTP Headers to find potential information about the webserver software and possibly the programming/scripting language in use.   
`curl http://10.10.134.48 -v`  
The -v switch enables verbose mode, which will output the headers

When successfully finding a framework using on of the methods, Framework Stacking can be used afterwards where you check the framework documentation for potential admin portals etc.

### Automated
**What is Automated Discovery?**  
Automated discovery is the process of using tools to discover content rather than doing it manually. This process is automated as it usually contains hundreds, thousands or even millions of requests to a web server. These requests check whether a file or directory exists on a website, giving us access to resources we didn't previously know existed. This process is made possible by using a resource called wordlists.

**What are wordlists?**  
Wordlists are just text files that contain a long list of commonly used words; they can cover many different use cases. For example, a password wordlist would include the most frequently used passwords, whereas we're looking for content in our case, so we'd require a list containing the most commonly used directory and file names.

**Most common Automation tools**   
`ffuf`, `dirb` and `gobuster`.   
I personally use gobuster the most.


### Osint
**Google Hacking / Dorking**   
Google hacking / Dorking utilizes Google's advanced search engine features, which allow you to pick out custom content.  
| Filter | Example | Description |
|---|---|---|
| site | site:berkankutuk.dk | returns results only from the specified website address |
| inurl | inurl:admin | returns results that have the specified word in the URL |
| filetype | filetype:pdf | returns results which are a particular file extension |
| intitle | intitle:admin | returns results that contain the specified word in the title |  

**Wappalyzer**  
Wappalyzer is an online tool and browser extension that helps identify what technologies a website uses, such as frameworks, Content Management Systems (CMS), payment processors and much more, and it can even find version numbers as well. Read more [here](https://www.wappalyzer.com/).  

**Wayback Machine**  
The Wayback Machine is a historical archive of websites that dates back to the late 90s. You can search a domain name, and it will show you all the times the service scraped the web page and saved the contents. This service can help uncover old pages that may still be active on the current website. Find the website [here](https://archive.org/web/).

### Subdomain enumeration

**SSL/TLS Certificates**  
When an SSL/TLS (Secure Sockets Layer/Transport Layer Security) certificate is created for a domain by a CA (Certificate Authority), CA's take part in what's called "Certificate Transparency (CT) logs". These are publicly accessible logs of every SSL/TLS certificate created for a domain name.
The following site consists of a searchable database of certificates that shows current and historical results. [Link](crt.sh) 

**Search Engines**
The following search would only contain results from subdomain names belonging to domain.com:  
`-site:www.domain.com site:*.domain.com` 

**DNS Bruteforce**  
Bruteforce DNS (Domain Name System) enumeration is the method of trying tens, hundreds, thousands or even millions of different possible subdomains from a pre-defined list of commonly used subdomains. Fot this method, the tool [DNSrecon](https://www.kali.org/tools/dnsrecon/) & [Sublist3r](https://github.com/aboul3la/Sublist3r) can be used.

**Virtual Hosts**  
Some subdomains aren't always hosted in publically accessible DNS results, such as development versions of a web application or administration portals. Instead, the DNS record could be kept on a private DNS server or recorded on the developer's machines in their /etc/hosts file (or c:\windows\system32\drivers\etc\hosts file for Windows users) which maps domain names to IP addresses. 

Because web servers can host multiple websites from one server when a website is requested from a client, the server knows which website the client wants from the Host header. We can utilise this host header by making changes to it and monitoring the response to see if we've discovered a new website.

Bruteforce by using the following command: `ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: {domain}" -u http://{IP} -fs {size}`

## Privilege Escalation 
Check for root password
Run: `id`  
Run: `sudo -l`  
Locate password folder and crack it using johntheripper  
Or use [GTFOBins](https://gtfobins.github.io)

You can also run:  
`wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh` on a target machine to see the files that stand out.

Another option would be to run the following command to find all files with the SUID bit set:  
`find / -user root -perm 4000 -print 2>/dev/null` good  
`find / -user root -perm 4000 -exec ls -ldb {} \; 2>/dev/null` better  
`find / -user root -perm 4000 -exec ls -ldb {} \; 2>/dev/null | grep 'bin'` best  

`2>/dev/null` will filter out the errors so that they will not be output to your console

### Find info about the users of the system
Find users on a system  
`cat /etc/passwd | grep “/bin/bash”`

Find passwords  
`cat /etc/passwd`

If you don't have privilege, try this  
`find / -name shadow* 2>/dev/null | head`

### Privilege Escalation using SUID Binaries
`-rwsr-xr-x`  
“s” = SUID. This means that any user can execute these commands and they will be ran as the original owner.

**Example**  
Lets say the `cat` command had the 's' in its SUID. Then you would be able to use something like the following command:  
`find /home/berkan/flag1.txt -exec cat {} \;`

## Phishing

### Phishing terms
**A BEC (Business Email Compromise)** is when an adversary gains control of an internal employee's account and then uses the compromised email account to convince other internal employees to perform unauthorized or fraudulent actions. 

**A typosquatting attack**, also known as a URL hijacking, a sting site, or a fake URL, is a type of social engineering where threat actors impersonate legitimate domains for malicious purposes such as fraud or malware spreading.

### Types of Phishing attacks
**Spam** - unsolicited junk emails sent out in bulk to a large number of recipients. The more malicious variant of Spam is known as MalSpam.

**Phishing** -  emails sent to a target(s) purporting to be from a trusted entity to lure individuals into providing sensitive information. 

**Spear phishing** - takes phishing a step further by targeting a specific individual(s) or organization seeking sensitive information.  

**Whaling** - is similar to spear phishing, but it's targeted specifically to C-Level high-position individuals (CEO, CFO, etc.), and the objective is the same. 

**Smishing** - takes phishing to mobile devices by targeting mobile users with specially crafted text messages. 

**Vishing** - is similar to smishing, but instead of using text messages for the social engineering attack, the attacks are based on voice calls. 

### Analyze/identify
1. Open Email
2. See its raw format
3. Analyze the results:

* **X-Originating-IP** - The IP address of the email was sent from (this is known as an X-header)
* **Smtp.mailfrom/header.from** - The domain the email was sent from (these headers are within Authentication-Results)
* **Reply-To** - This is the email address a reply email will be sent to instead of the From email address

In case the mail is encoded using base64, the following command can be used to decrypt the message:  
`base64 -d <filename> > decrypted.<filetype>` 

### Phishing security
Hyperlinks and IP addresses should be [defanged](https://www.ibm.com/docs/en/rsoa-and-rp/32.0?topic=SSBRUQ_32.0.0/com.ibm.resilient.doc/install/resilient_install_defangURLs.htm).

Expand shortened links with this [tool](https://www.expandurl.net).

# Forensics
Is simply 'the art of uncovering'

Digital forensics is a branch of forensic science that focuses on identifying, acquiring, processing, analysing, and reporting on data stored electronically.

Use case  
* Find hidden information in files or meta data
* Recover lost or deleted data
* Reconstruct corrupted files
* Recognize file structures and identify file formats
* Understand a course of events from network logs or memory dumps
* Hash cracking 

## File analysis
### Encodings
* Decimal: 70 111 114 101 110 115 105 99 115 33
* Hex: 46 6f 72 65 6e 73 69 63 73 21
* Octal: 106 157 162 145 156 163 151 143 163 41
* ASCII: Forensics!
* Base64: Rm9yZW5zaWNzIQ==
* Base85: 7W3<YDKBN%F!1

### File type
The file type is often indicated by the file extension in the file name, e.g. .png, .mp4
* Typically what the OS uses to assess how to open / interpret the file
* Do not rely on extensions! Can be modified to trick the OS into misinterpreting data

The file type is indicated in the contents of the file with a file signature - a magic number
* Hex string at a specific offset
* Eg PNG files: 89 50 4e 47 (last three hex is PNG in ASCII)
* Tool: `file`

### Metadata
The file extension is one form of metadata: (data about data)

Additional information about a file in addition to the content itself
* General: File name, extension, size, time of origin, permissions
* Specific: GPS data in images, number of frames in GIF, CPU architecture in executables, etc.

Why analyze metadata?
* Can store important info - maybe even info that should have been hidden
* In some cases even more important than content - eg with encrypted HTTPS traffic
* Tool: `exiftool` 

### File format
A file type has a specific format - the structure of the file

Typical structure
* Signature file - magic number

Header - typical info to be used to understand the content (metadata)
* Possibly meta data
* Data
* Trailer that completes the file

The format is precisely defined in a specification doc - often publicly available
* Corrupted files: compare file with specification, correct differences with hex editor
* Unknown file types: search for tracks from a file format 

## Steganography
Steganography is the practice of hiding a secret message in something that is not secret

**File Carving**  
File carving: extract files based on the file format
* Look for file signatures, headers, trailers, etc.
* Originally used in connection with. extraction of files from disk images and memory dumps
* Useful for extracting files stored in other files in stego challenges

File carving tools:
* binwalk
* foremost
* dd (manual extraction)
  * dd if = input.png or = output.txt bs = 1 skip = 1000 count = 32 

### Steghide
Steghide is a steganography program that hides data in various kinds of image and audio files ,
only supports these file formats : JPEG, BMP, WAV and AU . but it’s also useful for extracting
embedded and encrypted data from other files.

**Useful commands:**  
`steghide info file`  displays info about a file whether it has embedded data or not.  
`steghide extract -sf file`  extracts embedded data from a file

### Stegsolve
Sometimes there is a message or a text hidden in the image itself and in order to view it you
need to apply some color filters or play with the color levels. You can do it with GIMP or
Photoshop or any other image editing software but stegsolve made it easier. it’s a small java tool
that applies many color filters on images.

### Strings
Strings is a linux tool that displays printable strings in a file. That simple tool can be very helpful when solving stego challenges. Usually the embedded data is password protected or encrypted
and sometimes the password is actaully in the file itself and can be easily viewed by using strings.
It’s a default linux tool so you don’t need to install anything.

**Useful commands:**  
`strings file`  displays printable strings in the given file

### Exiftool
Sometimes important stuff is hidden in the metadata of the image or the file , exiftool can be
very helpful to view the metadata of the files.

**Useful commands:**  
`exiftool file`  shows the metadata of the given file

### Exiv2
A tool similar to exiftool.

**Useful commands:**  
`exiv2 file` shows the metadata of the given file  

### Binwalk
Binwalk is a tool for searching binary files like images and audio files for embedded files and
data.

**Useful commands:**  
`binwalk file` Displays the embedded data in the given file  
`binwalk -e file` Displays and extracts the data from the given file

### Zsteg
zsteg is a tool that can detect hidden data in png and bmp files.

**Useful commands:**  
`zsteg -a file` Runs all the methods on the given file  
`zsteg -E file` Extracts data from the given payload (example : zsteg -E b4,bgr,msb,xy
name.png)

### Wavsteg
WavSteg is a python3 tool that can hide data and files in wav files and can also extract data from
wav files.

**Useful commands:**  
`python3 WavSteg.py -r -s soundfile -o outputfile` extracts data from a wav sound file and
outputs the data into a new file

### Sonic visualizer
Sonic visualizer is a tool for viewing and analyzing the contents of audio files, however it can be
helpful when dealing with audio steganography. You can reveal hidden shapes in audio files.

## Memory analysis
Traditionel computer forensics can be made out of volatile memory.

What is volatile data?
* Volatile data: non-permanent data, disappears when the power goes out
* Typically the contents of main memory RAM
* "Live box forensics"
* Analysis takes place on a memory dump - provides a snapshot 

Data that can be found in volatile memory
* Running processes and services
* Open files
* Network connections
* Run commands
* Passwords, keys
* Unencrypted data that is encrypted on disk but must be used in decrypted mode in memory
* Stateless malware - malware that lives only in memory
* Even things like a basic screenshot or the user's clipboard 

A tool used for analyzing memory dumps is [volatility 3](https://github.com/volatilityfoundation/volatility3).

# Cryptology
Cryptography in Cryptology is used to protect confidentiality, ensure integrity, ensure authenticity.

## Generate keys
To generate a private key we use the following command (8912 creates the key 8912 bits long):  
`openssl genrsa -aes256 -out private.key 8912`

To generate a public key we use our previously generated private key:  
`openssl rsa -in private.key -pubout -out public.key`

Lets now encrypt a file (plaintext.txt) using our public key:  
`openssl rsautl -encrypt -pubin -inkey public.key -in plaintext.txt -out encrypted.txt`

Now, if we use our private key, we can decrypt the file and get the original message:  
`openssl rsautl -decrypt -inkey private.key -in encrypted.txt -out plaintext.txt`


# Networking
`TO BE ADDED`

# Vulnerabilities
## SQL Injection
`TO BE ADDED`

## XSS (Cross-Site Scripting)
**DOM-Based XSS**: This is when an attack payload is executed by manipulating the DOM (Document Object Model) in the target's browser. This type uses the client-side code instead of server-side code.

**Reflected XSS**: This is when a malicious script bounces off another website onto the target's web application or website. Normally, these are passed in the URL as a query, and it's easy as making the target click a link. This type originates from the target's request.

**Stored XSS**: This is when a malicious script is directly injected into the webpage or web application. This type originates from the website's database.

## Printer Hacking (IPP)
Enumeration and exploitation tools can be found [here](https://github.com/RUB-NDS/PRET)  
Printer security cheat sheet can be found [here](http://hacking-printers.net/wiki/index.php/Printer_Security_Testing_Cheat_Sheet)

It allows clients to submit one or more print jobs to the printer or print server, and perform tasks such as querying the status of a printer, obtaining the status of print jobs, or canceling individual print jobs."  
Most of them appear to run the CUPS server (which is a simple UNIX printing system).  

Running `python pret.py` will start an automatic printer discovery in your local network. 