file = open('mbox-short.txt')

wrd_dict = {}
count = 0
for line in file:
    words = line.split()
    if len(words) < 2:
        continue
    if words[0] != 'From':
        continue
    if words[1] not in wrd_dict:
        wrd_dict[words[1]] = 0
    if words[1] in wrd_dict:
        wrd_dict[words[1]] += 1

print(wrd_dict)