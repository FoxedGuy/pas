import socket
import time
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sockUDP:
    sockUDP.connect(("localhost", 2901))
    start = time.time()
    sockUDP.send('2'.encode('utf-8'))
    end = time.time()
    time_all = end - start
    print(f"UDP: {time_all:f}")
    response = sockUDP.recv(1024)
    print(response.decode('utf-8'))
    sockUDP.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockTCP:
    sockTCP.connect(("localhost", 2900))
    start = time.time()
    sockTCP.send('2'.encode('utf-8'))
    end = time.time()
    time_all = end - start
    print(f"TCP: {time_all:f}", )
    response = sockTCP.recv(1024)
    print(response.decode('utf-8'))
    sockTCP.close()


# korzystałem z serwerów echo z 1 laboratoriów
# podczas testowania wychodziło, że tcp jest szybszy od udp (przy wysyłaniu 2)


# jednak teoria jest inna
# udp jest szybszy, bo nie wymaga nawiązania połączenia by zacząć przesyłać pakiety, a tcp wymaga nawiązania połączenia
# i przesłania pakietu potwierdzającego nawiązanie połączenia, co zajmuje więcej czasu
# udp:
# -zalety:szybkość, brak konieczności nawiązywania połączenia
# -wady: brak gwarancji dostarczenia pakietu, brak gwarancji kolejności pakietów
# tcp:
# -zalety: gwarancja dostarczenia pakietu, gwarancja kolejności pakietów, szyfrowanie
# -wady: wolniejszy niż udp, konieczność nawiązania połączenia