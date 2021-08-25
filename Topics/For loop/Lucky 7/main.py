n = int(input())
value_list = list()

for _ in range(n):
    value = int(input())
    value_list.append(value)

for k in value_list:
    if k % 7 == 0:
        print(k ** 2)
