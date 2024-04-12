# Volatility 3
Volatility is a memory forensics framework that allows the extraction of digital artifacts from memory dumps. It is used to analyze the memory of a running system, and it is commonly used in incident response and malware analysis. Volatility 3 is the latest version of the framework, and it has been rewritten in Python 3.

> To begin analyzing a dump, you will first need to identify the image type; there are multiple ways of identifying this information that we will cover later.

# Table of Contents
- [Installation](#installation)
- [Memory Extraction](#memory-extraction)
- [Plugins](#plugins)
- [Identifying Image Info and Profile](#identifying-image-info-and-profile)
- [Listing Processes and Connections](#listing-processes-and-connections)
- [Volatility Hunting and Detection Capabilities](#volatility-hunting-and-detection-capabilities)
- [Advanced Memory Forensics](#advanced-memory-forensics)
- [Practical Use](#practical-use)
- [Resources](#resources)
  
# Installation
When downloading, you can make a choice to use the pre-packaged executable (.whl file) that will work the same and requires no dependencies (Windows Only), or you can decide to run it directly from Python.

To obtain a pre-packaged executable, simply download a zip file containing the application from their releases page. https://github.com/volatilityfoundation/volatility3/releases/tag/v1.0.1

To begin running the project from source, you will need to first download the following dependencies: Python 3.5.3 or later and Pefile 2017.8.1 or later. https://pypi.org/project/pefile/

```bash
git clone https://github.com/volatilityfoundation/volatility3.git
```
You now have Volatility installed!

To test your installation run the vol.py file with the help parameter.

```bash
python3 vol.py -h
```

It is important to note that for any Linux or Mac memory files, you will need to download the symbol files from the Volatility GitHub. https://github.com/volatilityfoundation/volatility3#symbol-tables

See the [Volatility Wiki](https://github.com/volatilityfoundation/volatility/wiki) for more information.

# Memory Extraction
Extracting a memory dump can be performed in numerous ways, varying based on the requirements of your investigation. Listed below are a few of the techniques and tools that can be used to extract a memory from a bare-metal machine.

* FTK Imager
* Redline
* DumpIt.exe
* win32dd.exe / win64dd.exe
* Memoryze
* FastDump

When using an extraction tool on a bare-metal host, it can usually take a considerable amount of time; take this into consideration during your investigation if time is a constraint.

Most of the tools mentioned above for memory extraction will output a `.raw` file with some exceptions like Redline that can use its own agent and session structure.

## Virtual Machines
For virtual machines, gathering a memory file can easily be done by collecting the virtual memory file from the host machine’s drive. This file can change depending on the hypervisor used; listed below are a few of the hypervisor virtual memory files you may encounter.

* VMWare - .`vmem`
* Hyper-V - `.bin`
* Parallels - `.mem`
* VirtualBox - `.sav` file *this is only a partial memory file

# Plugins
Volatility 3 has a wide range of plugins that can be used to extract digital artifacts from memory dumps. These plugins can be used to extract information such as running processes, network connections, registry hives, and more. The plugins are organized into different categories based on the type of information they extract.

In previous Volatility versions, you would need to identify a specific OS profile exact to the operating system and build version of the host, which could be hard to find or used with a plugin that could provide false positives. With Volatility3, profiles **have been scrapped**, and Volatility will automatically identify the host and build of the memory file.

The naming structure of plugins has also changed. In previous versions of Volatility, the naming convention has been simply the name of the plugin and was universal for all operating systems and profiles. Now with Volatility3, you need to specify the operating system prior to specifying the plugin to be used, for example, `windows.info` vs `linux.info`. This is because there are no longer profiles to distinguish between various operating systems for plugins as each operating system has drastically different memory structures and operations. Look below for options of operating system plugin syntax.

* `.windows`
* `.linux`
* `.mac`

There are several plugins available with Volatility as well as third-party plugins; we will only be covering a small portion of the plugins that Volatility has to offer.

To get familiar with the plugins available, utilize the help menu. 

```bash
python3 vol.py -h
```

As Volatility3 is currently in active development, there is still a short list of plugins compared to its python 2 counterpart; however, the current list still allows you to do all of your analysis as needed.

For volatility 2, some useful plugins that aren't available in volatility 3 are:
* hashdump
* shutdowntime

# Identifying Image Info and Profile
By default, Volatility comes with all existing Windows profiles from Windows XP to Windows 10.

Image profiles can be hard to determine if you don't know exactly what version and build the machine you extracted a memory dump from was. In some cases, you may be given a memory file with no other context, and it is up to you to figure out where to go from there. In that case, Volatility has your back and comes with the `imageinfo` plugin. This plugin will take the provided memory dump and assign it a list of the best possible OS profiles. OS profiles have since been deprecated with Volatility3, so we will only need to worry about identifying the profile if using Volatility2; this makes life much easier for analyzing memory dumps.

> Note: imageinfo is not always correct and can have varied results depending on the provided dump; use with caution and test multiple profiles from the provided list.

If we are still looking to get information about what the host is running from the memory dump, we can use the following three plugins` windows.info`, `linux.info` & `mac.info`. This plugin will provide information about the host from the memory dump.

Syntax
```bash
python3 vol.py -f <file> windows.info
```

# Listing Processes and Connections
Five different plugins within Volatility allow you to dump processes and network connections, each with varying techniques used.

## pslist
The most basic way of listing processes is using `pslist`; this plugin will get the list of processes from the doubly-linked list that keeps track of processes in memory, equivalent to the process list in task manager. The output from this plugin will include all current processes and terminated processes with their exit times.

```bash
python3 vol.py -f <file> windows.pslist
```

## psscan
Some malware, typically rootkits, will, in an attempt to hide their processes, unlink itself from the list. By unlinking themselves from the list you will no longer see their processes when using `pslist`. To combat this evasion technique, we can use `psscan`;this technique of listing processes will locate processes by finding data structures that match `_EPROCESS`. While this technique can help with evasion countermeasures, it can also cause false positives.

```bash
python3 vol.py -f <file> windows.psscan
```

## pstree
The `pstree` plugin will list the processes in a tree format, showing the parent and child processes. This plugin is useful for understanding the relationships between processes and can help identify malicious processes that are spawned from other processes.

```bash
python3 vol.py -f <file> windows.pstree
```

## netstat
The `netstat` plugin will list all network connections that are currently active on the system. This plugin is useful for identifying network connections that may be malicious or unauthorized.

```bash
python3 vol.py -f <file> windows.netstat
```

This command in the current state of volatility3 can be very unstable, particularly around old Windows builds. To combat this, you can utilize other tools like bulk_extractor to extract a PCAP file from the memory file. In some cases, this is preferred in network connections that you cannot identify from Volatility alone. https://tools.kali.org/forensics/bulk-extractor

## dlllist
The last plugin we will cover is `dlllist`. This plugin will list all DLLs associated with processes at the time of extraction. This can be especially useful once you have done further analysis and can filter output to a specific DLL that might be an indicator for a specific type of malware you believe to be present on the system.

```bash
python3 vol.py -f <file> windows.dlllist
```
# Volatility Hunting and Detection Capabilities
Volatility offers a plethora of plugins that can be used to aid in your hunting and detection capabilities when hunting for malware or other anomalies within a system's memory.

## malfind
The first plugin we will be talking about that is one of the most useful when hunting for code injection is malfind. This plugin will attempt to identify injected processes and their PIDs along with the offset address and a Hex, Ascii, and Disassembly view of the infected area. The plugin works by scanning the heap and identifying processes that have the executable bit set `RWE or RX` and/or no memory-mapped file on disk (file-less malware).

Based on what `malfind` identifies, the injected area will change. An MZ header is an indicator of a Windows executable file. The injected area could also be directed towards shellcode which requires further analysis.

```bash	
python3 vol.py -f <file> windows.malfind
```

## yarascan
Volatility also offers the capability to compare the memory file against YARA rules. `yarascan` will search for strings, patterns, and compound rules against a rule set. You can either use a YARA file as an argument or list rules within the command line.

```bash
python3 vol.py -f <file> windows.yarascan --yara-file=<file>
```
# Advanced Memory Forensics
Advanced Memory Forensics can become confusing when you begin talking about system objects and how malware interacts directly with the system, especially if you do not have prior experience hunting some of the techniques used such as hooking and driver manipulation. When dealing with an advanced adversary, you may encounter malware, most of the time rootkits that will employ very nasty evasion measures that will require you as an analyst to dive into the drivers, mutexes, and hooked functions. A number of modules can help us in this journey to further uncover malware hiding within memory.

## Hooking
The first evasion technique we will be hunting is hooking; there are five methods of hooking employed by adversaries, outlined below:

* SSDT Hooks
* IRP Hooks
* IAT Hooks
* EAT Hooks
* Inline Hooks

We will only be focusing on hunting SSDT hooking as this one of the most common techniques when dealing with malware evasion and the easiest plugin to use with the base volatility plugins.

### SSDT

The `ssdt` plugin will search for hooking and output its results. Hooking can be used by legitimate applications, so it is up to you as the analyst to identify what is evil. As a brief overview of what SSDT hooking is: SSDT stands for System Service Descriptor Table; the Windows kernel uses this table to look up system functions. An adversary can hook into this table and modify pointers to point to a location the rootkit controls.

There can be hundreds of table entries that `ssdt` will dump; you will then have to analyze the output further or compare against a baseline. A suggestion is to use this plugin after investigating the initial compromise and working off it as part of your lead investigation.

```bash
python3 vol.py -f <file> windows.ssdt 
```

## Drivers
Adversaries will also use malicious driver files as part of their evasion. Volatility offers two plugins to list drivers.

### Modules
The `modules` plugin will dump a list of loaded kernel modules; this can be useful in identifying active malware. However, if a malicious file is idly waiting or hidden, this plugin may miss it.

This plugin is best used once you have further investigated and found potential indicators to use as input for searching and filtering.

```bash
python3 vol.py -f <file> windows.modules
```

### Driverscan
The driverscan plugin will scan for drivers present on the system at the time of extraction. This plugin can help to identify driver files in the kernel that the modules plugin might have missed or were hidden.

As with the last plugin, it is again recommended to have a prior investigation before moving on to this plugin. It is also recommended to look through the modules plugin before driverscan.

```bash
python3 vol.py -f <file> windows.driverscan
```

In most cases, driverscan will come up with no output; however, if you do not find anything with the modules plugin, it can be useful to attempt using this plugin.

## Other Plugins

There are also other plugins listed below that can be helpful when attempting to hunt for advanced malware in memory.

* modscan
* driverirp
* callbacks
* idt
* apihooks
* moddump
* handles

# Practical Use
## Windows info
```bash
python3 vol.py -f <file> windows.info
```

## Dumping a process
```bash
python3 vol.py -f <file> -o <out_dir> windows.memmap.Memmap --pid <PID> --dump
```

Maybe you want to read user agents for that process
```bash
python3 vol.py -f ./ctf-files/Investigation-1.vmem -o /out/ windows.memmap.Memmap --pid 1640 --dump
cd /out/
strings *.dmp | grep -i "user-agent"
```

## Retrieve command line arguments
This plugin is designed to retrieve the command line arguments that were used to start a process. It's particularly useful because many malware and scripts rely on specific command line parameters to configure their behavior.

```bash
python3 vol.py -f <file> windows.cmdline
```

## Listing file objects
The `windows.filescan` plugin scans a memory dump to find and list file objects, providing information about files that were open at the time of the dump. It can detect files regardless of whether they are hidden or unlinked from the file system's directory structure, which makes it incredibly useful for uncovering hidden or deleted files that were still in use.

```bash
python3 vol.py -f <file> windows.filescan
```

## Using windows.handles
The `windows.handles` plugin in Volatility 3 is used to list the handle tables for processes in a memory dump. Handles are identifiers used by Windows to manage system resources such as files, registry keys, events, threads, and other system objects. 

```bash
python3 vol.py -f <file> windows.handles
```

# Resources
* A [Cheatsheet](https://andreafortuna.org/2017/07/10/volatility-my-own-cheatsheet-part-3-process-memory/) from Andrea Fortuna.