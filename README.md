# To be added

# List of contents
1. [Concepts](#concepts)
2. [Links](#links)
3. [Tools](#tools-for-pentesting-in-general)
4. [Linux Commands](#linux-commands)
5. [Steps](#steps)

# Concepts
## Hashing
plaintext ➡️ hash  
hash ⛔ plaintext
## Encryption

### Symetric encryption
plaintext ➡️ 🔑 ➡️ ciphertext  
plaintext ⬅️ 🔑 ⬅️ ciphertext  
(🔑 shared key)

### Asymetric encryption
plaintext ➡️ 🔑 ➡️ ciphertext  
plaintext ⬅️ 〽️ ⬅️ ciphertext  
(🔑 public key, 〽️ private key

# Links
[ExploitDB](https://www.exploit-db.com) - searchable archive from The Exploit Database.  
[CVE Mitre](https://cve.mitre.org) - list of publicly known cybersecurity vulnerabilities.

# Tools (For pentesting in general)
[Aircrack-ng](https://www.aircrack-ng.org) - is a complete suite of tools to assess WiFi network security  
[Burp Suite](https://portswigger.net/burp) - is a tool for testing web app security, intercepting proxy to replay, inject, scan and fuzz.  
[Gobuster](https://github.com/OJ/gobuster) - is a free and open source directory/file & DNS busting tool written in Go.  
[Hashcat](https://hashcat.net/hashcat/) - is world's fastest and most advanced password recovery utility.  
[Hydra](https://github.com/vanhauser-thc/thc-hydra) - is a parallelized login cracker which supports numerous protocols to attack  
[John The Ripper](https://www.openwall.com/john/) - is a fast password cracker, currently available for many flavors of Unix, Windows, and other.  
[Metasploit](https://www.metasploit.com) - is a tool and framework for pentesting system, web and many more, contains a lot a ready to use exploits.  
[Nano](https://nano-editor.org) - is an easy to use command line text editor  
[Netcat](http://netcat.sourceforge.net) - is an utility which reads and writes data across network connections, using the TCP/IP protocol.  
[Nikto 2](https://cirt.net/Nikto2) - is a web server scanner which performs comprehensive tests against web servers for multiple items.  
[Nmap](https://nmap.org) - is a free and open source (license) utility for network discovery and security auditing.  
[Vim](https://www.vim.org) - is a highly configurable text editor.  
[Wireshark](https://www.wireshark.org) - is the world’s foremost and widely-used network protocol analyzer.  

## Aircrack-ng
## Burp
## Gobuster## Hashcat## Hydra## Johntheripper
## Metasploit
## Nano
## Netcat
## Nikto
## Nmap
### Syntax
`nmap -switch1 -switch2 ipaddress`  

Example:  
`nmap -sT -A 172.162.39.86`  

### A list of most useful switches:
TCP scan (Most likely to be filtered)= `-sT`  
Syn Scan (No logging)= `-sS`  
UDP scan (Slow)= `-sU`  

ICMP Scanning (ping sweep) = `-sn`  
Default ping scanning) = `-sP` 
Detect OS = `-O`  
Detect version of services = `-sV`  
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
## Vim
## Wireshark

# Linux Commands 
## ps
## top
## kill
## find
## diff
## tail
## pwd
## chmod
## curl
## apt
## dig
## perl
## grep

# Steps
