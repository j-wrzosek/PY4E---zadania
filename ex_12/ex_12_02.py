import socket
import sys

full_data = ''
limit = 3000

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

    decoded = data.decode()
    full_data = full_data + decoded

print (full_data[:limit])

print(f'Total characters {len(full_data)}')
mysock.close()

#http://data.pr4e.org/romeo.txt