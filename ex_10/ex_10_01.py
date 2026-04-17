file = open('mbox-short.txt')
wrd_dict = {}
for line in file:
    words = line.split()
    if len(words) < 2:
        continue
    if words[0] != 'From':
        continue
    