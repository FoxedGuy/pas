import socket

mail_from = ""
rcpt_to = ""
data = ""
write_data = False


def parse(message):
    global mail_from, rcpt_to, data, write_data
    print("Recived: " + message)
    if message == "HELO":
        return "OK"
    elif message.startswith("MAIL FROM:"):
        mail_from = message.split(" ")[2]
        return "250 OK"
    elif message.startswith("RCPT TO:"):
        rcpt_to = message.split(" ")[2]
        return "250 OK"
    elif message == "DATA":
        write_data = True
        return "354 Zakończ wiadomość znakiem '.' w osobnej linii"
    elif write_data and message != ".":
        data += message
        return ""
    elif write_data and message == ".":
        print("hello")
        write_data = False
        return data
    elif message == "QUIT":
        return "221 Service closing transmission channelw"

    return "500 Syntax error: command unrecognized"


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('localhost', 2910))
        sock.listen()
        print("Listening on port 2911...")
        while True:
            conn, address = sock.accept()
            with conn:
                print('Connected by', address)
                conn.sendall("Service Ready\n".encode('utf-8'))
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    res = parse(data.decode('utf-8'))
                    conn.sendall(res.encode('utf-8'))


if __name__ == "__main__":
    main()