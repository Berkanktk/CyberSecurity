import socket
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Berkanktk \n Port Scanner")
print(ascii_banner)

open_ports = []

ip = str(input("Type the ip address:\n> "))  # 127.0.0.1
port_from = int(input("Start scanning from port\n> "))
port_to = int(input("To port\n> "))
ports = range(port_from, port_to)

print("Started scanning...")


def probe_port(ip, port, result=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result


for port in ports:
    sys.stdout.flush()
    response = probe_port(ip, port)
    if response == 0:
        open_ports.append(port)

if open_ports:
    print("Open Ports are: ")
    print(sorted(open_ports))
else:
    print("Looks like no ports are open :(")
