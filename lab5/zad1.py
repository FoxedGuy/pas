import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("localhost", 2914))
    while True:
        data = input("Enter number: ")
        sock.send(data.encode('utf-8'))
        response = sock.recv(1024)
        print(response.decode('utf-8'))
        if response.decode('utf-8') == "This is the correct number!":
            sock.close()
            break

print("Connection closed")
print("You won!")