# echo-server.py

import socket
import random

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 8888  # Port to listen on (non-privileged ports are > 1023)
password = b"test"

print(f"Port created: {PORT}")
clients_connected = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        clients_connected += 1
        if not data:
            break
        if data.decode() == password.decode():
            conn.sendall(b"Connection Allowed")
        else:
            conn.sendall(b"1")
    if clients_connected >= 5:
        s.close()
        break