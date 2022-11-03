"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/2/2022
https://samsclass.info/124/proj14/VP220.htm
"""

# In a Web browser, open this page:
# https://samsclass.info/124/proj14/VP220-1.php
# Monitor the DNS requests. After a while you'll find the flag

from scapy.all import *
import sys

def findDNS(p):
    if p.haslayer(DNS):
        # Avoid "IndexError: Layer [IP] not found"
        try:
            msg = (p[IP].src, p[DNS].summary())
        except:
            msg = print(p[DNS].summary())
        # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        if not isinstance(msg, type(None)):
            print(msg)
            print(type(msg))  # Won't print!?
            if 'flag' in str(msg):
                raise Exception(msg)  # Won't exit!?
        if 'flag' in str(msg):
            raise Exception(msg)  # Won't exit!?

sniff(prn=findDNS)

# DNS Qry "b'the-flag-is-dnsconfusion.samsclass.info.'"
