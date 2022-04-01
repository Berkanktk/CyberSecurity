# Samba enumeration
Samba is the standard Windows interoperability suite of programs for Linux and Unix. It allows end users to access and use files, printers and other commonly shared resources on a companies intranet or internet. Its often referred to as a network file system.

# How to 
Using nmap we can enumerate a machine for SMB shares.

Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares!

`nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>`

Inspect one of the shares.

`smbclient //<ip>/<share>`

You can recursively download the SMB share too. Submit the username and password as nothing.

`smbget -R smb://<ip>/<share>`

Enumerate ports

`nmap -p <port> --script=nfs-ls,nfs-statfs,nfs-showmount <ip>`