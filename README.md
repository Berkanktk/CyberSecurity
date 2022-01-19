# List of contents
1. [Concepts](#concepts)
   1. [Hashing](#hashing)
   2. [Encryption](#encryption)
2. [Links](#links)
3. [Services](#services)
4. [Terms](#terms)
5. [Overview of tools](#overview-of-tools-for-pentesting-in-general)
6. [Tools (CLI)](#tools-cli)
   1. [Aircrack-ng](#aircrack-ng)
   2. [Gobuster](#gobuster)
   3. [Hashcat](#hashcat)
   4. [Hydra](#hydra)
   5. [John The Ripper](#john-the-ripper)
   6. [Metasploit](#metasploit)
   7. [Netcat](#netcat)
   8. [Nikto](#nikto-2)
   9.  [Nmap](#nmap)
7. [Tools (GUI)](#tools-gui)
   1. [Burp Suite](#burp)
   2. [Wireshark](#wireshark)
8. [Text Editors](#text-editors)
   1.  [Nano](#nano)
   2.  [VIM](#vim)
9. [Linux Commands](#linux-commands)
10. [Steps](#steps)
    1. [Privilege Escalation](#privilege-escalation)
    2. [Phishing](#phishing)
    3. [Steganography](#steganography)
11. [Networking](#networking) 

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
[GTFOBins](https://gtfobins.github.io) - list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.

# Services
## Active directory (Windows)
Active Directory is a collection of machines and servers connected inside of domains, that are a collective part of a bigger forest of domains, that make up the Active Directory network. 

Other related terms include: Domain controllers, Trusts & Policies, Services, Authentication & Cloud security.

# Terms
**Active reconnaissance** - Directly interacting with the system.  
**Passive reconnaissance** - We rely on publicly available information.   
**IDOR** - IDOR stands for Insecure Direct Object Reference and is a type of access control vulnerability.  

# Overview of Tools (For pentesting in general)
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
### SSH Private Key
Hash the private key  
`/root/Tools/'Password Attacks'/john/ssh2john.py id_rsa > hash`

Crack the hash  
`john hash --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.txt`
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

## Nessus

## Netcat
Netcat aka nc is an extremely versatile tool. It allows users to connect to specific ports and send and receive data. It also allows machines to receive data and connections on specific ports, which makes nc a very popular tool to gain a Reverse Shell.

### Syntax
Computer B (acts as the receiving server):  
`nc -l -p 6790 > testfile.txt`  
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

# Tools (GUI) 
## Burp
https://twitter.com/Pethuraj/status/1399408069377880064/photo/1  
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
https://cheatography.com/typo209/cheat-sheets/comprehensive-vim-cheat-sheet/

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
Search for files
`find -name passwords.txt`

Find any file with the extension of ".txt"
`find -name *.txt`
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
| 1  |  That file can be executed |
| 2  |    That file can be written to   | 
| 3  | That file can be executed and written to |
| 4  | That file can be read |
| 5  | That file can be read and executed |
| 6  | That file can be written to and read |
| 7  | That file can be read, written to, and executed |
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
`-x`Specify IP adress
`+noall +answer` dDtailed information

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

`wc -l file.txt` get numbers of entries

`grep "81.143.211.90" file.txt`

Flags:
`-n` line numbers for every string found? 
## whoami
Find out what user we're currently logged in as
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
Sudo is Linux's run as administrator button

Flags:  
`-u <user>` specify user   
`-l` list current sudo priviliges   
## adduser & addgroup
The syntax for both of these commands are `adduser username` and `addgroup groupname`.

Add a user to a group  
`usermod -a -G <groups seperated by commas> <user>`
## Operators
`>` is the operator for output redirection. Meaning that you can redirect the output of any command to a file  
`>>` does mainly the same thing as >, with one key difference. >> appends the output of a command to a file, instead of erasing it.


# Steps
## Privilege Escalation 
Check for root password
Run: `id`  
Run: `sudo -l`  
Locate password folder and crack it using johntheripper  
Or use [GTFOBins](https://gtfobins.github.io)

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


## Steganography
## SQL Injection

# Networking