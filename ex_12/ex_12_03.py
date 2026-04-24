import urllib.request, urllib.parse, urllib.error
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
    fhand = urllib.request.urlopen(url)
except:
    print('Cannot connect to server.')
    sys.exit()


while True:
    data = fhand.read()
    if len(data) < 1:
        break

    decoded = data.decode()
    full_data = full_data + decoded

print (full_data[:limit])

print(f'Total characters {len(full_data)}')


#http://data.pr4e.org/romeo.txt