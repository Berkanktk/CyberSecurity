# Tor Network

## Tor

Tor is a free and open-source software for enabling anonymous communication. Tor directs Internet traffic through a free, worldwide, volunteer overlay network consisting of more than seven thousand relays to conceal a user's location and usage from anyone conducting network surveillance or traffic analysis. Using Tor makes it more difficult to trace Internet activity to the user: this includes "visits to Web sites, online posts, instant messages, and other communication forms". Tor's intended use is to protect the personal privacy of its users, as well as their freedom and ability to conduct confidential communication by keeping their Internet activities unmonitored.

In penetration testing, there might be a need to conduct a full-fledged black-box test. This is a form of testing in which security professionals have to deal with such things as firewalls and other mechanisms of restriction on the customer’s side. In this case, the Tor network can be used in order to constantly change IP and DNS addresses and therefore successfully overcome any restrictions.

Run `apt-get install tor` to install/update your Tor packages

Run `service tor start` to start the Tor service

Run `service tor status` to check Tor's availability

Run `service tor stop` to stop the Tor service

## Proxychains

Proxychains - a tool that forces any TCP connection made by any given application to follow through proxy like TOR or any other SOCKS4, SOCKS5 or HTTP(S) proxy.

Proxychains is widely used by pentesters during the reconnaissance stage (For example with nmap).

![Proxy Chains](/Images/Proxy-chains.png/)

Start with running `apt install proxychains` to install/update proxychains tool

Now it's time to configure proxychains to work properly

Run `sudo nano /etc/proxychains.conf` to edit the settings. (You can of course use any text editing tool instead of nano)

We can now see, that most of the methods are under comment mark. You can read their description and decide on using one of them in the future. 

**What to uncomment?**

`dynamic_chain` and comment others (simply put '#' to the left). 

Additionally, it is useful to uncomment `proxy_dns` in order to prevent DNS leak.

Apply all the settings.

Now let's check our settings.

Start the TOR service and run proxychains firefox. Usually, you are required to put 'proxychains' command before anything in order to force it to transfer data through Tor.

After the firefox has loaded, check if your IP address has changed with any website that provides such information. Also, try running a test on dnsleaktest.com and see if your DNS address changed too.

NOTE: All other web browser windows should be closed before opening firefox through proxychains!

# Download Tor
Download tor for [Windows & Mac OS](https://www.torproject.org)

Downlaod tor browser for kali

```bash
$ sudo apt install -y tor torbrowser-launcher
$ torbrowser-launcher
```

Change security to level 2 (Safer)