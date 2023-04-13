import socket

def check_syntax(message):
    if len(message.split(';')) != 7:
        return "BAD_SYNTAX"
    else:
        txt = message.split(';')
        print(txt)
        if txt[0] == "zad13odp" and txt[1] == "src" and txt[3] == "dst" and txt[5] == "data":
            try:
                src = int(txt[2])
                dst = int(txt[4])
                data = txt[6]
                if src == 2900 and dst == 35211 and data == "hello :)":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('localhost', 2909))
    while True:
        data, address = sock.recvfrom(4096)
        print('received "%s" from %s' % (data.decode('utf-8'), address))
        res = check_syntax(data.decode('utf-8'))
        sock.sendto(res.encode('utf-8'), address)