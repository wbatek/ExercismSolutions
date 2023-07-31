COMMANDS = ('wink', 'double blink', 'close your eyes', 'jump')


def commands(binary_str):
    number = int(binary_str, 2)
    c = []
    for i, j in enumerate(COMMANDS):
        if number & 1 << i:
            c.append(j)
    if number & 1 << 4:
        c.reverse()
    return c

