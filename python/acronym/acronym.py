import re


def abbreviate(words):
    words = words.replace('-', ' ').replace('_', ' ')
    l = re.sub(r'[^\w\s]', '', words).split()
    result = ""
    for word in l:
        result += word[0].upper()
    return result


abbreviate("The Road _Not_ Taken")