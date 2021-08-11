x_index = int(input())
y_index = int(input())
index = x_index + y_index

moves = 0

if 1 < x_index < 8:
    if 1 < y_index < 8:
        print('8')
    elif y_index in [1, 8]:
        print('5')
elif x_index in [1, 8]:
    if 1 < y_index < 8:
        print('5')
    elif y_index in [1, 8]:
        print('3')
