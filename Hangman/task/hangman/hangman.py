import random

words_list = ['python', 'java', 'kotlin', 'javascript']
word_to_guess = random.choice(words_list)

print('''H A N G M A N
The game will be available soon.''')

guess = input('Guess the word: ')

if guess == word_to_guess:
    print('You survived!')
else:
    print('You lost!')
