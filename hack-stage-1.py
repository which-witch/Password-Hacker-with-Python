import socket
import sys

argv = sys.argv

address = argv[1], int(argv[2])
message = argv[3]

client_socket = socket.socket()
client_socket.connect(address)
client_socket.send(message.encode())

response = client_socket.recv(1024)
response = response.decode()
print(response)
client_socket.close()
