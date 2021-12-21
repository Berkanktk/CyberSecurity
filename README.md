# To be added

# List of contents
1. [Concepts](#concepts)
2. [Links](#links)
3. [Overview of tools](#overview-of-tools-for-pentesting-in-general)
4. [Tools (CLI)](#tools-cli)
5. [Tools (GUI)](#tools-gui)
6. [Linux Commands](#linux-commands)
7. [Steps](#steps)

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

# Overview of Tools (For pentesting in general)
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

# Tools (CLI)
## Aircrack-ng
https://cheatography.com/itnetsec/cheat-sheets/aircrack-ng-suite/
## Gobuster
### Syntax
`gobuster -w wordlist.txt`

### Example:  
`gobuster dir -u http://172.162.39.86 -w /usr/share/wordlists/dirb/megalist.txt` 

### A list of most useful options:
`-u` (url) – full URL (including scheme), or base domain name.  
`-w` (wordlist) – path to the wordlist used for brute forcing (use – for stdin).  
`-a` (user agent string) – specify a user agent string to send in the request header.  
`-o` (file) – specify a file name to write the output to.  
`-x` (extensions) – list of extensions to check for, if any.  
`-P` (password) – HTTP Authorization password (Basic Auth only, prompted if missing).  
`-U` (username) – HTTP Authorization username (Basic Auth only).  

## Hashcat
## Hydra
### Syntax  
`hydra -options path`  

**Example**
`hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.46.127 http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid" -V`

### Examples:  
Guess SSH credentials using a given username and a list of passwords:  
`hydra -l username -P path/to/wordlist.txt host_ip ssh`

Guess Telnet credentials using a list of usernames and a single password, specifying a non-standard port and IPv6: 
`hydra -L path/to/usernames.txt -p password -s port -6 host_ip telnet`

Guess FTP credentials using usernames and passwords lists, specifying the number of threads:  
`hydra -L path/to/usernames.txt -P path/to/wordlist.txt -t n_tasks host_ip ftp` 

Guess MySQL credentials using a username and a passwords list, exiting when a username/password pair is found:  
`hydra -l username -P path/to/wordlist.txt -f host_ip mysql`

Guess IMAP credentials on a range of hosts using a list of colon-separated username/password pairs:  
`hydra -C path/to/username_password_pairs.txt imap://[host_range_cidr]`

Guess POP3 credentials on a list of hosts using usernames and passwords lists, exiting when a username/password pair is found:
`hydra -L path/to/usernames.txt -P path/to/wordlist.txt -M path/to/hosts.txt -F pop3`

### A list of most useful options:
`-S` connect via SSL  
`-l` LOGIN or `-L` FILE login with LOGIN name, or load several logins from FILE  
`-p` PASS or `-P` FILE try password PASS, or load several passwords from FILE  
`-u` by default Hydra checks all passwords for one login and then tries the next login. This option loops around the passwords, so the first password is tried on all logins, then the next password.  
`-o` FILE
write found login/password pairs to FILE instead of stdout
## John The Ripper
## Metasploit
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
## Netcat
https://www.comparitech.com/net-admin/netcat-cheat-sheet/
## Nikto 2 
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
https://cheatography.com/typo209/cheat-sheets/comprehensive-vim-cheat-sheet/

# Tools (GUI) 
## Burp
https://twitter.com/Pethuraj/status/1399408069377880064/photo/1
## Wireshark
https://packetlife.net/media/library/13/Wireshark_Display_Filters.pdf

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
