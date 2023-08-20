import random
import string

NAME_CACHE = set()
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '1234567890'


def generate_name():
    name = ''.join((random.choice(UPPERCASE),
                    random.choice(UPPERCASE),
                    random.choice(DIGITS),
                    random.choice(DIGITS),
                    random.choice(DIGITS)))
    return name


class Robot:
    def __init__(self):
        name = generate_name()
        while name in NAME_CACHE:
            name = generate_name()
        NAME_CACHE.add(name)
        self.name = name

    def reset(self):
        self.__init__()
