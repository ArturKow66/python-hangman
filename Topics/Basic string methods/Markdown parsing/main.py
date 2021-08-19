text = input()


def no_special(no_special_text):
    return no_special_text.strip('*_~`')


print(no_special(text))
