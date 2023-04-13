import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('localhost', 6668))

while True:
    data, client_address = sock.recvfrom(4096)
    if data:
        print('received "%s"' % data.decode('utf-8'))

        # we assume that the data is in the form of "number operator number"
        all = data.decode('utf-8').split(' ')
        if all[1] == "+":
            result = int(all[0]) + int(all[2])
        elif all[1] == "-":
            result = int(all[0]) - int(all[2])
        elif all[1] == "*":
            result = int(all[0]) * int(all[2])
        elif all[1] == "/":
            try:
                result = int(all[0]) / int(all[2])
            except ZeroDivisionError:
                result = "Cannot divide by zero"
        else:
            result = "Wrong operator"
        sock.sendto(str(result).encode('utf-8'), client_address)