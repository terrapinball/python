#!/usr/bin/python3
#Author: <put your name here>
#Date:<put todays date here>
#version: 1.0

'''
<insert a description about this program>
'''

import urllib.request

page=urllib.request.urlopen('http://example.org/')
print("The HTML from the website:")
print(page.read().decode('utf8'))