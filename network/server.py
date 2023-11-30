import socket
from threading import Thread
from random import randint, sample

class Server:
    def __init__(self, password: str = None,
                 host: str = socket.gethostbyname(socket.gethostname()),
                 port: int = randint(0, 65535), max_connections: int = 200):
        self.__HOST: str = host
        self.__PORT: int = port
        self.__KEY = None
        self.__PASSWORD = password
        self.running: bool = False
        self.__SERVER: socket.socket = None
        self.max_conn = max_connections
        self.clients_conn = 0

    @property
    def HOST(self):
        return self.__HOST

    @HOST.setter
    def HOST(self, HOST: str):
        if not self.HOST:
            self.__HOST: str = HOST
        else:
            raise AttributeError(f"Attribute already assigned to value")

    @property
    def PORT(self):
        return self.__PORT

    @PORT.setter
    def PORT(self, PORT: int):
        if not self.PORT:
            self.__PORT: int = PORT
        else:
            raise AttributeError(f"Attribute already assigned to value")
    
    @property
    def KEY(self):
        return self.__KEY
    
    @KEY.setter
    def KEY(self, KEY: str):
        if not self.KEY:
            self.__KEY: int = KEY
        else:
            raise AttributeError(f"Attribute already assigned to value")
    
    @property
    def PASSWORD(self):
        return self.__PASSWORD
    
    @property
    def SERVER(self):
        return self.__SERVER

    @SERVER.setter
    def SERVER(self, SERVER: socket.socket):
        if not self.SERVER:
            self.__SERVER: socket.socket = SERVER
        else:
            raise AttributeError(f"Attribute already assigned to value")

    def create_client_key(self) -> None:
        """
        Create key for client to connect to server
        """
        sprtr = chr(randint(35, 38))
        temp = self.HOST.split(".")
        sep_host = sample(temp, k=len(temp))
        mess_ip = sprtr.join(part for part in sep_host)
        decoder = sprtr.join(str(sep_host.index(part)) for part in temp)
        del temp, sep_host
        self.KEY = f"{sprtr}{str(self.PORT)[:len(str(self.PORT))//2]}{sprtr}{mess_ip}{sprtr}{decoder}{sprtr}{str(self.PORT)[len(str(self.PORT))//2:]}{sprtr}"
    
    def start_server(self) -> None:
        """
        Start the server main loop
        """
        self.SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER.bind((self.HOST, self.PORT))
        self.running = True
        if not self.KEY:
            self.create_client_key()
        print(f"Started server...\nKEY: {self.KEY}")
        listen = Thread(target=self.run_server())
        listen.start()
    
    def run_server(self) -> None:
        """
        Continuously check for connections
        """
        while self.clients_conn < self.max_conn:
            self.SERVER.listen()
            conn, addr = self.SERVER.accept()
            process = Thread(target=self.accept_client, args=(conn, addr))
            process.start()
    
    def accept_client(self, conn, addr) -> None:
        """
        Handle different clients
        """
        try:
            with conn:
                self.clients_conn += 1
                print(f"Current # of clients connected: {self.clients_conn}")
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data.decode() == self.PASSWORD.decode():
                    conn.sendall(b"Connection Allowed")
                else:
                    conn.sendall(b"1")
        except ConnectionResetError:
            print(f"Connection closed with {addr}. Updated # of clients connected: {self.clients_conn-1}")
        self.clients_conn -= 1
        print(f"Current # of clients connected: {self.clients_conn}")
    
    def close_server(self):
        self.SERVER.close()