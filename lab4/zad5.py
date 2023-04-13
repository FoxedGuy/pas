import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 6668))

while True:
    data, client_address = sock.recvfrom(4096)
    print(client_address)
    if data:
        print('received "%s"' % data.decode('utf-8'))
        # get hostname by ip
        hostname = socket.gethostbyaddr(data.decode('utf-8'))
        sock.sendto(hostname[0].encode('utf-8'), client_address)
    else:
        print('no more data')
        break
