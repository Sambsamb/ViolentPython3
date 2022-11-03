"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/2/2022
https://samsclass.info/124/proj14/VP210.htm
"""

# Make a Python script that logs in to this page:
# https://bowneconsultingcontent.com/BASIC0/index.php
# with these parameters:
# Username: admin0
# Password: password
# User-Agent: python
# The server will reply with a flag.
# Hint: use requests.
# Hint: First repeat VP 210.3 using "requests".

import requests

# Input
url = 'https://bowneconsultingcontent.com/BASIC0/index.php'
username = 'admin0'
password = 'password'

# Process, output
headers = {'User-Agent': 'python'}
r = requests.get(url, auth=(username, password), headers=headers)
print(r.text)

# Congratulations! The flag is easy-request
