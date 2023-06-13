import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect(('httpbin.org', 80))
        data = "GET /html HTTP/1.1\r\nHost: httpbin.org\r\nUser-Agent: Safari/7.0.3\r\n\r\n"
        sock.sendall(data.encode())
        res = ""
        while True:
            data = sock.recv(10000).decode()
            res += data
            if data.endswith("</html>"):
                break
    finally:
        header = res.split("\r\n\r\n")[0]
        print(header)
        res = res.split("\r\n\r\n")[1]
        with open("index.html", "w") as f:
            f.write(res)
        sock.close()



