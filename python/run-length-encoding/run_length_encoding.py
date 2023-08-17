def decode(string):
    result = ''
    i = 0
    while i < len(string):
        if not string[i].isnumeric():
            result += string[i]
        else:
            memory = i
            while string[i + 1].isnumeric():
                i += 1
            count = string[memory : i + 1]
            print(count)
            result += string[i + 1] * int(count)
            i += 1
        i += 1
    return result


def encode(string):
    result = ''
    i = 0
    while i < len(string):
        current = string[i]
        count = 1
        while i + 1 < len(string) and string[i + 1] == current:
            i += 1
            count += 1

        if count == 1:
            result += current
        else:
            result += str(count) + current

        i += 1

    return result
