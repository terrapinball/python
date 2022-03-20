#!/usr/bin/env python3

import requests

text = requests.get('http://www.msn.com').text
text = text.split("\n")
for line in text:
    if "<a href=\"https" in line:
        link = line.split('"')[1]
        print(link)