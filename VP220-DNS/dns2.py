"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/2/2022
https://samsclass.info/124/proj14/VP220.htm
"""

from scapy.all import *


def findDNS(p):
    if p.haslayer(DNS):
        print(p[IP].src, p[DNS].summary())


sniff(prn=findDNS)


# Traceback (most recent call last):
#   File "D:\BU\OneDrive - SmartWebApps\Documents\edu\FHSU\2022 Fall\INF 601G - Advanced Python\ViolentPython3\VP220-DNS\dns2.py", line 18, in <module>
#     sniff(prn=findDNS)
#   File "D:\BU\OneDrive - SmartWebApps\Documents\edu\FHSU\2022 Fall\INF 601G - Advanced Python\ViolentPython3\venv\lib\site-packages\scapy\sendrecv.py", line 1263, in sniff
#     sniffer._run(*args, **kwargs)
#   File "D:\BU\OneDrive - SmartWebApps\Documents\edu\FHSU\2022 Fall\INF 601G - Advanced Python\ViolentPython3\venv\lib\site-packages\scapy\sendrecv.py", line 1210, in _run
#     session.on_packet_received(p)
#   File "D:\BU\OneDrive - SmartWebApps\Documents\edu\FHSU\2022 Fall\INF 601G - Advanced Python\ViolentPython3\venv\lib\site-packages\scapy\sessions.py", line 108, in on_packet_received
#     result = self.prn(pkt)
#   File "D:\BU\OneDrive - SmartWebApps\Documents\edu\FHSU\2022 Fall\INF 601G - Advanced Python\ViolentPython3\VP220-DNS\dns2.py", line 15, in findDNS
#     print(p[IP].src, p[DNS].summary())
#   File "D:\BU\OneDrive - SmartWebApps\Documents\edu\FHSU\2022 Fall\INF 601G - Advanced Python\ViolentPython3\venv\lib\site-packages\scapy\packet.py", line 1344, in __getitem__
#     raise IndexError("Layer [%s] not found" % name)
# IndexError: Layer [IP] not found