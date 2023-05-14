import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost', 5000))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        while True:
            message = input()
            sock.sendall(message.encode('utf-8'))
            data = sock.recv(1024)
            print(data.decode('utf-8'))


if __name__ == "__main__":
    main()