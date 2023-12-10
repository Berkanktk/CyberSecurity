# Windows Fundamentals

# List of Contents
1. [Windows Editions](#windows-editions)
2. [The File System](#the-file-system)
3. [The Windows\System32 Folders](#the-windowssystem32-folders)
4. [User Accounts, Profiles, and Permissions](#user-accounts-profiles-and-permissions)
5. [User Account Control](#user-account-control)
6. [Settings and the Control Panel](#settings-and-the-control-panel)
7. [Task Manager](#task-manager)
8. [System Configuration](#system-configuration)
9. [Computer Management](#computer-management)
10. [System Information](#system-information)
11. [Resource Monitor](#resource-monitor)
12. [Command Prompt](#command-prompt)
13. [Registry Editor](#registry-editor)
14. [Windows Updates](#windows-updates)
15. [Windows Security](#windows-security)
16. [Virus & threat protection](#virus--threat-protection)
    1.  [Current threats](#current-threats)
    2.  [Virus & threat protection settings](#virus--threat-protection-settings)
17. [Firewall & network protection](#firewall--network-protection)
18. [App & browser control](#app--browser-control)
19. [Device security](#device-security)
20. [BitLocker](#bitlocker)
21. [Volume Shadow Copy Service](#volume-shadow-copy-service)

# Windows Editions

The Windows operating system has a long history dating back to 1985, and currently, it is the dominant operating system in both home use and corporate networks. Because of this, Windows has always been targeted by hackers & malware writers.

Windows XP was a popular version of Windows and had a long-running. Microsoft announced Windows Vista, which was a complete overhaul of the Windows operating system. There were many issues with Windows Vista. It wasn't received well by Windows users, and it was quickly phased out.

When Microsoft announced the end-of-life date for Windows XP, many customers panicked. Corporations, hospitals, etc., scrambled and tested the next viable Windows version, which was Windows 7, against many other hardware and devices. Vendors had to work against the clock to ensure their products worked with Windows 7 for their customers. If they couldn't, their customers had to break their agreement and find another vendor that upgraded their products to work with Windows 7. It was a nightmare for many, and Microsoft took note of it.

Windows 7, as quickly as it was released soon after, was marked with an end of support date. Windows 8.x came and left and it was short-lived, like Vista.

Then arrived [Windows 10](https://www.microsoft.com/en-us/windows/features?activetab=NewPopular), which is the current Windows operating system version for desktop computers.

Windows 10 comes in 2 flavors, Home and Pro. You can read the difference between the Home and Pro [here](https://www.microsoft.com/en-us/windows/compare-windows-10-home-vs-pro).

Even though we didn't talk about servers, the current version of the Windows operating system for servers is [Windows Server 2019](https://www.microsoft.com/en-us/windows-server).

Many critics like to bash on Microsoft, but they have made long strides to improve the usability and security with each new version of Windows.

**Note**: The Windows edition for the attached VM is Windows Server 2019 Standard, as seen in **System Information**.

**Update**: As of June 2021, Microsoft announced the retirement dates for Windows 10 [here](https://docs.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro?ranMID=24542&ranEAID=kXQk6*ivFEQ&ranSiteID=kXQk6.ivFEQ-M28j3qbUhtM2JFCT2wmhOA&epi=kXQk6.ivFEQ-M28j3qbUhtM2JFCT2wmhOA&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=%28ir__uszrgcddyskfqz3fkk0sohz3wv2xuurc01kgzkod00%29%287593%29%281243925%29%28kXQk6.ivFEQ-M28j3qbUhtM2JFCT2wmhOA%29%28%29&irclickid=_uszrgcddyskfqz3fkk0sohz3wv2xuurc01kgzkod00&ranMID=24542&ranEAID=kXQk6*ivFEQ&ranSiteID=kXQk6.ivFEQ-4cKUPfbv9lM_IR2EX7K_hw&epi=kXQk6.ivFEQ-4cKUPfbv9lM_IR2EX7K_hw&irgwc=1&OCID=AID2000142_aff_7593_1243925&tduid=%28ir__feexvhocigkfqna9kk0sohznb32xutanagupypus00%29%287593%29%281243925%29%28kXQk6.ivFEQ-4cKUPfbv9lM_IR2EX7K_hw%29%28%29&irclickid=_feexvhocigkfqna9kk0sohznb32xutanagupypus00).

"Microsoft will continue to support at least one Windows 10 Semi-Annual Channel until October 14, 2025".

# The File System

The file system used in modern versions of Windows is the **New Technology File System** or simply [NTFS](https://docs.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview).

Before NTFS, there was **FAT16/FAT32** (File Allocation Table) and **HPFS** (High Performance File System).

You still see FAT partitions in use today. For example, you typically see FAT partitions in USB devices, MicroSD cards, etc. but traditionally not on personal Windows computers/laptops or Windows servers.

NTFS is known as a journaling file system. In case of a failure, the file system can automatically repair the folders/files on disk using information stored in a log file. This function is not possible with FAT.

NTFS addresses many of the limitations of the previous file systems; such as:

- Supports files larger than 4GB
- Set specific permissions on folders and files
- Folder and file compression
- Encryption ([Encryption File System](https://docs.microsoft.com/en-us/windows/win32/fileio/file-encryption) or **EFS**)

If you're running Windows, what is the file system your Windows installation is using? You can check the Properties (right-click) of the drive your operating system is installed on, typically the C drive (C:\).

You can read Microsoft's official documentation on FAT, HPFS, and NTFS [here](https://docs.microsoft.com/en-us/troubleshoot/windows-client/backup-and-storage/fat-hpfs-and-ntfs-file-systems).

Let's speak briefly on some features that are specific to NTFS.

On NTFS volumes, you can set permissions that grant or deny access to files and folders.

The permissions are:

- **Full control**
- **Modify**
- **Read & Execute**
- **List folder contents**
- **Read**
- **Write**

# The Windows\System32 Folders

The Windows folder (`C:\Windows`) is traditionally known as the folder which contains the Windows operating system.

The folder doesn't have to reside in the C drive necessarily. It can reside in any other drive and technically can reside in a different folder.

This is where environment variables, more specifically system environment variables, come into play. Even though not discussed yet, the system  environment variable for the Windows directory is `%windir%`.

Per [Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.1), "Environment variables store information about the operating system environment. This information includes details such as the operating system path, the number of processors used by the operating system, and the location of temporary folders".

The System32 folder holds the important files that are critical for the operating system.

You should proceed with extreme caution when interacting with this folder. Accidentally deleting any files or folders within System32 can render the Windows OS inoperational. Read more about this action [here](https://www.howtogeek.com/346997/what-is-the-system32-directory-and-why-you-shouldnt-delete-it/).

**Note**: Many of the tools that will be covered in the Windows Fundamentals series reside within the System32 folder.

# User Accounts, Profiles, and Permissions

User accounts can be one of two types on a typical local Windows system: Administrator & Standard User.

The user account type will determine what actions the user can perform on that specific Windows system.

- An Administrator can make changes to the system: add users, delete users, modify groups, modify settings on the system, etc.
- A Standard User can only make changes to folders/files attributed to the user & can't perform system-level changes, such as install programs.

You are currently logged in as an Administrator. There are several ways to determine which user accounts exist on the system.

One way is to click the `Start Menu` and type `Other User`. A shortcut to `System Settings > Other users` should appear.

When a user account is created, a profile is created for the user. The location for each user profile folder will fall under is C:\Users.

For example, the user profile folder for the user account Max will be C:\Users\Max.

Each user profile will have the same folders; a few of them are:

- Desktop
- Documents
- Downloads
- Music
- Pictures

Another way to access this information, and then some, is using **Local User and Group Management**.

Right-click on the Start Menu and click **Run**. Type `lusrmgr.msc`.

# User Account Control

The large majority of home users are logged into their Windows systems as local administrators. Remember that any user with administrator as the account type can make changes to the system.

A user doesn't need to run with high (elevated) privileges on the system to run tasks that don't require such privileges, such as surfing the Internet, working on a Word document, etc. This elevated privilege increases the risk of system compromise because it makes it easier for malware to infect the system. Consequently, since the user account can make changes to the system, the malware would run in the context of the logged-in user.

To protect the local user with such privileges, Microsoft introduced **User Account Control** (UAC). This concept was first introduced with the short-lived [Windows Vista](https://en.wikipedia.org/wiki/Windows_Vista) and continued with versions of Windows that followed.

**Note**: UAC (by default) doesn't apply for the built-in local administrator account.

How does UAC work? When a user with an account type of administrator logs into a system, the current session doesn't run with elevated permissions. When an operation requiring higher-level privileges needs to execute, the user will be prompted to confirm if they permit the operation to run.

Let's look at the program on the account you're currently logged into, the built-in administrator account—Right-click to view its Properties.

In the Security tab, we can see the users/groups and their permissions to this file. Notice that the standard user is not listed.

# Settings and the Control Panel

On a Windows system, the primary locations to make changes are the Settings menu and the Control Panel.

For a long time, the Control Panel has been the go-to location to make system changes, such as adding a printer, uninstall a program, etc.

The Settings menu was introduced in Windows 8, the first Windows operating system catered to touch screen tablets, and is still available in Windows 10. As a matter of fact, the Settings menu is now the primary location a user goes to if they are looking to change the system.

Control Panel is the menu where you will access more complex settings and perform more complex actions. In some cases, you can start in Settings and end up in the Control Panel.

For example, in Settings, click on **Network & Internet**.

# Task Manager

The Task Manager provides information about the applications and processes currently running on the system. Other information is also available, such as how much CPU and RAM are being utilized, which falls under Performance.

# System Configuration

The **System Configuration** utility (`MSConfig`) is for advanced troubleshooting, and its main purpose is to help diagnose startup issues.

Note: You need local administrator rights to open this utility.

The utility has five tabs across the top. Below are the names for each tab.

1. General
2. Boot
3. Services
4. Startup
5. Tools

- In the **General** tab, we can select what devices and services for Windows to load upon boot. The options are: Normal, Diagnostic, or Selective.
- In the **Boot** tab, we can define various boot options for the Operating System.
- The **Services** tab lists all services configured for the system regardless of their state (running or stopped). A service is a special type of application that runs in the background.
- In the **Startup** tab, you won't see anything interesting in the attached VM
    - Microsoft advises using Task Manager (taskmgr) to manage (enable/disable) startup items. The System Configuration utility is NOT a startup management program.
- There is a list of various utilities (**tools**) in the Tools tab that we can run to configure the operating system further. There is a brief description of each tool to provide some insight into what the tool is for.
    - Notice the Selected command section. The information in this textbox will change per tool.
    - To run a tool, we can use the command to launch the tool via the run prompt, command prompt, or by clicking the Launch button.

# Computer Management

The Computer Management (`compmgmt`) utility has three primary sections: System Tools, Storage, and Services and Applications.

**System Tools**

Let's start with **Task Scheduler**. Per Microsoft, with Task Scheduler, we can create and manage common tasks that our computer will carry out automatically at the times we specify.

A task can run an application, a script, etc., and tasks can be configured to run at any point. A task can run at log in or at log off. Tasks can also be configured to run on a specific schedule, for example, every five mins.

To create a basic task, click on `Create Basic Task` under **Actions** (right pane).

Next is **Event Viewer**.

Event Viewer allows us to view events that have occurred on the computer. These records of events can be seen as an audit trail that can be used to understand the activity of the computer system. This information is often used to diagnose problems and investigate actions executed on the system.

Event Viewer has three panes.

1. The pane on the left provides a hierarchical tree listing of the event log providers. (as shown in the image above)
2. The pane in the middle will display a general overview and summary of the events specific to a selected provider.
3. The pane on the right is the actions pane.

There are five types of events that can be logged
1. **Error** - An error event indicates that a significant problem has occurred on the system.
2. **Warning** - A warning event indicates a problem that is not immediately significant, but that may signify conditions that could cause future problems.
3. **Information** - An information event describes the successful operation of an application, driver, or service.
4. **Success Audit** - A success audit event indicates that a user or application has successfully performed an audited security event.
5. **Failure Audit** - A failure audit event indicates that a user or application has failed to perform an audited security event.

The standard logs are visible under Windows Logs.
1. Application - This log contains events logged by applications or programs.
2. Security - This log contains events such as valid and invalid logon attempts, as well as events related to resource use, such as creating, opening, or deleting files or other objects.
3. System - This log contains events logged by Windows system components.
4. Custom Log - This log contains events that are logged by a specific application or component.

The Local Users and Groups it's `lusrmgr.msc`  

**Performance**  
In Performance, you'll see a utility called Performance Monitor (`perfmon`).  

**Disk Management**  
Disk Management is a system utility in Windows that enables you to perform advanced storage tasks.  Some tasks are:

Under Storage is Windows Server Backup and Disk Management. (`diskmgmt.msc`)

- Set up a new drive
- Extend a partition
- Shrink a partition
- Assign or change a drive letter (ex. E:)

# System Information

We're continuing with Tools that are available through the System Configuration panel.

What is the **System Information** (`msinfo32`) tool?

Per Microsoft, "Windows includes a tool called Microsoft System Information (Msinfo32.exe).  This tool gathers information about your computer and displays a comprehensive view of your hardware, system components, and software environment, which you can use to diagnose computer issues."

The  information in **System Summary** is divided into three sections:

- **Hardware Resources**
- **Components**
- **Software Environment**

System Summary will display general technical specifications for the computer, such as processor brand and model.

The information displayed in **Hardware Resources** is not for the average computer user. If you want to learn more about this section, refer to the official Microsoft page.

Under **Components**, you can see specific information about the hardware devices installed on the computer. Some sections don't show any information, but some sections do, such as Display and Input.

In the **Software Environment** section, you can see information about software baked into the operating system and software you have installed. Other details are visible in this section as well, such as the Environment Variables and Network Connections.

# Resource Monitor

We're continuing with Tools that are available through the System Configuration panel.

What is **Resource Monitor** (`resmon`)?

Per Microsoft, "Resource Monitor displays per-process and aggregate CPU, memory, disk, and network usage information, in addition to providing details about which processes are using individual file handles and modules. Advanced filtering allows users to isolate the data related to one or more processes (either applications or services), start, stop, pause, and resume services, and close unresponsive applications from the user interface. It also includes a process analysis feature that can help identify deadlocked processes and file locking conflicts so that the user can attempt to resolve the conflict instead of closing an application and potentially losing data."

As some of the other tools mentioned in this room, this utility is geared primarily to advanced users who need to perform advanced troubleshooting on the computer system.

In the Overview tab, Resmon has four sections:

- **CPU**
- **Disk**
- **Network**
- **Memory**

# Command Prompt

We're continuing with Tools that are available through the System Configuration panel.

The command prompt (`cmd`) can seem daunting at first, but it's really not that bad once you understand how to interact with it.

In early operating systems, the command line was the sole way to interact with the operating system.

When the GUI (graphical user interface) was introduced, it allowed users to perform complex tasks with a few clicks of a button instead of entering commands in the command prompt.

Even though the GUI is the primary way to interact with the operating system, a computer user can still interact via the command prompt.

In this task, we'll only cover a few commands that a computer user can run in the command prompt to obtain information about the computer system.

Let's start with a few simple commands, such as `hostname` and `whoami`.
* The command hostname will output the computer name.
* The command whoami will output the name of the logged-in user.

Next, let's look at some commands that are useful when troubleshooting.

A command used often is `ipconfig`. This command will show the network address settings for the computer.

The next command is netstat. Per the help manual, this command will display protocol statistics and current TCP/IP network connections.

# Registry Editor

We're continuing with Tools that are available through the System Configuration panel.

The **Windows Registry** (per Microsoft) is a central hierarchical database used to store information necessary to configure the system for one or more users, applications, and hardware devices.

The registry contains information that Windows continually references during operation, such as:

- Profiles for each user
- Applications installed on the computer and the types of documents that each can create
- Property sheet settings for folders and application icons
- What hardware exists on the system
- The ports that are being used.

**Warning**: The registry is for advanced computer users. Making changes to the registry can affect normal computer operations.

There are various ways to view/edit the registry. One way is to use the **Registry Editor** (`regedit`).

# Windows Updates

Let's start things off with **Windows** **Update**.

Windows Update is a service provided by Microsoft to provide security updates, feature enhancements, and patches for the Windows operating system and other Microsoft products, such as Microsoft Defender.

Updates are typically released on the 2nd Tuesday of each month. This day is called **Patch Tuesday**. That doesn't necessarily mean that a critical update/patch has to wait for the next Patch Tuesday to be released. If the update is urgent, then Microsoft will push the update via the Windows Update service to the Windows devices.

Refer to the following link to see the **Microsoft Security Update** **Guide** [here](https://msrc.microsoft.com/update-guide)**.** 

Windows Update is located in Settings. See below.

**Tip**: Another way to access Windows Update is from the Run dialog box, or CMD, by running the command `control /name Microsoft.WindowsUpdate`.

# Windows Security

Per Microsoft, "***Windows Security** is your home to manage the tools that protect your device and your data*".

In case you missed it, **Windows Security** is also available in **Settings**.

Focus your attention on **Protection areas**.

- **Virus & threat protection**
- **Firewall & network protection**
- **App & browser control**
- **Device security**

# Virus & threat protection

Virus & threat protection is divided into two parts:

- **Current threats**
- **Virus & threat protection settings**

## Current threats

**Scan options**

- **Quick scan** - Checks folders in your system where threats are commonly found.
- **Full scan** - Checks all files and running programs on your hard disk. This scan could take longer than one hour.
- **Custom scan** - Choose which files and locations you want to check.

**Threat history**

- **Last scan** - Windows Defender Antivirus automatically scans your device for viruses and other threats to help keep it safe.
- **Quarantined threats** - Quarantined threats have been isolated and prevented from running on your device. They will be periodically removed.
- **Allowed threats** - Allowed threats are items identified as threats, which you allowed to run on your device.

**Warning**: Allow an item to run that has been identified as a threat only if you are **100%** sure of what you are doing.

Next is **Virus & threat protection settings**.

## Virus & threat protection settings

**Manage settings**

- **Real-time protection** - Locates and stops malware from installing or running on your device.
- **Cloud-delivered protection** - Provides increased and faster protection with access to the latest protection data in the cloud.
- **Automatic sample submission** - Send sample files to Microsoft to help protect you and others from potential threats.
- **Controlled folder access** - Protect files, folders, and memory areas on your device from unauthorized changes by unfriendly applications.
- **Exclusions** Windows Defender Antivirus won't scan items that you've excluded.
- **Notifications** - Windows Defender Antivirus will send notifications with critical information about the health and security of your device.

Warning: Excluded items could contain threats that make your device vulnerable. Only use this option if you are **100%** sure of what you are doing.

**Virus & threat protection updates**

- **Check for updates** - Manually check for updates to update Windows Defender Antivirus definitions.

**Ransomware protection**

- **Controlled folder access** - Ransomware protection requires this feature to be enabled, which in turn requires Real-time protection to be enabled.

**Note**: Real-time protection is turned off in the attached VM to decrease the chances of performance issues. Since the VM can't reach the Internet and there aren't any threats in the VM, this is safe to do. Real-time protection should definitely be enabled in your personal Windows devices unless you have a 3rd party product that provides the same protection. Ensure it's always up-to-date and enabled.

**Tip**: You can perform on-demand scans on any file/folder by right-clicking the item and selecting 'Scan with Microsoft Defender'.

# Firewall & network protection

What is a **firewall**?

Per Microsoft, "*Traffic flows into and out of devices via what we call ports. A firewall is what controls what is - and more importantly isn't - allowed to pass through those ports. You can think of it like a security guard standing at the door, checking the ID of everything that tries to enter or exit*".

**Note**: Each network may have different status icons for you.

What is the difference between the 3 (**Domain**, **Private**, and **Public**)?

Per Microsoft, "*Windows Firewall offers three firewall profiles: domain, private and public".*

- **Domain** - *The domain profile applies to networks where the host system can authenticate to a domain controller.*
- **Private** - *The private profile is a user-assigned profile and is used to designate private or home networks.*
- **Public** - *The default profile is the public profile, used to designate public networks such as Wi-Fi hotspots at coffee shops, airports, and other locations.*

If you click on any firewall profile, another screen will appear with two options: **turn the firewall on/off** and **block all incoming connections**.

Warning: Unless you are 100% confident in what you are doing, it is recommended that you leave your Windows Defender Firewall enabled.

Configuring the **Windows Defender Firewall** is for advanced Windows users. Refer to the following Microsoft documentation on best practices [here](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/best-practices-configuring).

**Tip:** Command to open the Windows Defender Firewall is `WF.msc`.

# App & browser control

In this section, you can change the settings for the **Microsoft Defender SmartScreen**.

Per Microsoft, "*Microsoft Defender SmartScreen protects against phishing or malware websites and applications, and the downloading of potentially malicious files*".

Refer to the official Microsoft document for more information on Microsoft Defender SmartScreen [here](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-smartscreen/microsoft-defender-smartscreen-overview).

# Device security
What is the **Trusted Platform Module** (**TPM**)?

Per Microsoft, "*Trusted Platform Module (TPM) technology is designed to provide hardware-based, security-related functions. A TPM chip is a secure crypto-processor that is designed to carry out cryptographic operations. The chip includes multiple physical security mechanisms to make it tamper-resistant, and malicious software is unable to tamper with the security functions of the TPM*".

# BitLocker

What is **BitLocker**?

Per Microsoft, "*BitLocker Drive Encryption is a data protection feature that integrates with the operating system and addresses the threats of data theft or exposure from lost, stolen, or inappropriately decommissioned computers*".

On devices with TPM installed, BitLocker offers the best protection.

Per Microsoft, "*BitLocker provides the most protection when used with a Trusted Platform Module (TPM) version 1.2 or later. The TPM is a hardware component installed in many newer computers by the computer manufacturers. It works with BitLocker to help protect user data and to ensure that a computer has not been tampered with while the system was offline*".

Refer to the official Microsoft documentation to learn more about BitLocker [here](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview).

**Note**: The BitLocker feature is not included in the attached VM.

# Volume Shadow Copy Service

Per [Microsoft](https://docs.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service), the Volume Shadow Copy Service (VSS) coordinates the required actions to create a consistent shadow copy (also known as a snapshot or a point-in-time copy) of the data that is to be backed up.

Volume Shadow Copies are stored on the System Volume Information folder on each drive that has protection enabled.

If VSS is enabled (**System Protection** turned on), you can perform the following tasks from within **advanced system settings**.

- **Create a restore point**
- **Perform system restore**
- **Configure restore settings**
- **Delete restore points**

From a security perspective, malware writers know of this Windows feature and write code in their malware to look for these files and delete them. Doing so makes it impossible to recover from a ransomware attack unless you have an offline/off-site backup.