from typing import List


def sum_alphabet(words: List[str]) -> List[int]:
    # ord("a") = 97, ord("b") = 98
    if not words: return [0]

    return [
        sum((ord(char) - ord("a") + 1) for char in word)
        for word in words
    ]
