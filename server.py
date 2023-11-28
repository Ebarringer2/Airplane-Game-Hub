# echo-server.py

import socket
import threading
import sys

HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)
password = b"test"

def create_client_key():
    global PORT, HOST
    return str(PORT) + "*$()W##$" + str(HOST)

print(f"Port created: {PORT} from Host: {HOST}")
clients_connected = 0
max_traffic = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print(create_client_key())

def run_server():
    global clients_connected
    global s
    
    while clients_connected < max_traffic:
        s.listen()
        conn, addr = s.accept()
        process = threading.Thread(target=accept_client, args=(conn, addr))
        process.start()
        
    s.close()
    sys.exit()

def accept_client(conn, addr):
    global clients_connected
    global s
    
    try:
        with conn:
            clients_connected += 1
            print(f"Current # of clients connected: {clients_connected}")
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            if data.decode() == password.decode():
                conn.sendall(b"Connection Allowed")
            else:
                conn.sendall(b"1")
    except ConnectionResetError:
        print(f"Connection closed with {addr}. Current # of clients connected: {clients_connected}")
    clients_connected -= 1
    print(f"Current # of clients connected: {clients_connected}")

run_server()