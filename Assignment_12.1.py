import socket
skt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
skt.send(cmd)
while True:
    data=skt.recv(1024)
    if len(data)<1:
        break
    print(data.decode())
skt.close()

# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#
# mysock.close()