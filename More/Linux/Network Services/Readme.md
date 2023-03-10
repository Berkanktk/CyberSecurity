# Network Services

## SSH
Secure Shell (SSH) is a network protocol that allows the secure transmission of data and commands over a network.

The most commonly used SSH server is the OpenSSH server. It is available for most Linux distributions and can be installed with the following command:
```console
berkankutuk@kali:~$ sudo apt install openssh-server
```

To check if the server is running, we can use the following command:

```console
berkankutuk@kali:~$ sudo systemctl status ssh
```

OpenSSH can be configured and customized by editing the file /etc/ssh/sshd_config with a text editor. Here we can adjust settings such as the maximum number of concurrent connections, the use of passwords or keys for logins, host key checking, and more. 

## NFS
Network File System (NFS) is a network protocol that allows us to store and manage files on remote systems as if they were stored on the local system. It enables easy and efficient management of files across networks. For example, administrators use NFS to store and manage files centrally (for Linux and Windows systems) to enable easy collaboration and management of data. For Linux, there are several NFS servers, including NFS-UTILS (Ubuntu), NFS-Ganesha (Solaris), and OpenNFS (Redhat Linux).

It can also be used to share and manage resources efficiently, e.g., to replicate file systems between servers. It also offers features such as access controls, real-time file transfer, and support for multiple users accessing data simultaneously. We can use this service just like FTP in case there is no FTP client installed on the target system, or NFS is running instead of FTP.

We can install NFS on Linux with the following command:

```console
berkankutuk@kali:~$ sudo apt install nfs-kernel-server -y
```

To check if the server is running, we can use the following command:

```console
berkankutuk@kali:~$ sudo systemctl status nfs-kernel-server
```

We can configure NFS via the configuration file /etc/exports. This file specifies which directories should be shared and the access rights for users and systems. It is also possible to configure settings such as the transfer speed and the use of encryption. NFS access rights determine which users and systems can access the shared directories and what actions they can perform. Here are some important access rights that can be configured in NFS:

| Permissions    | Description                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| rw             | Gives users and systems read and write permissions to the shared directory.                                                                                |
| ro             | Gives users and systems read-only access to the shared directory.                                                                                          |
| no_root_squash | Prevents the root user on the client from being restricted to the rights of a normal user.                                                                 |
| root_squash    | Restricts the rights of the root user on the client to the rights of a normal user.                                                                        |
| sync           | Synchronizes the transfer of data to ensure that changes are only transferred after they have been saved on the file system.                               |
| async          | Transfers data asynchronously, which makes the transfer faster, but may cause inconsistencies in the file system if changes have not been fully committed. |
| async          | Transfers data asynchronously, which makes the transfer faster, but may cause inconsistencies in the file system if changes have not been fully committed. |

### Create NFS Share

To create an NFS share, we need to create a directory that we want to share. We can do this with the following command:

```console  
berkankutuk@kali:~$ mkdir nfs_sharing
berkankutuk@kali:~$ echo '/home/berkankutuk/nfs_sharing hostname(rw,sync,no_root_squash)' >> /etc/exports
berkankutuk@kali:~$ cat /etc/exports | grep -v "#"
```

If we have created an NFS share and want to work with it on the target system, we have to mount it first. We can do this with the following command:


```console
berkankutuk@kali:~$ mkdir ~/target_nfs
berkankutuk@kali:~$ mount 10.129.12.17:/home/john/dev_scripts ~/target_nfs
berkankutuk@kali:~$ tree ~/target_nfs
```

So we have mounted the NFS share (dev_scripts) from our target (10.129.12.17) locally to our system in the mount point target_nfs over the network and can view the contents just as if we were on the target system. There are even some methods that can be used in specific cases to escalate our privileges on the remote system using NFS.

## Web Server
Apache web server has a variety of features that allow us to host a secure and efficient web application. Moreover, we can also configure logging to get information about the traffic on our server, which helps us analyze attacks. We can install Apache using the following command:

To install Apache on Kali Linux, we can use the following command:

```console
berkankutuk@kali:~$ sudo apt install apache2 -y
```

For Apache2, to specify which folders can be accessed, we can edit the file /etc/apache2/apache2.conf with a text editor. This file contains the global settings. We can change the settings to specify which directories can be accessed and what actions can be performed on those directories.

### Apache2 Configuration

```xml
<Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
</directory>
```

This section specifies that the default `/var/www/html` folder is accessible, that users can use the `Indexes` and `FollowSymLinks` options, that changes to files in this directory can be overridden with `AllowOverride` `All`, and that Require all granted grants all users access to this directory. 

For example, if we want to transfer files to one of our target systems using a web server, we can put the appropriate files in the /var/www/html folder and use wget or curl or other applications to download these files on the target system.

It is also possible to customize individual settings at the directory level by using the .htaccess file, which we can create in the directory in question. This file allows us to configure certain directory-level settings, such as access controls, without having to customize the Apache configuration file. We can also add modules to get features like mod_rewrite, mod_security, and mod_ssl that help us improve the security of our web application.


## Python Web Server
Python comes with a built-in web server that we can use to host a web application. We can start the web server with the following command:

```console
berkankutuk@kali:~$ python3 -m http.server 8000
```

We can also host our Python web server on a port other than the default port by using the -p option:
    
```console
berkankutuk@kali:~$ python3 -m http.server -p 443
```

This will host our Python web server on port 443 instead of the default TCP/8000 port. We can access this web server by typing the link in our browser.

## VPN
A virtual private network (VPN) is a network that uses a public network (usually the Internet) to connect remote sites or users together. It allows us to securely connect to a private network and access resources. It is used to extend a private network across a public network, and it enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network.

Some of the most popular VPN servers for Linux servers are OpenVPN, L2TP/IPsec, PPTP, SSTP, and SoftEther. 

OpenVPN can also be used by us as a penetration tester to connect to internal networks. It can happen that a VPN access is created by the customer so that we can test the internal network for security vulnerabilities. This is an alternative for cases when the penetration tester is too far away from the customer. OpenVPN provides us with a variety of features, including encryption, tunneling, traffic shaping, network routing, and the ability to adapt to dynamically changing networks. We can install the server and client with the following command:

```console
berkankutuk@kali:~$ sudo apt install openvpn -y
```

OpenVPN can be customized and configured by editing the configuration file /etc/openvpn/server.conf. This file contains the settings for the OpenVPN server. We can change the settings to configure certain features such as encryption, tunneling, traffic shaping, etc.

If we want to connect to an OpenVPN server, we can use the .ovpn file we received from the server and save it on our system. We can do this with the following command on the command line:

```console
berkankutuk@kali:~$ sudo openvpn --config client.ovpn
```
