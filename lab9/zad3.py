import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect(('httpbin.org', 8080))
        data = "GET /image.jpeg HTTP/1.1\r\nHost: 212.182.24.27\r\n\r\n"
        sock.sendall(data.encode())
        sock.settimeout(5)
        res = b""
        while True:
            data = sock.recv(10000)
            res += data
    except socket.timeout:
        pass
    finally:
        pos = res.find(b"\r\n\r\n")
        picture = res[pos + 4:]
        with open("stuff.jpg", "wb") as file:
            file.write(picture)
            file.close()
