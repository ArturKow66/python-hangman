def check_email(string):
    if ' ' not in string:
        if '@' in string and '.' in string:
            return (string.rfind('@') + 1) < string.rfind('.')
        else:
            return False
    else:
        return False
