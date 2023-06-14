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
    msg = "test looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo" \
          "ooooooooooooooooooooooooooooooooooong message"

    print(len(msg))
    # create websocket frame
    frame = bytearray()
    frame.append(int('10000001', 2))
    if len(msg) < 126:
        frame.append(128+len(msg))
    elif len(msg) == 126:
        frame.append(128+126)
        frame.append(len(msg) >> 8)
        frame.append(len(msg) & 0xff)
    else:
        frame.append(128+127)
        for i in range(8):
            frame.append(len(msg) >> (7 - i) * 8 & 0xff)


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
