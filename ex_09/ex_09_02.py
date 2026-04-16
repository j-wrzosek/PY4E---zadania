file = open(input('Enter file name: '))
wrd_dict = {}
count = 0
for line in file:
    words = line.split()
    if len(words) < 2:
        continue
    if words[0] != 'From':
        continue
    if words[2] not in wrd_dict:
        wrd_dict[words[2]] = 0
    if words[2] in wrd_dict:
        wrd_dict[words[2]] += 1

print(wrd_dict)