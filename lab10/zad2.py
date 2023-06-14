import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 10000))
    sock.settimeout(0.5)
    sock.sendall(("GET /.ws HTTP/1.1\r\nHost: localhost\r\n" +
                 "Upgrade: websocket\r\n" +
                 "Connection: Upgrade\r\n" +
                 "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n" +
                 "Sec-WebSocket-Version: 13\r\n\r\n").encode('utf-8'))
    data = sock.recv(10000)

    print(data.decode('latin-1'))
    msg = "hello world!"

    frame = bytearray()
    frame.append(int('10000001', 2))
    frame.append(128+len(msg))  # payload length

    for i in range(4):
        frame.append(int('00000000', 2))  # mask-key
    frame.extend(msg.encode())

    sock.sendall(frame)
    try:
        while True:
            data = sock.recv(10000)
            print(data)
    except socket.timeout:
        sock.close()
