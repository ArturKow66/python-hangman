import random
is_running = True
counter = 0
guesses = 8
words_list = ['python', 'java', 'kotlin', 'javascript']
word_to_guess = random.choice(words_list)


def prepare_guess(word):
    n = len(word)
    word = '-' * n
    return word


def change_in_guess(word, current_output, letter):
    for i in range(len(word)):
        if word[i] == letter:
            current_output = current_output[:i] + letter + current_output[i+1:]
    return current_output


guess_output = prepare_guess(word_to_guess)

print('''H A N G M A N''')
while is_running:
    if counter < guesses:
        print(f'\n{guess_output}')
        guess = input('Input a letter: ')
        if guess in set(word_to_guess):
            guess_output = change_in_guess(word_to_guess, guess_output, guess)
        else:
            print("That letter doesn't appear in the word")
        counter += 1
    else:
        print('''\nThanks for playing!
We'll see how well you did in the next stage''')
        is_running = False
