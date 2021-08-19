def what_to_do(instructions):
    simon = "Simon says"
    if instructions.startswith(simon):
        output = instructions.lstrip(simon)
        return f'I {output}'
    elif instructions.endswith(simon):
        output = instructions.rstrip(simon)
        return f'I {output}'
    else:
        return "I won't do it!"

