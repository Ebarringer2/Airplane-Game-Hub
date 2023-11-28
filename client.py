# echo-client.py

import socket

HOST = socket.gethostbyname(socket.gethostname())  # The server's hostname or IP address
PORT = 5000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ing = input("Enter in password: ")
    s.sendall(ing.encode())
    data = s.recv(1024)
    if data == b"1":
        raise ConnectionRefusedError

print(f"Successfully Connected! Data outputted: {data}")
