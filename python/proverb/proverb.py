def proverb(*words, qualifier):
    if not words:
        return []
    lines = [f'For want of a {w} the {l} was lost.' for w, l in zip(words, words[1:])]
    q = '' if qualifier is None else f'{qualifier} '
    return lines + [f'And all for the want of a {q}{words[0]}.']



