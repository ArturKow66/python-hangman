import random
import string

is_play = True
guesses_counter = 8
guesses_set = set()
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


print('''H A N G M A N''')
while is_play:
    guess_output = prepare_guess(word_to_guess)
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == 'play':
        while guesses_counter != 0:
            print(f'\n{guess_output}')
            if guess_output == word_to_guess:
                print('You guessed the word!')
                print('You survived!')
                break
            guess = input('Input a letter: ')
            if len(guess) == 1:
                if guess in string.ascii_lowercase:
                    if guess in guesses_set:
                        print("You've already guessed this letter")
                    elif guess in set(word_to_guess):
                        guess_output = change_in_guess(word_to_guess, guess_output, guess)
                    else:
                        guesses_counter -= 1
                        print("That letter doesn't appear in the word")
                    guesses_set.add(guess)
                else:
                    print('Please enter a lowercase English letter')
            else:
                print('You should input a single letter')
        else:
            print('You lost!')
    elif play == 'exit':
        break
