from math import sqrt


def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    cnt = 0
    i = 0
    while True:
        i += 1
        if isprime(i):
            cnt += 1

        if cnt == number:
            return i
