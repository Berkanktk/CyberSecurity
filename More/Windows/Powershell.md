# Powershell

## Start a process
The `"Start-Process"` command can be used to start a process.

## Get all processes
`Get-Proces`s is useful to list all running processes.

## Command outputs
Especially with command outputs that may be difficult to read or need further processing appending the `“Export-Csv”` command will create a CSV file with the output of the first command.

## Reading files
Similar to `“cat”` on Linux and `“type”` on the Windows command-line, `“Get-Content”` can be used to display the content of a file.

## Copy and move
Files can be copied and moved with `“Copy-Item”` and `“Move-Item”`, respectively.

## File hashes
Although not directly related to penetration tests, hashes are handy to compare files or search for malware samples on platforms such as VirusTotal. The built-in `“Get-FileHash”` command can be used to obtain hashes on most formats.  
`Get-FileHash -Algorithm MD5 .\powerview.ps1`

## Execution bypass
Bypasses the prevention of the execution of PowerShell scripts on Windows systems  
`Powershell -ExecutionPolicy Bypass - File {file_path}`