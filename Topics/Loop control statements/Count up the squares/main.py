sum_ = 0
sum_square = 0
is_first = True
while True:
    value = int(input())
    while is_first:
        if value == 0:
            break
        is_first = False
    sum_ += value
    sum_square += value ** 2
    if sum_ == 0:
        break
print(sum_square)
