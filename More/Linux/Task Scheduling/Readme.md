# Taks Scheduling

## Systemd
Systemd is a service used in Linux systems such as Ubuntu, Redhat Linux, and Solaris to start processes and scripts at a specific time. With it, we can set up processes and scripts to run at a specific time or time interval and can also specify specific events and triggers that will trigger a specific task. To do this, we need to take some steps and precautions before our scripts or processes are automatically executed by the system.

1. Create a timer
2. Create a service3
3. Activate the timer

### Create a timer
To create a timer for systemd, we need to create a directory where the timer script will be stored.

```console
berkankutuk@kali:~$ sudo mkdir /etc/systemd/system/mytimer.timer.d
berkankutuk@kali:~$ sudo vim /etc/systemd/system/mytimer.time
```
Next, we need to create a script that configures the timer. 

The script must contain the following options: "Unit", "Timer" and "Install". 
* The "Unit" option specifies a description for the timer. 
* The "Timer" option specifies when to start the timer and when to activate it. 
* Finally, the "Install" option specifies where to install the timer.

```text
[Unit]
Description=My Timer

[Timer]
OnBootSec=3min
OnUnitActiveSec=1hour

[Install]
WantedBy=timers.target
```

### Create a Service
```console
berkankutuk@kali:~$ sudo vim /etc/systemd/system/mytimer.service
```

Here we set a description and specify the full path to the script we want to run. The "multi-user.target" is the unit system that is activated when starting a normal multi-user mode. It defines the services that should be started on a normal system startup.

```text
[Unit]
Description=My Service

[Service]
ExecStart=/full/path/to/my/script.sh

[Install]
WantedBy=multi-user.target
```

After that, we have to let systemd read the folders again to include the changes by reloading systemd.

```console
berkankutuk@kali:~$ sudo systemctl daemon-reload
```

Now, both the timer and the service are ready to be started.

```console	
berkankutuk@kali:~$ sudo systemctl start mytimer.service
berkankutuk@kali:~$ sudo systemctl enable mytimer.service
```

## Cron
Cron is a time-based job scheduler in Unix-like computer operating systems. 

With Cron, we can automate the same tasks, but the process for setting up the Cron daemon is a little different than Systemd. To set up the cron daemon, we need to store the tasks in a file called crontab and then tell the daemon when to run the tasks. Then we can schedule and automate the tasks by configuring the cron daemon accordingly. The structure of Cron consists of the following components:

| Time Frame             | Description                                                           |
|------------------------|-----------------------------------------------------------------------|
| Minutes (0-59)         | This specifies in which minute the task should be executed.           |
| Hours (0-23)           | This specifies in which hour the task should be executed.             |
| Days of month (1-31)   | This specifies on which day of the month the task should be executed. |
| Months (1-12)          | This specifies in which month the task should be executed.            |
| Days of the week (0-7) | This specifies on which day of the week the task should be executed.  |

For example, such a crontab could look like this:

```python	
# System Update
* */6 * * /path/to/update_software.sh

# Execute scripts
0 0 1 * * /path/to/scripts/run_scripts.sh

# Cleanup DB
0 0 * * 0 /path/to/scripts/clean_database.sh

# Backups
0 0 * * 7 /path/to/scripts/backup.sh
```
The "System Update" should be executed every sixth hour. This is indicated by the entry */6 in the minute column. The task is executed by the script update_software.sh, whose path is given in the last column.

The task execute scripts is to be executed every first day of the month at midnight. This is indicated by the entries 0 and 0 in the minute and hour columns and 1 in the days-of-the-month column. The task is executed by the run_scripts.sh script, whose path is given in the last column.

The third task, Cleanup DB, is to be executed every Sunday at midnight. This is specified by the entries 0 and 0 in the minute and hour columns and 0 in the days-of-the-week column. The task is executed by the clean_database.sh script, whose path is given in the last column.

The fourth task, backups, is to be executed every Sunday at midnight. This is indicated by the entries 0 and 0 in the minute and hour columns and 7 in the days-of-the-week column. The task is executed by the backup.sh script, whose path is given in the last column.

It is also possible to receive notifications when a task is executed successfully or unsuccessfully. In addition, we can create logs to monitor the execution of the tasks.

## Systemd vs. Cron
The key difference between these two tools is how they are configured. 

With Systemd, you need to create a timer and services script that tells the operating system when to run the tasks. On the other hand, with Cron, you need to create a crontab file that tells the cron daemon when to run the tasks.

