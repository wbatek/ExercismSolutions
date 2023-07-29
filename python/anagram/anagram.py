def find_anagrams(word, candidates):
    word = word.lower()
    sorted_word = sorted(word)

    result = set()
    for candidate in candidates:
        c = candidate.lower()
        if c == word:
            continue
        if sorted(c) == sorted_word:
            result.add(candidate)

    return result
