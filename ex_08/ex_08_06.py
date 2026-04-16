numbers = []

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    numbers.append(int(num))

print(f'{min(numbers):.1f}')
print(f'{max(numbers):.1f}')
