string = input().lower()


def reverse_word_sentence(sentence):
    return ' '.join(word[::-1] for word in sentence.split(" "))


if reverse_word_sentence(string) == string:
    print('Palindrome')
else:
    print('Not palindrome')
