def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            if item is not None:
                result.append(item)
    return result
