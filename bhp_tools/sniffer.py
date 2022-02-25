#!/usr/bin/env python3

# simple packet sniffer
# code: BHP v2
# comments: owen

import socket
import os

HOST = '192.168.0.12'                                                            # host machine IP

def main():
    if os.name == 'nt':                                                         # if windows
        socket_protocol = socket.IPPROTO_IP
    else:                                                                       # if linux
        socket_protocol = socket.IPPROTO_ICMP
        
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))                                                     # sniff all ports
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)                 # include IP headers
    
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)                      # turns on promiscuous mode on nic
        
    print(sniffer.recvfrom(65565))                                              # print raw packet hex
    
    if os.name == 'nt':                                                         # turn off after
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        
if __name__ == '__main__':
    main()

