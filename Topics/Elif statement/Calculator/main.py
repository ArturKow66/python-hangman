first_number = float(input())
second_number = float(input())
arithmetic_operator = input()

if arithmetic_operator == '+':
    print(float(first_number + second_number))
elif arithmetic_operator == '-':
    print(float(first_number - second_number))
elif arithmetic_operator == '*':
    print(float(first_number * second_number))
elif arithmetic_operator == 'pow':
    print(float(first_number ** second_number))
elif second_number == 0.0:
    print('Division by 0!')
elif arithmetic_operator == '/':
    print(float(first_number / second_number))
elif arithmetic_operator == 'mod':
    print(float(first_number % second_number))
elif arithmetic_operator == 'div':
    print(float(first_number // second_number))
