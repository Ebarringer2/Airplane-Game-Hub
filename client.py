# echo-client.py

import socket

HOST = ""  # The server's hostname or IP address
PORT = 0  # The port used by the server

def decode_client_key(key):
    global HOST
    global PORT
    pair = key.split("*$()W##$")
    HOST = pair[1]
    PORT = int(pair[0])

decode_client_key(input("Enter in room ID: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ing = input("Enter in password: ")
    s.sendall(ing.encode())
    data = s.recv(1024)
    if data == b"1":
        raise ConnectionRefusedError

print(f"Successfully Connected! Data outputted: {data}")
