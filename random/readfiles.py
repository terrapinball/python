#!/usr/bin/python3
#Author: owen
#Date: Wed Oct  6 23:15:45 CEST 2021
#version: 1.0


filename='/Users/owen/Documents/Flatiron/projects/python/example.txt'
fh=open(filename)

for line in fh:
	print(line)

fh.close()