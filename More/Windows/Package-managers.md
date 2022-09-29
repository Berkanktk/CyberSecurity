# Chocolatey Package Manager
Chocolatey is a free and open software package management solution that can manage the installation and dependencies for our software packages and scripts

1. First, ensure that you are using an administrative shell
2. Run `Get-ExecutionPolicy`. If it returns **Restricted**, then run `Set-ExecutionPolicy AllSigned` or `Set-ExecutionPolicy Bypass -Scope Process`.
3. Copy the command into your shell and press Enter.
```bash 
$ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
4. Wait a few seconds for the command to complete.
5. If you don't see any errors, you are ready to use Chocolatey! Type `choco` or `choco -?`

## Upgrade
In order to upgrade packages, run:  
`choco upgrade chocolatey -y `

# Other alternatives
* **Windows Package Manager**: Free and open-source package manager designed for Microsoft Windows 10;
* **Cygwin**: Free and open-source software repository for Windows NT. Provides many Linux tools and an installation tool with package manager;
* **Homebrew**: a port of the MacOS package manager meant for use with Windows Subsystem for Linux, using the already existing Linux port as its base;
* **Ninite**: Proprietary package manager for Windows NT;
* **NuGet**: A Microsoft-official free and open-source package manager for Windows, available as a plugin for Visual Studio, and extendable from the command-line;
* **Pacman**: MSYS2-ported Windows version of the Arch Linux package manager;
* **wpkg**: Open-source package manager that handles Debian packages on Windows. Started as a clone of dpkg, and has many apt-get like features too;
Zero Install (0install): Cross-platform packaging and distributions software. Uses .NET Framework on Windows NT;