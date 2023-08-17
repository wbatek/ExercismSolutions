def factors(value):
    result = []
    last_factor = 2
    while value > 1:
        while value % last_factor != 0:
            last_factor += 1

        result.append(last_factor)
        value //= last_factor

    return result
