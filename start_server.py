import game.network.server
import atexit



server = game.network.server.Server(password="test")
server.start_server()


def close_server():
    global server
    server.close_server()
    print("Closed server...")

atexit.register(close_server)