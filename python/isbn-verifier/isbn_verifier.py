def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    result = 0
    for i in range(len(isbn)):
        if isbn[i].isdigit():
            result += (10 - i) * int(isbn[i])
        elif isbn[i] == 'X' and i == len(isbn) - 1:
            result += (10 - i) * 10
        else:
            return False
    return result % 11 == 0
