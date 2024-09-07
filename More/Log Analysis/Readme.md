# Log Analysis
Logs are a record of events within a system. These records provide a detailed account of what a system has been doing, capturing a wide range of events such as user logins, file accesses, system errors, network connections, and changes to data or system configurations.

While the specific details may differ based on the type of log, a log entry usually includes the following information:

* A timestamp of when an event was logged
* The name of the system or application that generated the log entry
* The type of event that occurred
* Additional details about the event, such as the user who initiated the event or the device's IP address that generated the event

# Contextual Correlation
A single log entry may seem insignificant on its own. But when log data is aggregated, analysed, and cross-referenced with other sources of information, it becomes a potent investigation tool. Logs can answer critical questions about an event, such as:

* What happened?
* When did it happen?
* Where did it happen?
* Who is responsible?
* Were their actions successful?
* What was the result of their action?

# Security Purposes
Logging and configuration for security purposes are typically planned to detect and respond to anomalies and security issues. For example, configuration to verify the authenticity of user activity to ensure authorisation control and timely detection of unauthorised access. The main focus areas of this approach are:

* Anomaly and threat detection
* Logging user authentication data
* Ensuring the system's integrity and data confidentiality

# Log Types
Specific log types can offer a unique perspective on a system's operation, performance, and security. While there are various log types, we will focus on the most common ones that cover approximately 80% of the typical use cases.

Below is a list of some of the most common log types:

* **Application Logs**: Messages about specific applications, including status, errors, warnings, etc. 
* **Audit Logs**: Activities related to operational procedures crucial for regulatory compliance.
* **Security Logs**: Security events such as logins, permissions changes, firewall activity, etc.
* **Server Logs**: Various logs a server generates, including system, event, error, and access logs.
* **System Logs**: Kernel activities, system errors, boot sequences, and hardware status.
* **Network Log**s: Network traffic, connections, and other network-related events.
* **Database Logs**: Activities within a database system, such as queries and updates.
* **Web Server Logs**: Requests processed by a web server, including URLs, response codes, etc.

# Log Formats
A log format defines the structure and organisation of data within a log file. It specifies how the data is encoded, how each entry is delimited, and what fields are included in each row. These formats can vary widely and may fall into three main categories: Semi-structured, Structured, and Unstructured.

# Tools
**less:** The less command allows you to view the contents of a file one page at a time. Compared to the cat command, this allows you to easily review the contents without being overwhelmed by the large quantity of the log file.

After opening the file using **less**, press your `Up/Down` button to move one line at a time and `Page Up (b)/Page Down (space)` buttons to move one page at a time. Then, you can exit the view by pressing the `q` button.

**Chopping Down the Log (example)**

```tsx
timestamp - source_ip - domain:port - http_method - http_uri - status_code - response_size - user_agent

[2023/10/25:16:17:14] 10.10.140.96 storage.live.com:443 GET / 400 630 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
```

| Position | Field | Value |
| --- | --- | --- |
| 1 | Timestamp | [2023/10/25:16:17:14] |
| 2 | Source IP | 10.10.140.96 |
| 3 | Domain and Port | storage.live.com:443 |
| 4 | HTTP Method | GET |
| 5 | HTTP URI | / |
| 6 | Status Code | 400 |
| 7 | Response Size | 630 |
| 8 | User Agent | "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" |

The **cut** command allows you to extract specific sections (columns) of lines from a file or input stream by "cutting" the line into columns based on a delimiter and selecting which columns to display. This can be done using the `-d` option (for delimiter) and the `-f` for position. The example below uses space (' ') as its delimiter and only displays the timestamp (column #1 after cutting the log with space).

Count occurance

```tsx
| sort | uniq | wc -l
```

sort command arranges the list in alphabetical order

uniq command removes all the duplicates

We already have the list of unique domains based on our previous use case. Now, we only need to add some parameters to our commands to get the count of each domain accessed. This can be done by adding the `-c` option to the **uniq** command.

Moreover, the result can be sorted again based on the count of each domain by using the `-n` option of the **sort** command.

```tsx
cut -d ' ' -f3 access.log | cut -d ':' -f1 | sort | uniq -c | sort -n
```

If you want to make the output appear in descending order,  use the `-r` option