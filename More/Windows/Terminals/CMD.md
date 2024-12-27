# Windows Command Prompt

The default command prompt in Windows is `cmd.exe`. It is a command-line interpreter that allows you to interact with the operating system. This document covers the basics of using the Windows Command Prompt.

## Basic System Information
* `systeminfo`: Displays detailed configuration information about the computer and its operating system.
* `hostname`: Displays the name of the host.
* `tasklist`: Lists all running processes on the system.
* `driverquery`: Lists all installed drivers.
* `ver`: Displays the Windows version.
* `set`: Displays all environment variables.
* `cls`: Clears the screen.

## Network Troubleshooting
* `ping`: Sends ICMP echo requests to a host.
* `tracert`: Traces the route to a destination.
* `nslookup`: Queries DNS servers for information about domain names and IP addresses.
* `netstat`: Displays active network connections.
* `arp`: Displays and modifies the IP-to-Physical address translation tables used by address resolution protocol (ARP).
* `ipconfig`: Displays the IP configuration for all network adapters. Use `/all` for detailed information.

**Netstat Flags:**
* `-a`: Displays all connections and listening ports.
* `-b`: Displays the executable involved in creating each connection or listening port.
* `-o`: Displays the owning process ID associated with each connection.
* `-n`: Displays addresses and port numbers in numerical form.

## File and Disk Management
* `dir`: Lists the contents of a directory.
* `cd`: Changes the current directory.
* `copy`: Copies files.
* `move`: Moves files.
* `del`: Deletes files.
* `md`: Creates a new directory.
* `rd`: Removes a directory.
* `chkdsk`: Checks a disk and displays a status report.
* `xcopy`: Copies files and directory trees.
* `attrib`: Displays or changes file attributes.
* `find`: Searches for a text string in files.
* `more`: Displays output one screen at a time.
* `tree`: Graphically displays the directory structure of a drive or path.
* `type`: Displays the contents of a text file.
* `where`: Displays the location of files that match a search pattern.

## Task and Process Management
* `tasklist`: Lists all running processes.
* `taskkill`: Terminates a process.
* `start`: Starts a separate window to run a specified program or command.
* `shutdown`: Shuts down or restarts the computer. Use `/s` for shutdown and `/r` for restart.
* `schtasks`: Schedules commands and programs to run on a computer.

## Troubleshooting and System Maintenance
* `sfc`: Scans and repairs system files.
* `chkdsk`: Checks a disk and displays a status report.