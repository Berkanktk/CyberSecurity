# Wifi Hacking 101
This guide will walk you through the basics of hacking a wifi network. It will cover the basics of WPA, capturing packets, and cracking WPA/WPA2 and WEP. It will also cover the tools needed to do this, such as the aircrack-ng suite.

# Table of Contents
1. [The basics - An Intro to WPA](#the-basics---an-intro-to-wpa)
2. [Capturing packets](#capturing-packets)
   1. [Wireless Adapter Requirements](#wireless-adapter-requirements)
   2. [The aircrack-ng Suite](#the-aircrack-ng-suite)
   3. [Quick info about Mac Addresses](#quick-info-about-mac-addresses)
   4. [Changing the MAC address](#changing-the-mac-address)
   5. [Wireless modes](#wireless-modes)
   6. [Packet sniffing](#packet-sniffing)
   7. [Wiki bands 2.4Ghz & 5Ghz](#wiki-bands-24ghz--5ghz)
3. [Cracking WPA/WPA2 & WEP](#cracking-wpawpa2--wep)
   1. [Deauthentication Attacks](#deauthentication-attacks)
   2. [WEP Cracking](#wep-cracking)
      1. [How WEP Works](#how-wep-works)
      2. [WEP Weaknesses](#wep-weaknesses)
      3. [Steps to Crack WEP](#steps-to-crack-wep)
      4. [Fake Authentication (1/2)](#fake-authentication-12)
      5. [Fake Authentication (2/2)](#fake-authentication-22)
   3. [WPA/WPA2 Cracking](#wpawpa2-cracking)
      1. [WPS feature](#wps-feature)
      2. [Hacking WPA/WPA2 Without a Wordlist](#hacking-wpawpa2-without-a-wordlist)
      3. [Capturing the handshake (If WPS is disabled)](#capturing-the-handshake-if-wps-is-disabled)
      4. [Bruteforce the handshake using a wordlist](#bruteforce-the-handshake-using-a-wordlist)

# The basics - An Intro to WPA
Most home WiFi networks, and many others, use WPA(2) personal. If you have to log in with a password and it's not WEP, then it's WPA(2) personal. WPA2-EAP uses RADIUS servers to authenticate, so if you have to enter a username and password in order to connect then it's probably that.

Previously, the WEP (Wired Equivalent Privacy) standard was used. This was shown to be insecure and can be broken by capturing enough packets to guess the key via statistical methods.

The 4 way handshake allows the client and the AP to both prove that they know they key, without telling each other. WPA and WPA2 use practically the same authentication method, so the attacks on both are the same.

The keys for WPA are derived from both the ESSID and the password for the network. The ESSID acts as a salt, making dictionary attacks more difficult. It means that for a given password, the key will still vary for each access point. This means that unless you precompute the dictionary for just that access point/MAC address, you will need to try passwords until you find the correct one.

**Key Terms**

- `SSID`: The network "name" that you see when you try and connect
- `ESSID`: An SSID that *may* apply to multiple access points, eg a company office, normally forming a bigger network. For Aircrack they normally refer to the network you're attacking.
- `BSSID`: An access point MAC (hardware) address
- `WPA2-PSK`: Wifi networks that you connect to by providing a password that's the same for everyone
- `WPA2-EAP`: Wifi networks that you authenticate to by providing a username and password, which is sent to a RADIUS server.
- `RADIUS`: A server for authenticating clients, not just for wifi.

# Capturing packets

Using the Aircrack-ng suite, we can start attacking a wifi network. This will walk you through attacking a network yourself, assuming you have a monitor mode enabled NIC.

## Wireless Adapter Requirements
1. Monitor mode (See [this](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Chipsets.md) list for chipsets that support monitor mode)
2. Packet injection
3. AP mode

Recommended ones:
* RealTek RTL8812AU
* Atheros AR9271

## The aircrack-ng Suite
The aircrack-ng suite consists of a number of tools that can be used to attack wireless networks, such as: `aircrack-ng`, `aireplay-ng`, `airodump-ng`, `airmon-ng`, etc. These are also the ones used to attack WPA networks.

The aircrack tools come by default with Kali, or can be installed with a package manager or from https://www.aircrack-ng.org/

I suggest creating a hotspot on a phone/tablet, picking a weak password (From rockyou.txt) and following along with every stage. To generate 5 random passwords from rockyou, you can use this command on Kali: 

```bash
$ head /usr/share/wordlists/rockyou.txt -n 10000 | shuf -n 5 -
```

You will need a monitor mode NIC in order to capture the 4 way handshake. Many wireless cards support this, but it's important to note that not all of them do.

Injection mode helps, as you can use it to deauth a client in order to force a reconnect which forces the handshake to occur again. Otherwise, you have to wait for a client to connect normally.

## Quick info about Mac Addresses
The IP address is used in the internet to identify computers, and communicate between devices on the internet.
The MAC address is used within the network to identify devices and transfer data between devices.

A change to a mac address benefits:
1.	Increases anonymity
2.	Impersonate other devices
3.	Bypass filters

### Changing the MAC address
1. Type `ifconfig` and look after ‘ether’
2. Disable interface 
   1. `ifconfig <interfacename> down`
3. Change mac adress 
   1. `ifconfig <interfacename> hw <what to change> <what you want to change to>`
   2. Example: `ifconfig wlan0 hw ether 00:11:22:33:44:55`
4. Enable interface 
   1. `ifconfig <interfacename> up`

MAC address will reset on a reboot, since this change is only done in memory

## Wireless modes
- **Managed mode**: The default mode for a wireless card. It can connect to an access point.
- **Monitor mode**: Used for packet sniffing. It allows you to capture all packets in the air, including those not intended for your device.

Steps to put a wireless card into monitor mode:
```bash
$ ifconfig <interface name>
$ airmon-ng check kill # (for better results, but not necessary)
$ iwconfig <interface name> mode monitor
$ ifconfig <interface name> up
```

## Packet sniffing
Can be done with airodump-ng, which is a packet sniffer that captures packets from a wireless network. It can capture data, beacons, and handshakes.

```bash
$ airodump-ng <interfacename in monitor mode>
```

Here's your list formatted into a more detailed table format:

| Name    | Description                                                      |
| ------- | ---------------------------------------------------------------- |
| BSSID   | Mac address of target network                                    |
| PWR     | Signal strength                                                  |
| Beacons | Frame (Broadcast existence)                                      |
| #Data   | Data packets (IVs, the higher the number, the higher the chance) |
| #/s     | Data packets in the last 10 seconds                              |
| CH      | Channel                                                          |
| MB      | Maximum speed                                                    |
| ENC     | Encryption                                                       |
| Cipher  | Cipher used in the network                                       |
| Auth    | Authentication used                                              |
| ESSID   | Name of wireless network                                         |

Targetted packet sniffing
```bash
$ airodump-ng --bssid <BSSID> -c <channel> -w <output file> <interface>
```

This will also show the connected devices to the network below (STATION)  
Probe = Trying to connect to a network  

The saved `.pcap` file will show URL, chat messages, passwords etc. Since all requests is sent to the router. (But they can be encrypted with WPA2). So, if it were an open network, everything could be seen

## Wiki bands 2.4Ghz & 5Ghz
**Differences**
- 2.4Ghz
  - Longer range
  - Better at passing through walls
  - More interference
  - Slower
- 5Ghz
  - Shorter range
  - Less interference
  - Faster
  - Less devices use it

**Most common WIFI bands are**
* `a` use 5 Ghz frequency only
* `b,g` both use 2.4 Ghz frequency only
* `n` uses 5 and 2.4 Ghz
* `ac` uses frequencies lower than 6 Ghz

Airodump-ng only sniffs for 2.4 Ghz by default. In order to listen for 5Ghz use:
```r
$ airodump-ng --band a <interfacename>
```
Use band `abg` to listen for both 2.4 and 5 Ghz


# Cracking WPA/WPA2 & WEP
## Deauthentication Attacks
Deauth attacks are used to force a client to disconnect from an access point. This can be used to force a handshake to occur, which can be captured and used to crack the password.

**Commands**  
```sh
# 2.4 Ghz
aireplay-ng --deauth <DeauthPackets> -a <NetworkMAC> -c <TargetMAC> <Interface>
# 5 Ghz
aireplay-ng --deauth <DeauthPackets> -a <NetworkMAC> -c <TargetMAC> -d <Interface>
```
1. `<DeauthPackets>` should be a large number like `‘100000’` so the only way to reconnect is by hitting ctrl + c
2. To do this, we are going to pretend to be the client that we want to disconnect by changing our MAC address to the MAC address of that client and tell the router that I want to disconnect from you.
3. Then we are going to pretend to be the router, again, by changing our Mac address to the router's Mac address and tell the client that you requested to be disconnected, so I'm going to disconnect you.
4. If the command fails, you also have to run the airodump-ng against the network at the same time
5. Deauth attacks will not work If the client is connected via an Ethernet cable


## WEP Cracking
WEP is an outdated security protocol that is no longer considered secure. It can be cracked in minutes using tools like Aircrack-ng.

### How WEP Works
1.	Client encrypts data using a key
2.	Encrypted packet sent in the air
3.	Router decrypts using the key 

### WEP Weaknesses
1.	IV (Initialization Vector) is too short (24 bits)
2.	Clients reuse IVs
3.	IV + Key is sent in plaintext

### Steps to Crack WEP
* IV’s will repeat on busy networks
* This makes WEP vulnerable to statistical attacks when capturing large number of packets
* Repeated IVs can be used to determine the key stream and break the encryption


1. Put your wireless card in monitor mode.
   1. `airmon-ng start <interface>`
2. Identify the target network and capture a large number of packets.
   1. `airodump-ng <interface>`
3. Use aircrack-ng to analyze the captured packets and crack the key.
   1. `aircrack-ng -a 1 -b <BSSID> -e <ESSID> <capture file>`
   2. But if for some reason there is not an ascii representation, you just have to remove the colons from the key, and then use it as the network password. 41:73:32:33:70 -> 4173323370

But there can be problem such as the network is not busy enough. For this you can force the AP to generate more IVs by creating a Fake Authentication request. This will make the AP think that you are a client and start sending IVs.

### Fake Authentication (1/2)
Associate with the AP before launching the attack so we can inject packets into the network, and thereby force the number of data being transmitted.

```r
$ airodump-ng --bssid <id> --channel <number> --write <filename> <interface name>
$ aireplay-ng --fakeauth 0 -a <target_mac> -h <mac_wireless adapter (‘-‘ to ‘:’)>  <interface name>
```
* Note: `ether` changes to `unspec` in monitor mode 
* Note: Change minuses to colons in the mac address
* 0 = We are only doing the attack once
* AUTH should change to OPN, and a new associate to the network should also be shown 

### Fake Authentication (2/2)
Now that we have associated with our target network, we can start communicating with it, and it won't ignore us. So now we can go and start injecting packets into the traffic to force the access point to generate new packets with new IVs.

1.	Wait for an ARP packet
2.	Capture it, and replay it (retransmit it)
3.	This causes the AP to produce another packet with a new IV
4.	Keep doing this till we have enough IVs to crack the key

```r
$ aireplay-ng --fakeauth 0 -a <target_mac> -h <mac_wireless adapter (‘-‘ to ‘:’)>  <interface name>
$ aireplay-ng --arpreplay -b <target_mac> -h <mac_wireless adapter (‘-‘ to ‘:’)>  <interface name>
$ aircrack-ng <file_name>
```

## WPA/WPA2 Cracking
WPA/WPA2 is much more secure than WEP, but it can still be cracked using a dictionary attack. The attack is based on capturing the 4-way handshake between the client and the AP.

How WPA/WPA2 Works:
* Both can be cracked using the same methods
* Made to address the issues in WEP
* Much more secure
* Each packet is encrypted using a unique temporary key

### WPS feature
* WPS is a feature that can be used with WPA & WPA2
* Allows clients to connect without the password
* Authentication is done using an 8-digit pin
  * 8 digit is very small
  * We can try all possible pins in relatively short time
  * Then the WPS pin can be used to compute the actual password
* Only works if the router isn’t configured to use PBC (Push Button Authentication)

### Hacking WPA/WPA2 Without a Wordlist
Start by looking if any network has WPS active

```r
$ wash --interface <interface in monitor mode> # If this fails, then it probably uses PBC

# Bruteforce in verbose mode
$ reaver --bssid <target_mac> --channel <channel> --  > -vvv --no-associate

# Fake authentication
$ aireplay-ng --fakeauth 30 -a <target_mac> -h <mac_wireless adapter (‘-‘ to ‘:’)>  <interface name>
```

### Capturing the handshake (If WPS is disabled)
1. Run airodump-ng and save in a file
2. A handshake will then be captured automatically when a new client connects into the network
   1. This can be improved with a deauthentication attack
   2. Run deauth attack to grab handshake
3. use a low number like 4

**Handshake**
* The handshake des not contain data that helps recover the key
* It contains data that can be used to check if a key is valid or not

### Bruteforce the handshake using a wordlist
Wordlist is compared with a MIC (data from the packet), and if a MIC (Message integrity code) is the same, then the password is found.

```r
$ aircrack-ng <handshake file> -w <wordlist>
```
