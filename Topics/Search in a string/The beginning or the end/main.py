text = input()

if text.find('old') > text.rfind('old'):
    print(text.find('old'))
else:
    print(text.rfind('old'))
