import socket
import os
import time
import stat


class Server:
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', self.port))
        self.sock.listen(1)
        self.sock.settimeout(5)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                data = conn.recv(10000).decode()
                print(data)
                if data.startswith("GET"):
                    filename = data.split(" ")[1]
                    if filename == "/":
                        filename = "index.html"
                    try:
                        with open(filename, "rb") as file:
                            res = file.read()
                            conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n" + res)
                            conn.sendall(res)
                    except FileNotFoundError:
                        with open("error.html", "rb") as file:
                            res = file.read()
                            conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n" + res)
                elif data.startswith("POST"):
                    options = data.split(" ")[1]
                    if options != "/":
                        conn.sendall(b"HTTP/1.1 400 Bad request\r\n\r\n")
                        conn.close()
                    data = data.split("\r\n\r\n")[1]
                    print(data)
                    with open("data.txt", "a") as file:
                        file.write(data + "\n")
                    conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n" + res)
                conn.close()
            except socket.timeout:
                pass


if __name__ == "__main__":
    server = Server(8080)
    server.run()