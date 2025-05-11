from ipaddress import *

net = ip_network("172.16.128.0/255.255.192.0", 0)

k = 0
for ip in net:
    b = f"{ip:b}"
    if b.count("1") % 2 != 0:
        k += 1

print(k)

"""
8192
"""
