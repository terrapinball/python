#!/usr/bin/env python3

# simple ssh client
# code: BHP v2
# comment: owen

import paramiko                                                         # module for implementing ssh

def ssh_command(ip, port, user, passwd, cmd):                           # take user input parameters
    client = paramiko.SSHClient()                                       # initialize ssh client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())        # add host key if haven't connected to
    client.connect(ip, port=port, username=user, password=passwd)       #       server already
    
    _, stdout, stderr = client.exec_command(cmd)                        # _ is stdin, not important 
    output = stdout.readlines() + stderr.readlines()                    
    if output:                                                          # any output, print to console
        print('--- Output ---')
        for line in output:
            print(line.strip())
        
if __name__ == '__main__':
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()                                        # for secure password entry
    
    ip = input('Enter server IP: ') or '192.168.1.203'                  # defaults applied if no input given
    port = input('Enter port or <CR>: ') or 2222                        #
    cmd = input('Enter command or <CR>: ') or 'id'                      #
    ssh_command(ip, port, user, password, cmd)
