def square_root(number):
    if number < 2:
        return number
    for i in range((number // 2) + 1):
        if i * i == number:
            return i
    return None