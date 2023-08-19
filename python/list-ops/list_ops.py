def append(list1, list2):
    return list1 + list2


def concat(lists):
    res = []
    for list in lists:
        res = append(res, list)
    return res


def filter(function, list):
    return [element for element in list if function(element)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    for item in list[::-1]:
        accumulator = function(accumulator, item)
    return accumulator


def reverse(list):
    return list[::-1]
