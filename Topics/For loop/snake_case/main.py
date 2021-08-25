phrase = input()
output = ''

for i in range(len(phrase)):
    n = phrase[i]
    if n.isupper() and i == 0:
        output += n.lower()
    elif n.isupper():
        output += '_' + n.lower()
    else:
        output += n

print(output)
