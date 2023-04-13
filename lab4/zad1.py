import socket
import sys
from datetime import datetime


def get_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 6666)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(16).decode('utf-8')
            print('received "%s"' % data)
            if data:
                print('sending time to client')
                connection.sendall(get_time().encode('utf-8'))
            else:
                print('no more data from', client_address)
                break

    finally:
        connection.close()
