import socket
import os
import time
import stat

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        time = time.ctime(os.stat("stuff_2.png")[stat.ST_MTIME])
        sock.connect(('httpbin.org', 80))
        data = "GET /image/png HTTP/1.1\r\nHost: httpbin.org\r\nIf-Modified-Since:"+time+"\r\n\r\n"
        sock.sendall(data.encode())
        sock.settimeout(5)
        res = b""
        while True:
            data = sock.recv(10000)
            res += data
    except socket.timeout:
        pass
    finally:
        print(res)
        pos = res.find(b"\r\n\r\n")
        picture = res[pos + 4:]
        with open("stuff_2.png", "wb") as file:
            file.write(picture)
            file.close()
