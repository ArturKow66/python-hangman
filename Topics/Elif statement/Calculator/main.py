first_number = float(input())
second_number = float(input())
arithmetic_operator = input()

if second_number == 0.0:
    print('Division by 0!')
elif arithmetic_operator == '+':
    print(first_number + second_number)
elif arithmetic_operator == '-':
    print(first_number - second_number)
elif arithmetic_operator == '*':
    print(first_number * second_number)
elif arithmetic_operator == '/':
    print(first_number / second_number)
elif arithmetic_operator == 'mod':
    print(first_number % second_number)
elif arithmetic_operator == 'pow':
    print(first_number ** second_number)
elif arithmetic_operator == 'div':
    print(first_number // second_number)
