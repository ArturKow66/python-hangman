scores = input().split()
counter_i = 0
counter_c = 0

for i in scores:
    if i == 'I':
        counter_i += 1
        if counter_i == 3:
            print('Game over')
            print(counter_c)
            break
    elif i == 'C':
        counter_c += 1
else:
    print('You won')
    print(counter_c)
