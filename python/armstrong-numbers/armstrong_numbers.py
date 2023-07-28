def is_armstrong_number(number):
    number_length = len(str(number))
    number_copy = number
    sum = 0
    while number_copy > 0:
        sum += (number_copy % 10) ** number_length
        number_copy //= 10
    return number == sum