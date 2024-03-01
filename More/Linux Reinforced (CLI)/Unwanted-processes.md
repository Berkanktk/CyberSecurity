# Remove Unwanted Processes 
```bash
# See processes
top

# List cronjobs
cronjob -l

# List cronjobs for sudo
sudo su
cronjob -l

# Check environ
sudo cat environ

# List running services
systemctl list-unit-files
systemctl list-unit-files | grep enabled

# Stop service
sudo su
systemctl stop [redacted]
systemctl status [redacted]
systemctl disable [redacted]
```

Alright, so we can see that the status is still loaded, but it's disabled. The problem is that the service is still present in the system. To completely eradicate the service, we will have to remove the files from the file system as well.

```bash
rm -rf /etc/systemd/system/a
rm -rf /etc/systemd/system/[redacted]
systemctl daemon-reload
```