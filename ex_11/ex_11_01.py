import re

fname = input("Enter file name: ")

regex = input("Enter a regular expression: ")

count = 0

file = open(fname)

for line in file:
    line = line.rstrip()
    if re.search(regex, line):
        count += 1

print(fname, "had", count, "lines that matched", regex)