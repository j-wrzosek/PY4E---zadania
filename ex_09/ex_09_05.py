file = open('mbox-short.txt')

wrd_dict = {}

for line in file:
    words = line.split()
    if len(words) < 2:
        continue
    if words[0] != 'From':
        continue

    email = words[1]
    domain = email.split('@')[1]

    wrd_dict[domain] = wrd_dict.get(domain, 0) + 1

print(wrd_dict)