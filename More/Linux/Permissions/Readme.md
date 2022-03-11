# Linux Permission Management

## Overview
The whole permission system on Linux systems is based on the octal number system, and basically, there are three different types of permissions a file or directory can be assigned:

(`r`) - Read   
(`w`) - Write  
(`x`) - Execute  

```bash
berkankutuk@kali$ ls -l /etc/passwd

- rwx rw- r--   1 root root 1641 May  4 23:42 /etc/passwd
- --- --- ---   |  |    |    |   |__________|
|  |   |   |    |  |    |    |        |_ Date
|  |   |   |    |  |    |    |__________ File Size
|  |   |   |    |  |    |_______________ Group
|  |   |   |    |  |____________________ User
|  |   |   |    |_______________________ Number of hard links
|  |   |   |_ Permission of others (read)
|  |   |_____ Permissions of the group (read, write)
|  |_________ Permissions of the owner (read, write, execute)
|____________ File type (- = File, d = Directory, l = Link, ... )
```

## Change Permissions
We can modify permissions using the `chmod` command, permission group references (`u` - owner, `g` - Group, `o` - others, `a` - All users), and either a [+] or a [-] to add remove the designated permissions. In the following example, a user creates a new shell script owned by that user, not executable, and set with read/write permissions for all users.

Representations
```
Binary Notation:                4 2 1  |  4 2 1  |  4 2 1
----------------------------------------------------------
Binary Representation:          1 1 1  |  1 0 1  |  1 0 0
----------------------------------------------------------
Octal Value:                      7    |    5    |    4
----------------------------------------------------------
Permission Representation:      r w x  |  r - x  |  r - -
```

## Change Owner
To change the owner and/or the group assignments of a file or directory, we can use the `chown` command. The syntax is like following:  
`chown <user>:<group> <file/directory>`

## SUID & GUID
Besides assigning direct user and group permissions, we can also configure special permissions for files by setting the Set User ID (SUID) and Set Group ID (GUID) bits. These SUID/GUID bits allow, for example, users to run programs with the rights of another user. Administrators often use this to give their users special rights for certain applications or files. The letter "s" is used instead of an "x". When executing such a program, the SUID/GUID of the file owner is used.

It is often the case that administrators are not familiar with the applications but still assign the SUID/GUID bits, which leads to a high-security risk. Such programs may contain functions that allow the execution of a shell from the pager, such as the application "journalctl."

If the administrator sets the SUID bit to "journalctl," any user with access to this application could execute a shell as root.
