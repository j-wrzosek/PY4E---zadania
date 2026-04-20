file = open('mbox-short.txt')

wrd_dict = {}

for line in file:
    words = line.split()
    if len(words) < 2:
        continue
    if words[0] != 'From':
        continue

    email = words[1]

    wrd_dict[email] = wrd_dict.get(email, 0) + 1

print(wrd_dict)

lista = []
for email,count in wrd_dict.items():
    lista.append((count, email))

lista.sort(reverse=True)
print(lista[0])
