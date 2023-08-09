import string

alphabet = list(string.ascii_lowercase)


def encode(plain_text):
    result = ''
    counter = 0
    for letter in plain_text:
        if letter.isalnum():
            if counter % 5 == 0 and counter != 0:
                result += ' '
            if letter.isalpha():
                result += alphabet[-1 - alphabet.index(letter.lower())]
            else:
                result += letter
            counter += 1
    return result


def decode(ciphered_text):
    result = ''
    ciphered_text = ''.join(ciphered_text.split())
    for letter in ciphered_text:
        if letter.isalpha():
            result += alphabet[-1 - alphabet.index(letter)]
        else:
            result += letter
    return result
