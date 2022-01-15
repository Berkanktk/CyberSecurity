# List of contents
1. [Concepts](#concepts)
   1. [Hashing](#hashing)
   2. [Encryption](#encryption)
2. [Links](#links)
3. [Overview of tools](#overview-of-tools-for-pentesting-in-general)
4. [Tools (CLI)](#tools-cli)
5. [Tools (GUI)](#tools-gui)
6. [Linux Commands](#linux-commands)
7. [Steps](#steps)
   1. [Privilege Escalation](#privilege-escalation)
   2. [Phishing](#phishing)
   3. [Steganography](#steganography)

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
[The Ripper](https://www.openwall.com/john/) - is a fast password cracker, currently available for many flavors of Unix, Windows, and other.  
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
`-f` Suppresses all warnings prompts
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