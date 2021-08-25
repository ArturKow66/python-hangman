numbers = list()
while True:
    value = input()
    if value == '.':
        break
    number = float(value)
    numbers.append(number)

print(min(numbers))
