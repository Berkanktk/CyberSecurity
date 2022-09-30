# IPv6 Addresses
IPv6 is the successor of IPv4. In contrast to IPv4, the IPv6 address is 128 bit long. The prefix identifies the host 
and  network parts. The Internet Assigned Numbers Authority (IANA) is responsible for assigning IPv4 and IPv6 
addresses  and their associated network portions. In the long term, IPv6 is expected to completely replace IPv4, 
which is still predominantly used on the Internet. In principle, however, IPv4 and IPv6 can be made available 
simultaneously (Dual Stack).

IPv6 consistently follows the end-to-end principle and provides publicly accessible IP addresses for any end  
devices without the need for NAT. Consequently, an interface can have multiple IPv6 addresses, and there are special 
IPv6 addresses to which multiple interfaces are assigned.


IPv6 is a protocol with many new features, which also has many other advantages over IPv4:

* Larger address space
* Address self-configuration (SLAAC)
* Multiple IPv6 addresses per interface
* Faster routing
* End-to-end encryption (IPsec)
* Data packages up to 4 GByte

| Features           | IPv4          | IPv6                         |
|--------------------|---------------|------------------------------|
| Bit length         | 32-bit        | 128 bit                      |
| OSI layer          | Network Layer | Network Layer                |
| Adressing range    | ~ 4.3 billion | ~ 340 undecillion            |
| Representation     | Binary        | Hexadecimal                  |
| Prefix notation    | 10.10.10.0/24 | fe80::dd80:b1a9:6687:2d3b/64 |
| Dynamic addressing | DHCP          | SLAAC / DHCPv6               |
| IPsec              | Optional      | Mandatory                    |

There are four different types of IPv6 addresses:

| Type      | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| Unicast   | Addresses for a single interface.                                              |
| Anycast   | Addresses for multiple interfaces, where only one of them receives the packet. |
| Multicast | Addresses for multiple interfaces, where all receive the same packet.          |
| Broadcast | Do not exist and is realized with multicast addresses.                         |

## Hexadecimal System
The hexadecimal system (hex) is used to make the binary representation more readable and understandable. We can only 
show  10 (0-9) states with the decimal system and 2 (0 / 1) with the binary system by using a single character. In 
contrast to the binary and decimal system, we can use the hexadecimal system to show 16 (0-F) states with a single 
character.

| Decimal | Hex | Binary |
|---------|-----|--------|
| 1       | 1   | 0001   |
| 2       | 2   | 0010   |
| 3       | 3   | 0011   |
| 4       | 4   | 0100   |
| 5       | 5   | 0101   |
| 6       | 6   | 0110   |
| 7       | 7   | 0111   |
| 8       | 8   | 1000   |
| 9       | 9   | 1001   |
| 10      | A   | 1010   |
| 11      | B   | 1011   |
| 12      | C   | 1100   |
| 13      | D   | 1101   |
| 14      | E   | 1110   |
| 15      | F   | 1111   |

Let's look at an example with an IPv4, at how the IPv4 address (192.168.12.160) would look in hexadecimal 
representation.

| Representation | 1st Octet | 2nd Octet | 3rd Octet | 4th Octet |
|----------------|-----------|-----------|-----------|-----------|
| Binary         | 1100 0000 | 1010 1000 | 0000 1100 | 1010 0000 |
| Hex            | C0        | A8        | 0C        | A0        |
| Decimal        | 192       | 168       | 12        | 160       |

Because of its length, an IPv6 address is represented in hexadecimal notation. Therefore the 128 bits are divided into 8 
blocks times 16 bits (or 4 hex numbers). All 4 hex numbers are grouped and separated by a colon (:) instead of a 
simple  dot (.) as in IPv4. To simplify the notation, we leave out leading at least 4 zeros in the blocks, and we 
can  replace them with two colons (::).

An IPv6 address can look like this:

* Full IPv6: fe80:0000:0000:0000:dd80:b1a9:6687:2d3b/64
* Short IPv6: fe80::dd80:b1a9:6687:2d3b/64

An IPv6 address consists of two parts:

* Network Prefix (network part)
* Interface Identifier also called Suffix (host part)

The `Network Prefix` identifies the network, subnet, or address range. The `Interface Identifier` is formed from the 
48-bit MAC address of the interface and is converted to a 64-bit address in the 
process.  The default prefix length is /64. However, other typical prefixes are /32, /48, and /56. If we want to use 
our networks, we get a shorter prefix (e.g. /56) than /64 from our provider.

In RFC 5952, the aforementioned IPv6 address notation was defined:

* All alphabetical characters are always written in lower case.
* All leading zeros of a block are always omitted.
* One or more consecutive blocks of 4 zeros (hex) are shortened by two colons (::).
* The shortening to two colons (::) may only be performed once starting from the left.
