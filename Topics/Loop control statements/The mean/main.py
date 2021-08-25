number = 0
counter = 0
is_running = True
while is_running:
    value = input()
    if value == '.':
        break
    number += int(value)
    counter += 1

print(number / counter)
