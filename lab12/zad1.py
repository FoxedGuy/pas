import socket, threading


class ClientThread(threading.Thread):
    def __init__(self,connection):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            self.connection.send(data)
        self.connection.close()


class Server:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print("Server is listening on port {}".format(port))

    def run(self):
        try:
            while True:
                connection, address = self.sock.accept()
                print("Client connected from {}".format(address))
                c = ClientThread(connection)
                c.start()
        except socket.error as e:
            print("Error accepting connection: {}".format(e))


def main():
    server = Server('localhost', 6666)
    server.run()


if __name__ == "__main__":
    main()