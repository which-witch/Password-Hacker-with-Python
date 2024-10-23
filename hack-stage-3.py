from itertools import product
import re
import socket
import sys

argv = sys.argv

def yield_combination(file):
    with open(file, 'r') as file_lines:
        for line in file_lines:
            if re.match('[a-zA-Z]', line):
                for combination in map(''.join, product(*((ch.upper(), ch.lower()) for ch in line.strip("\n")))):
                    yield combination
            else:
                yield line.strip("\n")

combinations = yield_combination('passwords.txt')

with socket.socket() as client:
    address = argv[1], int(argv[2])
    client.connect(address)

    while True:
        try:
            data = next(combinations)
            client.send(data.encode())
            response = client.recv(1024).decode()
            if response == "Connection success!":
                print(data)
                break
            else:
                continue
        except StopIteration:
            print("All passwords have been attempted!")
            break
            

