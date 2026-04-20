file = open('mbox-short.txt')

wrd_dict = {}

for line in file:
    words = line.split()
    if len(words) < 6:
        continue
    if words[0] != 'From':
        continue

    time = words[5]
    hour = time.split(':')[0]

    wrd_dict[hour] = wrd_dict.get(hour, 0) + 1

lista = []

for hour, count in wrd_dict.items():
    lista.append((hour, count))

print(lista)