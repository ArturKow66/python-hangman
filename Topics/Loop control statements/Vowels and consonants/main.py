sentence = input()
for i in range(len(sentence)):
    if sentence[i] in ' !@#$%^&*()_+-=\][|}{;:/.,?><`"':
        break
    elif sentence[i] in 'aeiou':
        print('vowel')
    else:
        print('consonant')
