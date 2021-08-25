a = int(input())
b = int(input()) + 1
sum_ = 0
counter = 0

for i in range(a, b):
    if i % 3 == 0:
        sum_ += i
        counter += 1

print(sum_ / counter)
