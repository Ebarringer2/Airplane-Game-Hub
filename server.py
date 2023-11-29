import socket
from threading import Thread
from random import randint, sample

HOST = socket.gethostbyname(socket.gethostname()) 
PORT = randint(0, 65535)
password = b"test"

def create_client_key():
    sprtr = chr(randint(35, 38))
    temp = HOST.split(".")
    sep_host = sample(temp, k=len(temp))
    mess_ip = sprtr.join(part for part in sep_host)
    decoder = sprtr.join(str(sep_host.index(part)) for part in temp)
    del temp, sep_host
    return f"{sprtr}{str(PORT)[:len(str(PORT))//2]}{sprtr}{mess_ip}{sprtr}{decoder}{sprtr}{str(PORT)[len(str(PORT))//2:]}{sprtr}"

print(f"Port created: {PORT} in machine: {HOST}")
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
        process = Thread(target=accept_client, args=(conn, addr))
        process.start()
        
    s.close()
    quit()

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