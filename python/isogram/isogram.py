from string import ascii_lowercase


def is_isogram(string):
    for letter in ascii_lowercase:
        if string.lower().count(letter) > 1:
            return False
    return True
