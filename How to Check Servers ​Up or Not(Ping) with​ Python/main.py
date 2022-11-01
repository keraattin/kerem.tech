#/usr/bin/env python3

# Libraries
from scapy.all import sr1,IP,ICMP

# Global Values
TARGETS = ['192.168.1.1','192.168.1.2']

# Ping command
def ping(host):
    timeout = 3 # Set Timeout(Second)
    icmp_pkg = IP(dst=host)/ICMP() # Create ICMP Package
    response = sr1(
        icmp_pkg,       # Package
        verbose=False,  # Verbose set False
        timeout=timeout # Set Timeout
    )
    if response is None or "host-unreachable" in str(response):
        return False
    else:
        return True

for target in TARGETS:
    print(target + "->" + str(ping(target)))
