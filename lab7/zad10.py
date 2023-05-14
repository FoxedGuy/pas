import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 5000))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        message = "USER user2"
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        message = "PASS password2"
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        message = "LIST"
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(1024)
        data = data.decode('utf-8')
        data = data.split('\n')
        for line in data[1:]:
            message = "RETR " + line.split(' ')[0]
            sock.sendall(message.encode('utf-8'))
            data = sock.recv(1024)
            print(data.decode('utf-8'))