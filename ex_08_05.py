file = open('mbox-short.txt')
count = 0

for line in file:
        words = line.split()
        if len(words) < 2:
            continue

        if words[0] != 'From':
            continue

        print(words[1])
        count += 1


print(f'There were {count} lines in the file with From as the first words.')
