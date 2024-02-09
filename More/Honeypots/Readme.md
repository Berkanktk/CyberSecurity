# Honeypot
Can be added using **PenTBox** on Kali Linux.

```bash
vantwinkle@aocday13:~/pentbox/pentbox-1.8$ sudo ./pentbox.rb
           
PenTBox 1.8
           
------- Menu         ruby2.7.0 @ x86_64-linux-gnu
1 - Cryptography tools
2 - Network tools
3 - Web
           
----Redacted---
-> 2
           
1 - Net DoS Tester
2 - TCP port scanner
3 - Honeypot
--- Redacted---
```

```bash
1- Fast Auto Configuration
2- Manual Configuration
           
-> 2
           
Insert port to Open
-> 8080
Insert false message to show
-> Family is gone for a week.
           
---Redacted---
HONEYPOT ACTIVATED ON PORT 8080

INTRUSION ATTEMPT DETECTED! from 10.0.2.5:49852 (2023-11-01 22:56:15 +0000)
```