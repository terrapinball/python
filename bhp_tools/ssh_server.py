#!/usr/bin/env python3

# simple ssh server
# code: BHP 2e
# comments: owen

import os
import paramiko                                                         # to setup encryption for ssh session
import socket
import sys                                                              # supports windows/unix
import threading

CWD = os.path.dirname(os.path.realpath(__file__))                       # current working directory
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, '.test_rsa.key'))  # option to use hostkey for auth

class Server (paramiko.ServerInterface):                                # start multithreaded application
    def __init__(self):
        self.event = threading.Event()
    
    def check_channel_request(self, kind, chanid):                      # check channel request, show
        if kind == 'session':                                           # success or fail
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    
    def check_auth_password(self, username, password):
        if (username == 'tim') and (password == 'sekret'):              # hard coded creds :(
            return paramiko.AUTH_SUCCESSFUL                             # practice for example only

if __name__ == '__main__':
    server = '192.168.0.12'
    ssh_port = 2222
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # try to bind server socket to
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)      # new connection
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[.] Listening for connection ...')
        client, addr = sock.accept()
    except Exception as e:
        print('[-] Listen failed: ' + str(e))
        sys.exit(1)
    else:
        print(f'[+] Connected to {addr}')
        
    bhSession = paramiko.Transport(client)                              # start secured connection
    bhSession.add_server_key(HOSTKEY)
    server = Server()
    bhSession.start_server(server=server)
    
    chan = bhSession.accept(20)
    if chan is None:
        print('*** No channel.')
        sys.exit(1)
        
    print('[+] Authenticated')
    print(chan.recv(1024).decode())
    chan.send('Welcome to bh_ssh')
    try:
        while True:
            command = input("Enter command: ")                          # wait for commands
            if command != "exit":
                chan.send(command)
                r = chan.recv(8192)
                print(r.decode())
            else:
                chan.send('exit')
                print('exiting')
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()