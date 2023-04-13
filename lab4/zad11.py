import socket


def check_syntax_a(message):
    if len(message.split(';')) != 9:
        return "BAD_SYNTAX"
    else:
        txt = message.split(';')
        if txt[0] == "zad15odpA" and txt[1] == "ver" and txt[3] == "srcip" and txt[5] == "dstip" and txt[7] == "type":
            try:
                ver = int(txt[2])
                srcip = txt[4]
                dstip = txt[6]
                type = int(txt[8])
                if ver == 4 and type == 6 and srcip == "212.182.24.27" and dstip == "192.168.0.2" and type == 6:
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"


def check_syntax_b(message):
    if len(message.split(';')) != 7:
        return "BAD_SYNTAX"
    else:
        txt = message.split(';')
        if txt[0] == "zad15odpB" and txt[1] == "srcport" and txt[3] == "dstport" and txt[5] == "data":
            try:
                src = int(txt[2])
                dst = int(txt[4])
                data = txt[6]
                if src == 2900 and dst == 47526 and data == "network programming is fun":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('localhost', 2911))
    while True:
        data, address = sock.recvfrom(4096)
        print('received "%s" from %s' % (data.decode('utf-8'), address))
        if data.decode('utf-8').split(';')[0] == "zad15odpA":
            res = check_syntax_a(data.decode('utf-8'))
        elif data.decode('utf-8').split(';')[0] == "zad15odpB":
            res = check_syntax_b(data.decode('utf-8'))
        else:
            res = "BAD_SYNTAX"
        sock.sendto(res.encode('utf-8'), address)