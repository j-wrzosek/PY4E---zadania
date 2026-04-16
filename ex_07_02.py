#Write a program to prompt for a file name, and then read through the file and look for lines of the form
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point
# number on the line. Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

fh = open(input('Enter file name: '))

count = 0
prob = 0

for line in fh:
    line = line.rstrip()

    if line.startswith('X-DSPAM-Confidence:') :
        prob = prob + (float(line[19::]))

    if not(line.startswith('X-DSPAM-Confidence:') ):
        continue

    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1

print(f'Average spam confidence: {prob/count:.4f}')
