file = open('mbox-short.txt')

wrd_dict = {}

for line in file:
    line = line.lower()
    for letter in line:
        if letter.isalpha():
            wrd_dict[letter] = wrd_dict.get(letter,0) + 1

lista = []
for letter,count in wrd_dict.items():
    lista.append((count,letter))

lista.sort(reverse=True)

for count, letter in lista:
    print(letter,count)