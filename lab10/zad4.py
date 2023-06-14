import socket

# create WebSocket Server class
class WebSocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def check_handshake(self, data):
        return data.decode('latin-1').find("Upgrade: websocket") != -1

    def create_handshake_response(self, data):
        response = "HTTP/1.1 101 Switching Protocols\r\n" + \
                   "Upgrade: websocket\r\n" + \
                   "Connection: Upgrade\r\n" + \
                   "Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\r\n" + \
                   "\r\n"
        return response.encode('utf-8')

    def handle_frame(self, data):
        p_len = int(data[1])-128
        if p_len <= 125:
            payload = data[6:]
        elif p_len == 126:
            payload = data[8:]
        else:
            payload = data[14:]
        return payload


    def start(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print("Server is listening on port", self.port)
        while True:
            client, address = self.sock.accept()
            self.handle_client(client, address)

    # handle client
    def handle_client(self, client, address):
        handshake = False
        while True:
            try:
                data = client.recv(10000)
                if data:
                    if self.check_handshake(data) and not handshake:
                        print("Handshake OK")
                        # send handshake response
                        response = self.create_handshake_response(data)
                        client.sendall(response)
                        print("Handshake response sent")
                        continue
                    elif not self.check_handshake(data) and handshake:
                        res = self.handle_frame(data)
                        client.sendall(res.encode('utf-8'))
                        continue
                    else:
                        print("Handshake failed")
                        client.close()
                        return
                else:
                    pass
            except socket.timeout:
                print("Client disconnected")
                client.close()
                return

if __name__ == "__main__":
    server = WebSocketServer('localhost', 5000)
    server.start()