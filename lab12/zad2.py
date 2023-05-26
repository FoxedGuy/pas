import socket
from threading import Thread, Lock


class ClientThread(Thread):
    def __init__(self, connection, address, lock):
        Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.lock = lock

    def run(self):
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            with self.lock:
                with open("log.txt", "a") as f:
                    message = "Received from {}: {}".format(self.address, data.decode("utf-8"))
                    f.write(message+"\n")
            self.connection.send(data)
        self.connection.close()

class Server:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        self.lock = Lock()
        print("Server is listening on port {}".format(port))
        with self.lock:
            with open("log.txt", "a") as f:
                f.write("Server is listening on port {}\n".format(port))

    def run(self):
        try:
            while True:
                connection, address = self.sock.accept()
                message = "Client connected from {}".format(address)
                print(message)
                with self.lock:
                    with open("log.txt", "a") as f:
                        f.write(message+"\n")
                c = ClientThread(connection, address, self.lock)
                c.start()
        except socket.error as e:
            print("Error accepting connection: {}".format(e))


def main():
    server = Server('localhost', 6666)
    server.run()


if __name__ == "__main__":
    main()
