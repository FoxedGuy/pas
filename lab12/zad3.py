import socket
import  threading
import random


class ClientThread(threading.Thread):
    def __init__(self,connection, random_number):
        threading.Thread.__init__(self)
        self.connection = connection
        self.random_number = random_number

    def run(self):
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            try:
                number = int(data.decode("utf-8"))
                if number == self.random_number:
                    data = "You guessed correctly, closing connection"
                    self.connection.send(data.encode("utf-8"))
                    self.connection.close()
                    continue
                elif number < self.random_number:
                    data = "Your number is too small"
                else:
                    data = "Your number is too big"
                self.connection.send(data.encode("utf-8"))
            except ValueError:
                data = "You didn't enter a number"
                self.connection.send(data.encode("utf-8"))
        self.connection.close()


class Server:
    def __init__(self, host, port):
        self.random_number = random.randint(1, 5000)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print("Server is listening on port {}".format(port))

    def run(self):
        try:
            while True:
                connection, address = self.sock.accept()
                print("Client connected from {}".format(address))
                c = ClientThread(connection, self.random_number)
                c.start()
        except socket.error as e:
            print("Error accepting connection: {}".format(e))


def main():
    server = Server('localhost', 6666)
    server.run()


if __name__ == "__main__":
    main()