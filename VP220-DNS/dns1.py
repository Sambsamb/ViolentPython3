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
        print(p.summary())
        print(p.display())


sniff(prn=findDNS)


