# Log Analysis
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