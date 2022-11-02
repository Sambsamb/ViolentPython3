"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/1/2022
https://samsclass.info/124/proj14/VP200.htm
"""

# Connect to the target1.bowneconsulting.com server on port 22020.
# Its banner reveals another port to connect to. The next service reveals a flag

import socket
import re

s = socket.socket()
s.settimeout(1)
port = 22020
s.connect(('target1.bowneconsulting.com', port))
print(f"Testing port {port}")
msg = s.recv(1024).decode()
print(msg)
s.close()
# Testing port 22020
# Knocking Challenge 2 I hid the port number in the message below.
# You have 3 seconds.
# Good luck!
#         Yes, I am a criminal2.  My crime is that of curiosity.  My 222crime is
# that of ju222dging people by what they say and think, not what the22287y look like.
# My crime is that of 22outsmarting you, something t22hat you will never forgive me
# for.
#         I am a hacker, and this is my manifesto.  You may stop this individual,
# but 222you can't s222top us all... after all, we're all 2alike.

num_list = re.findall('\d+', msg)
dedup = [*set(num_list)]
print(f"The parsed port list is {dedup}")
print()
# The parsed port list is ['3', '222', '22253', '22', '2']

for port in dedup:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect(('target1.bowneconsulting.com', int(port)))
        print(f"Testing port {port}")
        msg = s.recv(1024).decode()
        print(msg)
        s.close()
    except socket.error as err:
        print(f"No response on port {port} - {err}")
# No response on port 3 - timed out
# No response on port 222 - timed out
# Testing port 22253
# Good work!  The flag is string-parsing
# Testing port 22
# SSH-2.0-OpenSSH_7.6p1
# No response on port 2 - timed out