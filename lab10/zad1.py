import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 10000))
    sock.sendall(("GET /.ws HTTP/1.1\r\nHost: localhost\r\n" +
                 "Upgrade: websocket\r\n" +
                 "Connection: Upgrade\r\n" +
                 "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n" +
                 "Sec-WebSocket-Version: 13\r\n\r\n").encode('utf-8'))
    data = sock.recv(10000)

    print(data.decode('latin-1'))
