
try:
    fhand = open('mbox-short.txt')
except:
    print('Nie ma takiego pliku')
    exit()

for line in fhand:
    line = line.rstrip()
    words = line.split()

    if len(words) == 0:
        continue

    if words[0] != 'From':
        continue

    if len(words) < 3:
        continue

    print(words[2])