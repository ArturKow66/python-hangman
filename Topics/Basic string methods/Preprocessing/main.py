text = input()


def output(new_output):
    return new_output.replace(',', '').replace('.', '').replace('!', '').replace('?', '').lower()


print(output(text))
