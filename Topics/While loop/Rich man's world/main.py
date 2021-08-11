start_value = int(input())
interest_rate = 1.071
counter = 0

while start_value <= 700000:
    start_value = start_value * interest_rate
    counter += 1
print(counter)