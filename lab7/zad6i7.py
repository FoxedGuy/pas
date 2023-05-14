import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 5000))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        message = "USER user1"
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        message = "PASS password1"
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        message = "STAT"
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))