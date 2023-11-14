# Privilege Escalation Checklist
- [ ] Determine the kernel of the machine (Kernel Exploitation)
- [ ] Locate other services running or applications installed that may be abusable (SUID and out of date software)
- [ ] Look for automated scripts like backup scripts (Cron Jobs)
- [ ] Credentials (User accounts, application config files, etc.)
- [ ] Misconfigured file and directory permissions

# Clearing your tracks
- [ ] Clear bash history
- [ ] Clear logs
- [ ] Clear SSH keys
- [ ] Clear any other files that may contain information about you
- [ ] Clear any files that may contain information about the machine you are on

## Clearing paths
- `/var/log`
- `/var/log/auth.log` (Attempted logins for SSH, changes too or logging in as system users:)
- `/var/log/syslog` (System events such as firewall alerts:)
- `/var/log/<service/`
    - For example, the access logs of apache2
        - `/var/log/apache2/access.log`
