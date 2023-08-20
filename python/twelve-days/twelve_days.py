DAYS = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]

ITEMS = [
    'a Partridge in a Pear Tree',
    'two Turtle Doves',
    'three French Hens',
    'four Calling Birds',
    'five Gold Rings',
    'six Geese-a-Laying',
    'seven Swans-a-Swimming',
    'eight Maids-a-Milking',
    'nine Ladies Dancing',
    'ten Lords-a-Leaping',
    'eleven Pipers Piping',
    'twelve Drummers Drumming'
]


def verse(n):
    if n == 1:
        return 'On the ' + DAYS[n - 1] + ' day of Christmas my true love gave to me: ' + ITEMS[n - 1] + '.'
    else:
        return 'On the ' + DAYS[n - 1] + ' day of Christmas my true love gave to me: ' + ', '.join(
            ITEMS[i] for i in range(n - 1, 0, -1)) + ', and ' + ITEMS[0] + '.'


def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse + 1)]
