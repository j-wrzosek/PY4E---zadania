import socket
import sys

url = input('Enter URL: ')
try:
    host = url.split('/')[2]
except:
    print('Invalid URL, try https://example.com/path')
    sys.exit()


try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((f'{host}', 80))
except:
    print('Cannot connect to server.')
    sys.exit()

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

#http://data.pr4e.org/romeo.txt
