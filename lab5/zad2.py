import socket
import random


# generate random number
def generate_random_number():
    return random.randint(0, 100000)


def main():
    random_number = generate_random_number()
    print("Generated random number: {}".format(random_number))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 2913))
    server_socket.listen(1)
    print("Server is listening on port 2913")
    while True:
        connection, address = server_socket.accept()
        print("Connection from {}".format(address))
        try:
            while True:
                # receive data from client
                data = connection.recv(8192)
                if not data:
                    print("Nothing received")
                    break
                data = data.decode('utf-8')
                try:
                    received_number = int(data)
                    print(received_number)
                    if received_number == random_number:
                        connection.send('This is the correct number!'.encode('utf-8'))
                        connection.close()
                        exit()
                    elif received_number > random_number:
                        connection.send('The number is too big'.encode('utf-8'))
                    else:
                        connection.send('The number is too small'.encode('utf-8'))

                except ValueError:
                    connection.send("Received data is not a number".encode('utf-8'))
                    continue
        except ConnectionError as e:
            print("Connection error: {}".format(e))
            continue
        finally:
            connection.close()


if __name__ == '__main__':
    main()
