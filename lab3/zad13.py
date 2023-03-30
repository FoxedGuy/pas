import socket


# convert hexadecimal strings to a string of ascii characters
def hex_to_ascii(data):
    ascii = ""
    for i in data:
        ascii += chr(int(i,base=16))
    return ascii


udp_h = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"

udp = udp_h.split(" ")

source_port = udp[0]+udp[1]
source_port = int(source_port,base=16)
destination_port = udp[2]+udp[3]
destination_port = int(destination_port,base=16)
length = udp[4]+udp[5]
length = int(length,base=16)
data = udp[8:]
data = hex_to_ascii(data)

print(data)


with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sockIPv4:
    sockIPv4.connect(("212.182.25.252", 2910))
    data_to_send = "zad14odp;"+"src;"+str(source_port)+";dst;"+str(destination_port)+";data;"+data
    sockIPv4.send(data_to_send.encode('utf-8'))
    data = sockIPv4.recv(1024)
    print(data.decode("utf-8"))
    sockIPv4.close()




