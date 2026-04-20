import re

fname = input("Enter file: ")

file = open(fname)

numbers = []

for line in file:
    line = line.rstrip()
    found = re.findall(r'^New Revision: ([0-9]+)', line)
    if found:
        numbers.append(int(found[0]))

average = sum(numbers) // len(numbers)

print(average)