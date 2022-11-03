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


# Ether / IPv6 / UDP / DNS Qry "b'server356.samsclass.info.'"
# ###[ Ethernet ]###
#   dst       = fc:51:a4:00:c4:0d
#   src       = 30:65:ec:8d:37:d4
#   type      = IPv6
# ###[ IPv6 ]###
#      version   = 6
#      tc        = 0
#      fl        = 874015
#      plen      = 50
#      nh        = UDP
#      hlim      = 64
#      src       = 2601:82:4380:63a0:f010:7cc5:916f:e7e8
#      dst       = 2001:558:feed::1
# ###[ UDP ]###
#         sport     = 49306
#         dport     = domain
#         len       = 50
#         chksum    = 0x190d
# ###[ DNS ]###
#            id        = 8179
#            qr        = 0
#            opcode    = QUERY
#            aa        = 0
#            tc        = 0
#            rd        = 1
#            ra        = 0
#            z         = 0
#            ad        = 0
#            cd        = 0
#            rcode     = ok
#            qdcount   = 1
#            ancount   = 0
#            nscount   = 0
#            arcount   = 0
#            \qd        \
#             |###[ DNS Question Record ]###
#             |  qname     = 'server356.samsclass.info.'
#             |  qtype     = A
#             |  qclass    = IN
#            an        = None
#            ns        = None
#            ar        = None
#
# None