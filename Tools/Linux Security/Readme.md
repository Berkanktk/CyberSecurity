# Linux Security

Always be up to date!  
`apt update && apt dist-upgrade`

## Firewall rules
If firewall rules are not appropriately set at the network level, we can use the Linux firewall and/or iptables to restrict traffic into/out of the host.

## ssh
If SSH is open on the server, the configuration should be set up to disallow password login and disallow the root user from logging in via SSH. It is also important to avoid logging into and administering the system as the root user whenever possible and adequately managing access control. Users' access should be determined based on the principle of least privilege. For example, if a user needs to run a command as root, then that command should be specified in the sudoers configuration instead of giving them full sudo rights. Another common protection mechanism that can be used is fail2ban. This tool counts the number of failed login attempts, and if a user has reached the maximum number, the host that tried to connect will be handled as configured.

## Auditing the system
It is also important to periodically audit the system to ensure that issues do not exist that could facilitate privilege escalation, such as an out-of-date kernel, user permission issues, world-writable files, and misconfigured cron jobs, or misconfigured services. Many administrators forget about the possibility that some kernel versions have to be updated manually.

## Security settings
In addition, some security settings should be made, such as:
* Removing or disabling all unnecessary services and software
* Removing all services that rely on unencrypted authentication mechanisms
* Ensure NTP is enabled and Syslog is running
* Ensure that each user has its own account
* Enforce the use of strong passwords
* Set up password aging and restrict the use of previous passwords
* Locking user accounts after login failures
* Disable all unwanted SUID/SGID binaries