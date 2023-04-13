import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('localhost', 6667))

while True:
    while True:
        data, client_addres = sock.recvfrom(4096)
        print('received "%s"' % data.decode('utf-8'))
        if data:
            print('sending data back client')
            sock.sendto(data, client_addres)
        else:
            print('no more data')
            break
