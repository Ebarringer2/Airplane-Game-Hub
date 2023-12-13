import socket
from threading import Thread
from random import randint, sample
from typing import Union, List
from atexit import register
from json import dumps, loads

class Server:
    def __init__(self, password: Union[str, None] = None,
                 host: str = socket.gethostbyname(socket.gethostname()),
                 port: int = randint(0, 65535), max_connections: int = 200):
        self.__HOST: str = host
        self.__PORT: int = port
        self.__KEY = None
        if password is None:
            self.__PASSWORD = ""
        else:
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
        register(self.close_server)
        self.SERVER.bind((self.HOST, self.PORT))
        self.running = True
        if not self.KEY:
            self.create_client_key()
        print(f"Started server...\nKEY: {self.KEY}")
        listen = Thread(target=self.run_server)
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
                if data.decode().strip() == self.__PASSWORD:
                    conn.sendall(b"Connection Allowed")
                else:
                    conn.sendall(b"1")
        except ConnectionResetError:
            print(f"Connection closed with {addr}. Updated # of clients connected: {self.clients_conn-1}")
        self.clients_conn -= 1
        print(f"Current # of clients connected: {self.clients_conn}")
    
    def close_server(self):
        print("Closing server")
        self.SERVER.close()

class TicTacToeServer(Server):
    def __init__(self, tictactoe):
        super().__init__(max_connections=1)
        self.board = {
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : None,
            7 : None,
            8 : None,
            9 : None
        }
        self.tic = "cross"
        self.clients_connected = False
        self.listening = False
        self.sending = True
        self.grid = tictactoe
    
    def accept_client(self, conn: socket, addr) -> None:
        self.clients_connected = True
        try:
            with conn:
                self.clients_conn += 1
                while True:
                    if self.listening:
                        self.grid.on_turn = False
                        try:
                            data = loads(self.conn.recv(1024))
                            for place, value in data.items():
                                self.board[place] = value
                            print(data)
                            self.listening = False
                            self.sending = True
                        except:
                            data = None
                    if self.do_send():
                        self.grid.on_turn = True
                        data = self.board
                        conn.sendall(dumps(data).encode())
                        self.listening = True
                        self.sending = False
        except (ConnectionRefusedError, ConnectionAbortedError):
            pass
        self.clients_conn -= 1
        self.clients_connected = False
    
    def read_board(self, board: List[int]):
        """
        board is a list of positions on the board.
        each position can have three possible
        values: None, cross, and circle.
        Example:
        [None, None, None,
        cross, None, circle,
        None, cross, circle]
        """
        for _ in range(9):
            self.board[_+1] = board[_]

    def do_send(self) -> bool:
        return self.grid.check_changed() and self.sending