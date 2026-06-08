import os
import platform
import ipaddress
from urllib import response


def scan_network():
    system_type = platform.system()
    network = input("Enter your network IP Address (e.g., 000.000.000.000/00): ")
    ip_net = ipaddress.ip_network(network, strict=False)

    print(f"Scanning for active devices...")
    for ip in ip_net.hosts():
        ip_str = str(ip)
        params = "-n" if system_type == "Windows" else "-c"

        response = os.system(f"ping {params} 1 -w 100 {ip_str} >nul 2>&1")

        if response == 0:
            print(f"[+] Active: {ip_str}")



if __name__ == "__main__":
    scan_network()