
fn = (input('Enter file name: '))

if fn == 'witam':
    print('witam')

    quit()

try:
    fh = open(fn)
except:
    print('File not found')
    quit()

count = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
print(f'There is {count} X-DSPAM-Confidence lines in the file.')