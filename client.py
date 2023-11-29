import socket

HOST = ""
PORT = 0

def decode_client_key(key):
    sprtr = key[0]
    tokens = key[1:len(key)-1].split(sprtr)
    port = int(tokens[0] + tokens[len(tokens)-1])
    tokens = tokens[1:len(tokens)-1]
    decoder = tokens[(len(tokens)-1)//2+1:]
    host_tokens = tokens[:(len(tokens)-1)//2+1]
    host = ".".join(host_tokens[int(index)] for index in decoder)
    return host, port

HOST, PORT = decode_client_key(input("Enter in room ID: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ing = input("Enter in password: ")
    s.sendall(ing.encode())
    data = s.recv(1024)
    if data == b"1":
        raise ConnectionRefusedError

print(f"Successfully Connected! Data outputted: {data.decode()}")
