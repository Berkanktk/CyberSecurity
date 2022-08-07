# Finding way around linux
Using `find` and `grep`

| What we can do | Syntax | Real example of syntax |
|---|---|---|
| Find files based on filename | find [directory path] -type f -name [filename] | find /home/Andy -type f -name sales.txt |
| Find Directory based on directory name | find [directory path] -type d -name [filename] | find /home/Andy -type d -name pictures |
| Find files based on size | find [directory path] -type f -size [size] | find /home/Andy -type f -size 10c (c for bytes, k for kilobytes M megabytes G for gigabytes type:'man find' for full information on the  options) |
| Find files based on username | find [directory path] -type f -user [username] | find /etc/server -type f -user john |
| Find files based on group name | find [directory path] -type f -group [group name] | find /etc/server -type f -group teamstar |
| Find files modified after a specific date | find [directory path] -type f -newermt '[date and time]' | find / -type f -newermt '6/30/2020 0:00:00' (all dates/times after 6/30/2020 0:00:00 will be considered a condition to look for) |
| Find files based on date modified | find [directory path] -type f -newermt [start date range] ! -newermt [end date range] | find / -type f -newermt 2013-09-12 ! -newermt 2013-09-14 (all dates before 2013-09-12 will be excluded; all dates after 2013-09-14 will be excluded, therefore this only leaves 2013-09-13 as the date to look for.) |
| Find files based on date accessed | find [directory path] -type f -newerat [start date range] ! -newerat [end date range] | find / -type f -newerat 2017-09-12 ! -newerat 2017-09-14 (all dates before 2017-09-12 will be excluded; all dates after 2017-09-14 will be excluded, therefore this only leaves 2017-09-13 as the date to look for.) |
| Find files with a specific keyword | grep -iRl [directory path/keyword] | grep -iRl '/folderA/flag' |
| read the manual for the find command | man find | man find |