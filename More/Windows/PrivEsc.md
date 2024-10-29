# Windows Privilege Escalation

Privilege escalation is the process of exploiting a vulnerability, misconfiguration, or oversight in an operating system or application to gain unauthorized access or higher privileges than initially granted. In Windows environments, understanding how privilege escalation works is essential for both system administrators and security professionals to secure systems effectively. This guide consolidates key concepts, techniques, and best practices to provide a thorough understanding of Windows privilege escalation.

## Table of Contents

1. [Understanding Windows Account Types](#understanding-windows-account-types)
2. [Common Privilege Escalation Vectors](#common-privilege-escalation-vectors)
3. [Initial Information Gathering](#initial-information-gathering)
4. [Harvesting Passwords from Common Locations](#harvesting-passwords-from-common-locations)
5. [Exploiting Service Misconfigurations](#exploiting-service-misconfigurations)
6. [Abusing Dangerous Privileges](#abusing-dangerous-privileges)
7. [Tools for Enumeration and Exploitation](#tools-for-enumeration-and-exploitation)
8. [Best Practices for Defense](#best-practices-for-defense)

## Understanding Windows Account Types

Windows systems have various user account types, each with different privilege levels:

- **Administrators**: Users with the highest privileges, capable of making system-wide changes and accessing all files.
- **Standard Users**: Users with limited privileges, restricted to non-essential system tasks and accessing their own files.
- **SYSTEM / LocalSystem**: A built-in account used by the OS with privileges exceeding those of administrators.
- **Local Service**: Runs services with minimal privileges, using anonymous network credentials.
- **Network Service**: Similar to Local Service but uses the computer's credentials for network authentication.
- **Domain Administrators**: In enterprise environments, users with full control over the domain and its resources.
- **Service Accounts**: Used by applications to perform tasks like backups or scans.
- **Domain Users**: Employee accounts with necessary privileges for daily tasks.
- **Local Accounts**: Accounts valid only on the local machine, not across the domain.

Accounts are often grouped for easier management and to apply collective permissions.

## Common Privilege Escalation Vectors

Privilege escalation can result from various vulnerabilities or misconfigurations:

1. **Stored Credentials**: Sensitive information left in unsecured files, scripts, or configurations.
2. **Vulnerable Software**: Outdated applications with known exploits.
3. **Insecure File/Folder Permissions**: Misconfigured permissions allowing unauthorized access to sensitive data.
4. **Insecure Service Permissions**: Services that allow modification or control by non-privileged users.
5. **DLL Hijacking**: Inserting malicious DLLs when applications search for missing ones.
6. **Unquoted Service Paths**: Services with unquoted paths containing spaces, leading to execution of unintended binaries.
7. **AlwaysInstallElevated**: Misconfigured policies allowing any user to install software with elevated privileges.
8. **Scheduled Tasks Misconfigurations**: Tasks running with higher privileges that can be manipulated.
9. **Excessive Account Privileges**: Users granted more privileges than necessary.
10. **Kernel Exploits**: Exploiting vulnerabilities in the Windows kernel.
11. **Abusing Windows Privileges**: Leveraging specific privileges like SeBackup, SeRestore, or SeTakeOwnership.

## Initial Information Gathering

Gathering system information is crucial for identifying potential escalation paths:

- **Enumerate Users**: `net users` lists user accounts.
- **Check OS Version**: `systeminfo` provides OS details.
- **List Services**: `wmic service list` or `sc query` lists installed services.
- **Check Installed Software**: Identifying software versions can reveal known vulnerabilities.
- **Review Scheduled Tasks**: `schtasks` lists tasks and their configurations.
- **Check Privileges**: `whoami /priv` lists current user privileges.

Understanding the system's landscape helps in pinpointing weaknesses.

## Harvesting Passwords from Common Locations

Passwords might be inadvertently stored in accessible locations:

### Unattended Windows Installations

Configuration files for automated installations may contain plaintext credentials:

- `C:\Unattend.xml`
- `C:\Windows\Panther\Unattend.xml`
- `C:\Windows\System32\Sysprep\Sysprep.xml`

**Example Snippet:**
```xml
<Credentials>
    <Username>Administrator</Username>
    <Domain>domain.local</Domain>
    <Password>Passw0rd!</Password>
</Credentials>
```

### PowerShell History

PowerShell commands, including those containing passwords, are stored in a history file:

- **Location:** `%UserProfile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`

**Accessing the File:**
```shell
type %UserProfile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

### Saved Windows Credentials

Windows Credential Manager stores saved credentials:

- **List Credentials:** `cmdkey /list`

While you can't see the actual passwords, if you notice any credentials worth trying, you can use them with the `runas` command and the `/savecred` option, as seen below.

```
runas /savecred /user:admin cmd.exe
```

### IIS Configuration Files

IIS web server configurations may contain sensitive data:

- **Common Locations:**
  - `C:\inetpub\wwwroot\web.config`
  - `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config`

**Searching for Connection Strings:**
```shell
findstr /si "connectionString" *.config
```

### Application Credentials

Applications like PuTTY may store session information with credentials in the registry:

- **Registry Path:** `HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions`

To retrieve the stored proxy credentials, you can search under the following registry key for ProxyPassword with the following command:

```
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

## Exploiting Service Misconfigurations

### Insecure Service Executable Permissions

If a service's executable is writable by a non-privileged user, it can be replaced with a malicious one:

- **Check Service Configuration:** `sc qc [service_name]`
- **Check File Permissions:** `icacls [path_to_executable]`

### Unquoted Service Paths

Services with unquoted paths containing spaces can be exploited:

- **Identify Vulnerable Services:** Look for unquoted paths using `sc qc`.
- **Exploit Path:** Place a malicious executable in a path that will be executed due to the unquoted service path.

**Example Vulnerable Path:**
```
C:\Program Files\Some Folder\Service.exe
```

### Insecure Service Permissions

Services with misconfigured permissions allow users to modify service settings:

- **Check Permissions with AccessChk:**
  ```shell
  accesschk.exe -uwcqv "Everyone" *
  ```
- **Modify Service Configuration:** Change the service to execute a malicious binary.



## Abusing Dangerous Privileges

### Understanding Windows Privileges

Users may have special privileges that can be leveraged:

- **List Privileges:** `whoami /priv`

### SeBackupPrivilege and SeRestorePrivilege

Allow users to read and write any file, ignoring permissions:

- **Copy Sensitive Files:**
  ```shell
  reg save hklm\sam sam.hive
  reg save hklm\system system.hive
  ```
- **Extract Password Hashes:** Use tools to extract and crack hashes from the copied hives.

### SeTakeOwnershipPrivilege

Allows taking ownership of any object on the system, including files and registry keys.

- **Take Ownership:**
  ```shell
  takeown /f [filename]
  ```
- **Grant Full Control:**
  ```shell
  icacls [filename] /grant [username]:F
  ```
- **Replace Executable:** Replace critical system files (e.g., `utilman.exe`) with a malicious one.

**Note:** Replacing `utilman.exe` can provide a SYSTEM-level command prompt at the login screen.


## Tools for Enumeration and Exploitation

### WinPEAS

An automated script for enumerating potential privilege escalation paths.

- **Usage:** Run on the target system to collect information.
- **Download:** [WinPEAS GitHub Repository](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)

### PrivescCheck

A PowerShell script that checks for common privilege escalation vulnerabilities.

- **Usage:**
  ```powershell
  Set-ExecutionPolicy Bypass -Scope Process -Force
  . .\PrivescCheck.ps1
  Invoke-PrivescCheck
  ```
- **Download:** [PrivescCheck GitHub Repository](https://github.com/itm4n/PrivescCheck)

### Windows Exploit Suggester - Next Generation (WES-NG)

Suggests exploits based on missing patches and vulnerabilities.

- **Usage:**
  ```shell
  wes.py systeminfo.txt
  ```
- **Download:** [WES-NG GitHub Repository](https://github.com/bitsadmin/wesng)

### Metasploit Framework

Provides modules for exploitation and post-exploitation.

- **Local Exploit Suggester:**
  ```shell
  use post/multi/recon/local_exploit_suggester
  ```


## Best Practices for Defense

- **Regular Updates:** Keep systems and software up to date to patch known vulnerabilities.
- **Principle of Least Privilege:** Assign the minimum necessary privileges to users and services.
- **Secure Configurations:** Ensure services and scheduled tasks have proper permissions.
- **Credential Hygiene:** Avoid storing plaintext credentials and regularly audit stored credentials.
- **Monitoring and Logging:** Implement comprehensive monitoring to detect suspicious activities.
- **Security Policies:** Enforce strong security policies and educate users on best practices.
