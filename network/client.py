import socket
from threading import Thread

class Client:
    def __init__(self):
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
    
    def start_client(self) -> None:
        """
        Connect to server
        """
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.HOST, self.PORT))
        self.running = True
        send = Thread(target=self.run_client)
        send.start()
    
    def run_client(self) -> None:
        """
        Communicating with server
        """
        try:
            data = self.conn.recv(1024)
            if data == b"1":
                raise ConnectionRefusedError
            print(f"Successfully Connected! Data outputted: {data.decode()}")
        except ConnectionAbortedError:
            pass
    
    def key_decoded(self) -> bool:
        """
        Check if HOST and PORT attributes already have
        values.
        """
        return self._HOST and self._PORT
    
    def close_client(self) -> None:
        self.conn.close()