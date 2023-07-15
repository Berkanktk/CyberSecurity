# Linux Service and Process Management

In general, there are two types of services: internal, the relevant services that are required at system startup, which for example, perform hardware-related tasks, and services that are installed by the user, which usually include all server services. Such services run in the background without any user interaction. These are also called daemons and are identified by the letter 'd' at the end of the program name, for example, sshd or systemd.

## Systemctl
After installing OpenSSH on our VM, we can start the service with the following command.  
`systemctl start ssh`

After we have started the service, we can now check if it runs without errors.  
`systemctl status ssh` 

To add OpenSSH to the SysV script to tell the system to run this service after startup, we can link it with the following command:   
`systemctl enable ssh`

Once we reboot the system, the OpenSSH server will automatically run. We can check this with a tool called ps.  
`ps -aux | grep ssh` 

We can also use systemctl to list all services.  
`systemctl list-units --type=service`

## Kill a Process
A process can be in the following states:

* Running
* Waiting (waiting for an event or system resource)
* Stopped
* Zombie (stopped but still has an entry in the process table).

Processes can be controlled using kill, pkill, pgrep, and killall

The most commonly used are:
| Signal | Description |
|---|---|
| 1 | SIGHUP - This is sent to a process when the terminal that controls it is closed. |
| 2 | SIGINT - Sent when a user presses [Ctrl] + C in the controlling terminal to interrupt a process. |
| 3 | SIGQUIT - Sent when a user presses [Ctrl] + D to quit. |
| 9 | SIGKILL - Immediately kill a process with no clean-up operations. |
| 15 | SIGTERM - Program termination. |
| 19 | SIGSTOP - Stop the program. It cannot be handled anymore. |
| 20 | SIGTSTP - Sent when a user presses [Ctrl] + Z to request for a service to suspend. The user can handle it afterward. |

For example, if a program were to freeze, we could force to kill it with the following command:  
`kill 9 <PID> `

## Background a Process
Set the process to the background with an AND sign (&) at the end of the command.
`ping -c 10 www.berkankutuk.dk &`

## Foreground a Process
If we want to get the background process into the foreground and interact with it again, we can use the `fg <ID>` command.

## Execute Multiple Commands
There are three possibilities to run several commands, one after the other. These are separated by:

Semicolon (`;`)  
Double ampersand characters (`&&`)  
Pipes (`|`)  

The semicolon (`;`) is a command separator and executes the commands by ignoring previous commands' results and errors.

However, it looks different if we use the double AND characters (`&&`) to run the commands one after the other. If there is an error in one of the commands, the following ones will not be executed anymore, and the whole process will be stopped.

Pipes (`|`) depend not only on the correct and error-free operation of the previous processes but also on the previous processes' results.