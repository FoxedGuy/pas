import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 2900))
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(4096)
            if len(data) > 20:
                connection.sendall("Wiadomość jest za długa".encode('utf-8'))
                continue
            else:
                print('received "%s"' % data.decode('utf-8'))
                print('sending data back to the client')
                connection.sendall(data)
    finally:
        connection.close()