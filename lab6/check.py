import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('localhost', 2910))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    sock.sendall("HELO".encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    while True:
        data = input()
        sock.sendall(data.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
