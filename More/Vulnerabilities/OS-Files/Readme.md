# Common OS files

| Location | Description |
|:---:|:---:|
| /etc/issue | contains a message or system identification to be printed before the login prompt. |
| /etc/profile | controls system-wide default variables, such as Export variables, File creation mask (umask), Terminal types, Mail messages to indicate when new mail has arrived |
| /proc/version | specifies the version of the Linux kernel |
| /proc/[0-9]*/fd/[0-9]*  | contains file descriptors for all processes (first number is the PID, second is the filedescriptor) |
| /proc/self/environ | contains the environment variables for the current process |
| /proc/cmdline | contains the kernel boot parameters |
| /etc/group | contains all the groups that are available on the system |
| /etc/hosts | contains the IP address to hostname mappings |
| /etc/passwd | has all registered user that has access to a system |
| /etc/shadow | contains information about the system's users' passwords |
| /etc/motd | contains the message of the day, which is displayed to all users after logging in |
| /etc/mysql/my.cnf | contains the MySQL database configuration file |
| /root/.bash_history | contains the history commands for root user |
| /var/log/dmessage | contains global system messages, including the messages that are logged during system startup |
| /var/mail/root | all emails for root user |
| /root/.ssh/id_rsa | Private SSH keys for a root or any known valid user on the server |
| /var/log/apache2/access.log | the accessed requests for Apache  webserver |
| C:\boot.ini | contains the boot options for computers with BIOS firmware |