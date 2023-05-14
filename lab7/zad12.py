import socket
import sys


class Server:
    POP_OPTIONS = ['USER', 'PASS', 'STAT', 'LIST', 'RETR', 'DELE', 'QUIT']
    SERVER_PORT = 5000
    SERVER_HOST = 'localhost'
    users = []
    temp_user = None
    current_user = None

    def __init__(self):
        # create some users
        self.users.append(User('user1', 'password1'))
        self.users.append(User('user2', 'password2'))

        # create some mails
        self.users[1].create_mail('user1@example.com', 'user2@example.com', 'hello', 'Hello world!')
        self.users[0].create_mail('user2@example.com', 'user1@example.com', 'h2u2', 'Hello to you too!')
        self.users[1].create_mail('user1@example.com', 'user2@example.com', 'największa wiadomość!', 'To jest największa wiadomość! Jest się z czego cieszyć!')

    def message_handler(self, message: str):
        message = message.replace("\r\n", "")
        try:
            command, arg = message.split()
        except ValueError:
            command = message
            arg = None
        print(command)
        if command not in self.POP_OPTIONS:
            return "-ERR invalid command\n"
        if command == 'USER':
            for user in self.users:
                if user.login == arg:
                    self.temp_user = user
                    return "+OK user found\n"
            return "-ERR user not found\n"
        elif command == 'PASS':
            if self.temp_user is None:
                return "-ERR no user specified\n"
            if self.temp_user.password == arg:
                self.current_user = self.temp_user
                self.temp_user = None
                return "+OK logged in\n"
            return "-ERR wrong password\n"
        elif command == 'STAT':
            if self.current_user is None:
                return "-ERR no user logged in\n"
            return "+OK {} {}\n".format(len(self.current_user.mails), sys.getsizeof(self.current_user.mails))
        elif command == 'LIST':
            mess = "+OK List of messages\n"
            for mail in self.current_user.mails:
                mess += "{} {}\n".format(mail['id'], sys.getsizeof(mail))
            return mess
        elif command == 'RETR':
            if arg is None:
                return "-ERR no message specified\n"
            try:
                id_ = int(arg)
            except ValueError:
                return "-ERR invalid message id\n"
            if id_ > len(self.current_user.mails):
                return "-ERR message not found\n"
            mail_r = self.current_user.get_mail(id_)
            return "+OK Message follows:\n" + mail_r
        elif command == 'DELE':
            if arg is None:
                return "-ERR no message specified\n"
            try:
                id_ = int(arg)
            except ValueError:
                return "-ERR invalid message id\n"
            if id_ > len(self.current_user.mails):
                return "-ERR message not found\n"
            self.current_user.mails.pop(id_-1)
            return "+OK message deleted\n"
        elif command == 'QUIT':
            self.current_user = None
            return "+OK logging out\n"

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.SERVER_HOST, self.SERVER_PORT))
            sock.listen()
            print("Listening on port {}...".format(self.SERVER_PORT))
            while True:
                conn, address = sock.accept()
                with conn:
                    print('Connected by', address)
                    conn.sendall("+OK POP3 server ready\n".encode('utf-8'))
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        res = self.message_handler(data.decode('utf-8'))
                        conn.sendall(res.encode('utf-8'))
                        if res == "+OK logging out":
                            conn.close()
                            break


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.mails = []
        self.login = login
        self.password = password

    def create_mail(self, from_, to_, subject, content):
        print("Adding mail to user {}".format(self.login))
        mail = {'id': len(self.mails)+1, 'from': from_, 'to': to_, 'subject': subject, 'content': content}
        self.mails.append(mail)

    def get_mail(self, id_):
        for mail in self.mails:
            if mail['id'] == id_:
                return "From: {}\nTo: {}\nSubject: {}\n\n{}\n\n".format(mail['from'], mail['to'], mail['subject'], mail['content'])


def main():
    server = Server()
    server.run()


if __name__ == "__main__":
    main()
