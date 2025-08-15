# PowerShell Basics

PowerShell is a Windows scripting language and shell environment built on the **.NET Framework**.
It can run **.NET functions directly** from the shell, and most commands (called **cmdlets**) are written in .NET.

Unlike many shells, PowerShell outputs **objects** instead of plain text, making it more **object-oriented**.

**Cmdlet format:**
`Verb-Noun` (e.g., `Get-Process`, `Start-Service`)

**Common verbs:**
`Get`, `Start`, `Stop`, `Read`, `Write`, `New`, `Out`


## Get Help

Get help for any cmdlet:

```powershell
Get-Help {command}
```

## Basic Commands

* **Start a process**

```powershell
Start-Process {program}
```

* **List all commands**

```powershell
Get-Command
```

* **List all running processes**

```powershell
Get-Process
```

* **Print working directory**

```powershell
Get-Location
```

* **Read a file** (like `cat` in Linux or `type` in cmd)

```powershell
Get-Content {file}
```

* **Copy / Move files**

```powershell
Copy-Item {source} {destination}
Move-Item {source} {destination}
```


## Exporting & Piping

* **Export to CSV**

```powershell
{command} | Export-Csv file.csv
```

* **Pipe commands**

```powershell
Get-Process | Export-Csv processes.csv
```

* **Save output to a file**

```powershell
{command} | Out-File file.txt
```

* **Send errors to null**

```powershell
{command} 2> $null
```


## Filtering & Sorting

* **Filter objects**

```powershell
Get-Process | Where-Object {$_.Name -notlike "System*"}
```

* **Sort objects**

```powershell
Get-Process | Sort-Object CPU
```


## File Hashes

Calculate file hashes (useful for malware analysis or file comparison):

```powershell
Get-FileHash -Algorithm MD5 .\powerview.ps1
```


## Execution Policy Bypass

Run a PowerShell script ignoring execution restrictions:

```powershell
PowerShell -ExecutionPolicy Bypass -File {file_path}
```


## Web Requests

Download a file:

```powershell
Invoke-WebRequest -Uri {url} -OutFile {output_file}
```

# Enumeration

* **Count total users**

```powershell
Get-LocalUser | Measure-Object
```

(remove `Measure-Object` to list them)

* **Count total groups**

```powershell
Get-LocalGroup | Measure-Object
```

* **Check password requirements**

```powershell
Get-LocalUser | Where-Object -Property PasswordRequired -Match false
```

* **Get IP info**

```powershell
Get-NetIPAddress
```

* **List listening ports**

```powershell
Get-NetTCPConnection | Where-Object -Property State -Match Listen | Measure-Object
```

* **View patch history**

```powershell
Get-HotFix
```

* **List scheduled tasks**

```powershell
Get-ScheduledTask
```

* **Search text in files**

```powershell
findstr hello
```

* **List SMB shares**

```powershell
Get-SmbShare
```

## DNS Queries

* **Query TXT records for a domain**

```powershell
Resolve-DnsName -Name google.com -Type TXT
```

**Explanation:** This queries DNS for **TXT records** (free-form text stored in DNS).
They are often used for:

* SPF records (email anti-spoofing)
* DKIM public keys
* DMARC policies
* Site verification (Google, Microsoft, etc.)

Example output for `google.com` might include SPF rules, verification tokens, and other service-related text.