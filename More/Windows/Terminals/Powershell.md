# PowerShell Overview

PowerShell was created to overcome the limitations of cmd.exe and batch files, offering a more robust tool for managing Windows systems and APIs in complex enterprise environments.

## PowerShell Basics

### Cmdlets
PowerShell commands are called **cmdlets** (command-lets) and follow the consistent **Verb-Noun** naming convention, making them easy to understand.  
Examples:  
- `Get-Content`: Retrieves file content.  
- `Set-Location`: Changes the current directory.  

Use `Get-Command` to list all available cmdlets, functions, aliases, and scripts in the current session.  
```powershell
$ Get-Command
```

### Help System
`Get-Help` provides usage details for cmdlets, including examples and parameter options.  
```powershell
$ Get-Help Get-Date
$ Get-Help Get-Date -examples
```

### Aliases
Aliases are shortcuts for cmdlets to ease the transition from traditional commands.  
Examples:  
- `dir` → `Get-ChildItem`  
- `cd` → `Set-Location`  

List all aliases with:  
```powershell
$ Get-Alias
```

### Modules
PowerShell's functionality can be extended by installing additional modules from online repositories like the PowerShell Gallery.  

- **Search for Modules**  
```powershell
$ Find-Module -Name "PowerShell*"
```

- **Install a Module**  
```powershell
$ Install-Module -Name "PowerShellGet"
```

This structure makes PowerShell both powerful and user-friendly for automation and system management.

## Navigating the File System and Working with Files

- **List Files/Directories**:  
  ```powershell
  $ Get-ChildItem
  ```
- **Change Directory**:  
  ```powershell
  $ Set-Location -Path "C:\Windows"
  ```
- **Copy/Move/Delete Files**:  
  ```powershell
  $ Copy-Item -Path "file.txt" -Destination "C:\Temp"
  $ Move-Item -Path "file.txt" -Destination "C:\Temp"
  $ Remove-Item -Path "file.txt"
  ```
- **Create File/Directory**:  
  ```powershell
  $ New-Item -Path "file.txt" -ItemType "file"
  $ New-Item -Path "folder" -ItemType "directory"
  ```
- **Read/Write/Appending Content**:  
  ```powershell
  $ Get-Content -Path "file.txt"
  $ Set-Content -Path "file.txt" -Value "Hello, World!"
  $ Add-Content -Path "file.txt" -Value "Hello, again!"
  ```
- **Rename File**:  
  ```powershell
  $ Rename-Item -Path "file.txt" -NewName "newfile.txt"
  ```
- **Get File Properties**:  
  ```powershell
  $ Get-Item -Path "file.txt" | Format-List *
  ```

## Piping, Filtering, and Sorting Data

PowerShell’s pipeline `|` passes output from one cmdlet to another.

- **Sort Files by Size**:  
  ```powershell
  $ Get-ChildItem | Sort-Object Length
  ```

- **Filter Files (e.g., `.txt` only)**:  
  ```powershell
  $ Get-ChildItem | Where-Object Extension -eq ".txt"
  ```

- **Comparison Operators**:  
  - `-eq` (equal), `-ne` (not equal), `-gt` (greater), `-lt` (less), `-ge` (>=), `-le` (<=)  
  - `-like` (wildcard match), `-match` (regex match), `-contains` (contains value)

- **Select Properties or Limit Results**:  
  ```powershell
  $ Get-ChildItem | Select-Object Name, Length
  $ Get-ChildItem | Sort-Object Length -Descending | Select-Object -First 1
  ```

- **Search Text in Files**:  
  ```powershell
  $ Select-String -Path "file.txt" -Pattern "password"
  ``` 

## System and Network Information
System and network information can be retrieved using PowerShell commands.

- **Computer and OS Info**:  
  ```powershell
  $ Get-ComputerInfo
  ```
- **List Local Users**:  
  ```powershell
  $ Get-LocalUser
  ```
- **Network Configuration**:  
  ```powershell
  $ Get-NetIPConfiguration
  ```
- **List IP Addresses**:  
  ```powershell
  $ Get-NetIPAddress
  ```

## Real-Time System Analysis
PowerShell can monitor system performance and resource usage in real-time.

- **List Running Processes**:  
  ```powershell
  $ Get-Process
  ```
- **Retrieve Performance Data**:  
  ```powershell
  $ Get-Counter
  ```
- **Service Information**:  
  ```powershell
  $ Get-Service
  ```
- **Event Logs**:  
  ```powershell
  $ Get-EventLog
  $ Get-WinEvent
  ```
- **Active TCP Connections**:  
  ```powershell
  $ Get-NetTCPConnection
  ```
- **Calculate File Hash**:  
  ```powershell
  $ Get-FileHash -Path "file.txt"
  ```

## Scripting and Automation
PowerShell scripts are saved as .ps1 files and can automate complex tasks.

- **Execute Script Block on Remote Machine**:   
  ```powershell
  $ Invoke-Command -ScriptBlock { Get-Process }
  ```