"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP200.htm
"""

# Find a service running on the target1.bowneconsulting.com server on a port between 21000 and 21030.
# Its banner reveals a flag.

import socket

for port in range(21000, 21031):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect(('target1.bowneconsulting.com', port))
        print(f"Testing port {port}")
        msg = s.recv(1024).decode()
        print(msg)
        s.close()
        break
    except socket.error as err:
        print(f"No response on port {port} - {err}")

# Testing port 21011
# Good!  The flag is banner-grabbing