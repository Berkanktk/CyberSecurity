# Samba enumeration
Samba is the standard Windows interoperability suite of programs for Linux and Unix. It allows end users to access and use files, printers and other commonly shared resources on a companies intranet or internet. Its often referred to as a network file system.

# Enumeration with nmap
Using nmap we can enumerate a machine for SMB shares.
```bash
berkankutuk@kali:~$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>

# or try this
berkankutuk@kali:~$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>
```

You can also use nmap to grab the banner of the SMB service. 

```bash
berkankutuk@kali:~$ nmap -sV --script=banner -p<port> <ip>/24
```

Or even create a SMB report.
```bash
berkankutuk@kali:~$ nmap --script smb-os-discovery.nse -p<port> <ip>
```

# SMBClient

List available SMB shares

```bash
berkankutuk@kali:~$ smbclient -N -L \\\\<ip>
```

> The -L flag specifies that we want to retrieve a list of available shares on the remote host, while -N suppresses the password prompt.

Connect to one of the shares.
```bash
berkankutuk@kali:~$ smbclient //<ip>/<share>
```

> You will be asked for a password, the easiest password is no password! We can just press "Enter" to test this theory

You can recursively download the SMB share too. Submit the username and password as nothing.

```bash
berkankutuk@kali:~$ smbget -R smb://<ip>/<share>
```

# Enum4linux
[Enum4linux](https://www.kali.org/tools/enum4linux/) is a tool for enumerating information from Windows and Samba systems. 

1. Run enum4linux and list all the possible options we could use, take time to study these for anything interesting: `./enum4linux.pl -h`
2. Note how we can use options like `-S` to list shares or `-U` (note the uppercase) to list possible users.
3. Access the server through Samba: `./enum4linux.pl -S <ip>`

# When you have access to a share
| Command | Description |
| --- | --- |
| ls | List files and directories in the current location |
| cd <directory> | Change our working directory |
| pwd | Output the full path to our working directory |
| more <filename> | Find out more about the contents of a file. To close the open file, you press :q |
| get <filename> | Download a file from a share |
| put <filename> | Upload a file from a share |