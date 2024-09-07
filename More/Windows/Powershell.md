# Powershell
Powershell is the Windows Scripting Language and shell environment built using the .NET framework.

This also allows Powershell to execute .NET functions directly from its shell. Most Powershell commands, called cmdlets, are written in .NET. Unlike other scripting languages and shell environments, the output of these cmdlets are objects - making Powershell somewhat object-oriented.

The normal format of a cmdlet is represented using Verb-Noun.

**Common verbs to use include:** Get, Start, Stop, Read, Write, New & Out

## Get help
The `“Get-Help”` command can be used to get help on any cmdlet. To get help with a particular command, run the following:
`Get-Help {command}`

## Start a process
The `"Start-Process"` command can be used to start a process.

## Get all commands
`Get-Command` is useful to list all available commands.

## Get all processes
`Get-Proces`s is useful to list all running processes.

## Print working directory
`Get-Location` is useful to print the current working directory.

## Command outputs
Especially with command outputs that may be difficult to read or need further processing appending the `“Export-Csv”` command will create a CSV file with the output of the first command.

## Piping commands
Piping commands is a common practice in Powershell. This is done by using the `“|”` character. For example, to list all processes and then export them to a CSV file, the following command can be used:
`Get-Process | Export-Csv processes.csv`

## Reading files
Similar to `“cat”` on Linux and `“type”` on the Windows command-line, `“Get-Content”` can be used to display the content of a file.

## Copy and move
Files can be copied and moved with `“Copy-Item”` and `“Move-Item”`, respectively.

## Filtering Objects
Objects can be filtered using the `“Where-Object”` command. For example, to filter processes that are not system processes, the following command can be used:
`Get-Process | Where-Object {$_.Name -notlike "System*"}`

## Sort-Object
Objects can be sorted using the `“Sort-Object”` command. For example, to sort processes by CPU usage, the following command can be used:
`Get-Process | Sort-Object`

## File hashes
Although not directly related to penetration tests, hashes are handy to compare files or search for malware samples on platforms such as VirusTotal. The built-in `“Get-FileHash”` command can be used to obtain hashes on most formats.  
`Get-FileHash -Algorithm MD5 .\powerview.ps1`

## Execution bypass
Bypasses the prevention of the execution of PowerShell scripts on Windows systems  
`Powershell -ExecutionPolicy Bypass - File {file_path}`

## Make web requests
Powershell can be used to make web requests. For example, to download a file from a URL, the following command can be used:
`Invoke-WebRequest -Uri {url} -OutFile {output_file}`

# Enumeration

## Get total users
To get the total number of users on a system, the following command can be used:
`Get-LocalUser | Measure-Object`. Remove `Measure-Object` to list all users.

## Get total groups
To get the total number of groups on a system, the following command can be used:
`Get-LocalGroup | Measure-Object`. Remove `Measure-Object` to list all groups.

## Check password requirements
To check the password requirements on a system, the following command can be used:  
`Get-LocalUser | Where-Object -Property PasswordRequired -Match false`

## Get IP Address information
To get IP address information, the following command can be used:
`Get-NetIPAddress`

## Get listening ports
To get a list of listening ports, the following command can be used:
`Get-NetTCPConnection | Where-Object -Property State -Match Listen | measure`. Remove `measure` to list all listening ports.

## See Patch History
To see the patch history of a system, the following command can be used:
`Get-HotFix`

## Scheduled Tasks
To see the scheduled tasks on a system, the following command can be used:
`Get-ScheduledTask`

## Find strings in files
To find strings in files, the following command can be used:
`findstr hello`

## Save output to a file
To save the output of a command to a file, the following command can be used:
`{command} | Out-File {output_file}`

## Send errors to null
To send errors to null, the following command can be used:
`{command} 2> $null`

## List SMB Shares
To list SMB shares on a system, the following command can be used:
`Get-SmbShare`