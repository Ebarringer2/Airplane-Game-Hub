import network.server
import atexit



server = network.server.Server(password="test")
server.start_server()


def close_server():
    global server
    server.close_server()
    print("Closed server...")

atexit.register(close_server)