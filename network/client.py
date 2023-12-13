import socket
from threading import Thread
from atexit import register
from json import loads, dumps
from typing import List

class Client:
    def __init__(self):
        """
        - HOST: server ip
        - PORT: server port
        - conn: socket connection
        - running: is client connected
        """
        self._HOST: str = ""
        self._PORT: int = 0
        self.conn: socket.socket = None
        self.running: bool = False

    @property
    def HOST(self):
        return self._HOST

    @HOST.setter
    def HOST(self, HOST):
        if not self.HOST:
            self._HOST = HOST
        else:
            raise AttributeError(f"Attribute already assigned to value")

    @property
    def PORT(self):
        return self._PORT

    @PORT.setter
    def PORT(self, PORT):
        if not self.PORT:
            self._PORT = PORT
        else:
            raise AttributeError(f"Attribute already assigned to value")
    
    def decode_client_key(self, text) -> None:
        """
        Initialize client host and port
        """
        try:
            sprtr = text[0]
            tokens = text[1:len(text)-1].split(sprtr)
            self.PORT = int(tokens[0] + tokens[len(tokens)-1])
            tokens = tokens[1:len(tokens)-1]
            decoder = tokens[(len(tokens)-1)//2+1:]
            host_tokens = tokens[:(len(tokens)-1)//2+1]
            self.HOST = ".".join(host_tokens[int(index)] for index in decoder)
        except ValueError:
            print("Invalid key!")
        return "test"
    
    def start_client(self) -> int:
        """
        Connect to server
        """
        try:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            register(self.close_client)
            self.conn.connect((self.HOST, self.PORT))
            self.running = True
            send = Thread(target=self.run_client)
            send.start()
        except ConnectionRefusedError:
            return -1
        return 0
    
    def run_client(self) -> None:
        """
        Receive from server
        """
        try:
            data = self.conn.recv(1024)
            if data == b"1":
                raise ConnectionRefusedError
            print(f"Successfully Connected! Data outputted: {data.decode()}")
        except (ConnectionAbortedError, OSError):
            pass
    
    def send_data(self, text: str) -> None:
        """
        Send to server
        
        - data: to be encoded and converted to bytes
        """
        try:
            self.conn.send(text.encode())
        except (ConnectionAbortedError, ConnectionRefusedError):
            print("Couldn't send data")
        return "send data"
    
    def key_decoded(self) -> bool:
        """
        Check if HOST and PORT attributes already have
        values.
        """
        return self._HOST and self._PORT
    
    def close_client(self) -> None:
        self.conn.close()

class TicTacToeClient(Client):
    def __init__(self, tictactoe):
        super().__init__()
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
        self.listening = True
        self.sending = False
        self.grid = tictactoe
    
    def run_client(self) -> None:
        try:
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
                    self.conn.sendall(dumps(data).encode())
                    self.listening = True
                    self.sending = False
        except (ConnectionAbortedError, ConnectionRefusedError):
            raise ConnectionAbortedError
            
    
    def send_data(self, data : dict) -> None:
        try:
            self.conn.sendall(dumps(data).encode())
        except (ConnectionAbortedError, ConnectionRefusedError):
            raise ConnectionAbortedError
    
    def read_board(self, board: List[int]):
        """
        board is a list of positions on the board.
        each position can have three values: None,
        cross, and circle.
        Example:
        [None, None, None,
        cross, None, circle,
        None, cross, circle]
        """
        for _ in range(9):
            self.board[_+1] = board[_]
    
    def do_send(self) -> bool:
        return self.grid.check_changed() and self.sending