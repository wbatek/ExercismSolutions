def get_factors(number):
    result = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            result.append(i)
    return result


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = get_factors(number)

    factors_sum = sum(factors)
    print(factors_sum)
    if factors_sum == number:
        return "perfect"
    return "abundant" if factors_sum > number else "deficient"