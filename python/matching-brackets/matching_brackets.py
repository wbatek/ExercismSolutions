mapping = {
    ']': '[',
    ')': '(',
    '}': '{'
}


def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack or mapping.get(char) != stack[-1]:
                return False
            stack.pop()
    if not stack:
        return True
    return False
