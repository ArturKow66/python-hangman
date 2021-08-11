number = 0
counter = 0
sum_of_numbers = 0
average = 0.0

while number != 55:
    counter += 1
    number = int(input())
    if number == 55:
        break
    else:
        sum_of_numbers += number
        average = sum_of_numbers / counter
print(counter - 1)
print(sum_of_numbers)
print(round(average))
