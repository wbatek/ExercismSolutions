def sum_of_multiples(limit, multiples):
    values = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        i = 1
        while multiple * i < limit:
            values.add(multiple * i)
            i += 1
    return sum(list(values))
