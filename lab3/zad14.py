import socket


# convert hexadecimal strings to a string of ascii characters
def hex_to_ascii(data):
    ascii = ""
    for i in data:
        ascii += chr(int(i,base=16))
    return ascii


tcp_h = "0b 54 " \
        "89 8b " \
        "1f 9a 18 ec " \
        "bb b1 64 f2 " \
        "80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"

tcp = tcp_h.split(" ")
source_port = tcp[0]+tcp[1]
source_port = int(source_port,base=16)
destination_port = tcp[2]+tcp[3]
destination_port = int(destination_port,base=16)
data = tcp[32:]
data = hex_to_ascii(data)


with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sockIPv4:
    sockIPv4.connect(("212.182.25.252", 2909))
    data_to_send = "zad13odp;"+"src;"+str(source_port)+";dst;"+str(destination_port)+";data;"+data
    sockIPv4.send(data_to_send.encode('utf-8'))
    data = sockIPv4.recv(1024)
    print(data.decode("utf-8"))

