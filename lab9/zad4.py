import socket
import requests


# create loop to get data from user and create dictionary
d = {}
while True:
    k = input("Key (0 to end): ")
    if k == "0":
        break
    v = input("Value: ")
    d[k] = v

# create json string from dictionary
s = "{"
for k, v in d.items():
    s += f"\"{k}\": \"{v}\", "
s = s[:-2] + "}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # connect to httpbin.org and send post request

    print(len(s))
    sock.connect(('httpbin.org', 80))
    sock.settimeout(5)
    data = "POST /post HTTP/1.1\r\n" \
        "Host: httpbin.org \r\n"\
        "Accept: application/json\r\n"\
        "Content-Type: application/json\r\n"\
        "Content-Length:" + str(len(s)) + "\r\n\r\n"\
        + s + "\r\n\r\n"

    sock.sendall(data.encode())
    res = ""
    try:
        while True:
            data = sock.recv(4096)
            res += data.decode()
    except socket.timeout:
        pass
    finally:
        print(res)


