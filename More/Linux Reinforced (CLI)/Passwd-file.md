# The passwd file explained
The /etc/passwd file stores essential information required during login. In other words, it stores user account information. The /etc/passwd is a plain text file. It contains a list of the system’s accounts, giving for each account some useful information like user ID, group ID, home directory, shell, and more. The /etc/passwd file should have general read permission as many command utilities use it to map user IDs to user names. However, write access to the /etc/passwd must only limit for the superuser/root account.

## Understanding /etc/passwd file fields
The /etc/passwd contains one entry per line for each user (user account) of the system. All fields are separated by a colon (`:`) symbol. Total of seven fields as follows. Generally, /etc/passwd file entry looks as follows:

![Fields](/Images/Passwd.png)

/etc/passwd file format
From the above image:

1. `Username`: It is used when user logs in. It should be between 1 and 32 characters in length.
2. `Password`: An x character indicates that encrypted password is stored in /etc/shadow file. Please note that you need to use the passwd command to computes the hash of a password typed at the CLI or to store/update the hash of the password in /etc/shadow file.
3. `User ID (UID)`: Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.
4. `Group ID (GID)`: The primary group ID (stored in /etc/group file)
5. `User ID Info (GECOS)`: The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.
6. `Home directory`: The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /
7. ` Command/shell`: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell. For example, sysadmin can use the nologin shell, which acts as a replacement shell for the user accounts. If shell set to /sbin/nologin and the user tries to log in to the Linux system directly, the /sbin/nologin shell closes the connection.