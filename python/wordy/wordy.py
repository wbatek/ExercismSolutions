operations = {
    'plus': '+',
    'minus': '-',
    'multiplied': '*',
    'divided': '/'
}


def answer(question):
    if not question.startswith("What is") and question.endswith('?'):
        raise ValueError('unknown operation')

    question = question.replace('What is', '').replace('by', '').rstrip('?').strip()
    if not question:
        raise ValueError('syntax error')
    if question.lstrip('-').isdigit():
        return int(question)

    words = question.split()
    if len(words) == 2:
        if words[1] not in operations.keys():
            raise ValueError('unknown operation')
        raise ValueError('syntax error')

    if words[0] in operations.keys():
        raise ValueError('syntax error')
    result = int(words[0])

    for i in range(1, len(words), 2):
        if words[i].lstrip('-').isdigit():
            raise ValueError('syntax error')
        if words[i] not in operations.keys():
            raise ValueError('unknown operation')

        operator = operations.get(words[i])

        if not words[i + 1].lstrip('-').isdigit():
            raise ValueError('syntax error')

        operand = int(words[i + 1])
        result = eval(f'{result}{operator}{operand}')
    return result