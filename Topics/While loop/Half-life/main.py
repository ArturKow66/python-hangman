initial_quantity = int(input())
final_quantity = int(input())
quantity = initial_quantity
counter = 0

while quantity > final_quantity:
    counter += 1
    quantity = quantity / 2

print(counter * 12)