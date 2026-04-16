file = open('romeo.txt')
uniwrd = []

for line in file:
    words = line.split()

    for word in words:
        if word in uniwrd:
            continue
        if words != uniwrd:
            uniwrd.append(word)

uniwrd.sort()

print(uniwrd)