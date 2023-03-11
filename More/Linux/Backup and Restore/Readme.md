# Backup and Restore
Linux systems offer a variety of software tools for backing up and restoring data, some of them being:

* Rsync
* Deja Dup
* Duplicity

##  Rsync
Rsync is an open-source tool that allows us to quickly and securely back up files and folders to a remote location. It is particularly useful for transferring large amounts of data over the network, as it only transmits the changed parts of a file. It can also be used to create backups locally or on remote servers. If we need to back up large amounts of data over the network, Rsync might be the better option.

Installing Rsync is as simple as running the following command:

```console
berkankutuk@kali:~$ sudo apt install rsync -y
```

To back up a file or folder, we can use the following command:

```console
berkankutuk@kali:~$ rsync -av /path/to/mydirectory user@backup_server:/path/to/backup/directory
```
 The option archive (-a) is used to preserve the original file attributes, such as permissions, timestamps, etc., and using the verbose (-v) option provides a detailed output of the progress of the rsync operation.

To restore a file or folder, we can use the following command:

```console
berkankutuk@kali:~$ rsync -av user@remote_host:/path/to/backup/directory /path/to/mydirectory
```

To ensure the security of our rsync file transfer between our local host and our backup server, we can combine the use of SSH and other security measures.


### Encrypting Rsync Transfers
```console
berkankutuk@kali:~$ rsync -avz -e ssh /path/to/mydirectory user@backup_server:/path/to/backup/directory
```

### Auto Syncing
To enable auto-synchronization using rsync, you can use a combination of cron and rsync to automate the synchronization process.

```bash
#!/bin/bash

rsync -avz -e ssh /path/to/mydirectory user@backup_server:/path/to/backup/directory
```

Then, in order to ensure that the script is able to execute properly, we must provide the necessary permissions.

```console
berkankutuk@kali:~$ chmod +x /path/to/script.sh
```

Finally, we can add the script to the crontab file to run it at a specified time interval.

```bash
0 * * * * /path/to/script.sh
```

## Duplicity
Duplicity is another graphical backup tool for Ubuntu that provides users with comprehensive data protection and secure backups. It also uses Rsync as a backend and additionally offers the possibility to encrypt backup copies and store them on remote storage media, such as FTP servers, or cloud storage services, such as Amazon S3.

## Deja Dup
Deja Dup is a graphical backup tool for Ubuntu that simplifies the backup process, allowing us to quickly and easily back up our data. It provides a user-friendly interface to create backup copies of data on local or remote storage media. It uses Rsync as a backend and also supports data encryption.