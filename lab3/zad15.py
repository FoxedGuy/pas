import socket

ip_h = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce " \
       "9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 " \
       "20 66 75 6e"


def hex_to_ascii(data):
    ascii = ""
    for i in data:
        ascii += chr(int(i,base=16))
    return ascii


def get_info_from_header(ip_h):
    ip = ip_h.split(" ")

    version = ip[0][0]
    ihl = int(ip[0][1],base=16)

    protocol = int(ip[9],base=16)

    source_ip = str(int(ip[12],base=16))+"."+str(int(ip[13],base=16))+"."+str(int(ip[14],base=16))+"."+str(int(ip[15],base=16))
    destination_ip = str(int(ip[16],base=16))+"."+str(int(ip[17],base=16))+"."+str(int(ip[18],base=16))+"."+str(int(ip[19],base=16))

    source_port = int(ip[20]+ip[21],base=16)
    destination_port = int(ip[22]+ip[23],base=16)

    data = ""
    if protocol == 6 and ihl == 5:
        data = ip[52:]
        data = hex_to_ascii(data)

    return version, source_ip, destination_ip, protocol, source_port, destination_port, data


version, source_ip, destination_ip, protocol, source_port, destination_port, data = get_info_from_header(ip_h)
odpA = "zad15odpA;ver;"+version+";srcip;"+source_ip+";dstip;"+destination_ip+";type;"+str(protocol)
odpB = "zad15odpB;srcport;"+str(source_port)+";dstport;"+str(destination_port)+";data;"+data

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sockIPv4:
    sockIPv4.connect(("localhost", 2911))
    sockIPv4.send(odpA.encode('utf-8'))
    result = sockIPv4.recv(1024).decode("utf-8")
    if result == "TAK":
        sockIPv4.send(odpB.encode('utf-8'))
        result = sockIPv4.recv(1024).decode("utf-8")
        if result == "TAK":
            print("Odpowiedź poprawna")
        else:
            print("Odpowiedź niepoprawna")