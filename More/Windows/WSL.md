# Info
Windows Subsystem for Linux 2 (WSL2) is the second iteration of Microsoft's architecture that allows users to run Linux instances, provides the ability to run Bash scripts and other apps like Vim, Python, etc. WSL also us to interact with the Windows operating system and file structure from a Unix instance. Best of all, it is done without the use of a hypervisor like VirtualBox or Hyper-V

## Installation

### Automatic
1. Install WSL2 with: `choco install WSL2`

Once WSL is installed, we can add the Linux platform of our choice. The most common one to find is Ubuntu on the Microsoft store. Current Linux distributions supported for WSL are:

* Ubuntu 16.04 LTS, 18.04 LTS, and 20.04 LTS
* openSUSE Leap 15.1
* SUSE Linux Enterprise Server 12 SP5 and 15 SP1
* Kali Linux
* Debian GNU/Linux
* Fedora Remix for WSL
* Pengwin and Pengwin Enterprise
* Alpine WSL

### Manual
1. Enable the Windows Subsystem for Linux: `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`
2. Check requirements for running WSL 2
   1. For x64 systems: Version 1903 or higher, with Build 18362 or higher.
   2. For ARM64 systems: Version 2004 or higher, with Build 19041 or higher.
   3. Builds lower than 18362 do not support WSL 2. Use the Windows Update Assistant to update your version of Windows.
3. Enable Virtual Machine feature
4. Download the Linux kernel update package [here](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
5. Set WSL 2 as your default version: `wsl --set-default-version 2`
6. Install your Linux distribution of choice

