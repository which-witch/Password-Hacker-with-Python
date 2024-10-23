import itertools
from string import ascii_lowercase, digits
import socket
import sys

argv = sys.argv

def connect_server():
    address = argv[1], int(argv[2])
    client.connect(address)


def try_password():
    length = 1
    while True:
        current_try = itertools.product(ascii_lowercase + digits, repeat=length)
        for passwd in current_try:
            data = "".join(passwd)
            message = data.encode()
            client.send(message)
            response = client.recv(1024).decode()
            if response == "Connection success!":
                print(data)
                break
        else:
            length += 1
            continue
        break


with socket.socket() as client:
    connect_server()
    try_password()
