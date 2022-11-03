"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/2/2022
https://samsclass.info/124/proj14/VP220.htm
"""

# In a Web browser, open this page:
# https://samsclass.info/124/proj14/VP220-2.php
# Monitor the DNS requests. After a while you'll find the flag.

from scapy.all import *

def findDNS(p):
    if p.haslayer(DNS):
        # Avoid "IndexError: Layer [IP] not found"
        try:
            msg = (p[IP].src, p[DNS].summary())
        except:
            msg = print(p[DNS].summary())
        if not isinstance(msg, type(None)):
            print(msg)
            print(type(msg))  # Only prints when <msg = (p[IP].src, p[DNS].summary())> is invoked as in:
            # ('10.0.0.176', 'DNS Qry "b\'_CC32E753._sub._googlecast._tcp.local.\'" ')
            # <class 'tuple'>
            if 'flag' in str(msg):
                raise Exception(msg)  # Won't exit!?
        if 'flag' in str(msg):
            raise Exception(msg)  # Won't exit!?

sniff(prn=findDNS)

# DNS Qry "b'dk1ngonqdm-flag-is-poorlyhidden-ak0kjpzezzsdzmjrh2.samsclass.info.'"