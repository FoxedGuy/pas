import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect(('httpbin.org', 80))
        # get image from /image/jpeg
        data = "GET /image/png HTTP/1.1\r\nHost: httpbin.org\r\n\r\n"
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
        with open("stuff_2.png", "wb") as file:
            file.write(picture)
            file.close()
