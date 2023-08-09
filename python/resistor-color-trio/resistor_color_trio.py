resistors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

prefixes = {
    1000000000: 'giga',
    1000000: 'mega',
    1000: 'kilo'
}


def label(colors):
    res = [resistors[v] for v in colors]
    first = int(f"{res[0]}{res[1]}")
    second = int(f"{first}{'0'*res[2]}")
    suffix = f"ohms"

    for base, pref in prefixes.items():
        if second > base:
            suffix = f"{pref}ohms"
            second = second // base
            break

    return f"{second} {suffix}"

