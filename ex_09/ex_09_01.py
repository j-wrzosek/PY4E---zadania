file = open('words.txt')
wrd_dict = {}
count = 0
for line in file:
    words = line.split()
    for word in words:
        if word not in wrd_dict:
            count = count + 1
            wrd_dict[word] = count

print(wrd_dict)
