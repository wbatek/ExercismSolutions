import string

alphabet = string.ascii_lowercase


def rotate(text, key):
    after_translation = alphabet[key:] + alphabet[:key]
    translation = str.maketrans(alphabet + alphabet.upper(), after_translation + after_translation.upper())
    return text.translate(translation)
