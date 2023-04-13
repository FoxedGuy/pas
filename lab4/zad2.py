import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6666)
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(16).decode('utf-8')
            print('received "%s"' % data)
            if data:
                print('sending data back to client')
                connection.sendall(data.encode('utf-8'))
            else:
                print('no more data from', client_address)
                break

    finally:
        connection.close()