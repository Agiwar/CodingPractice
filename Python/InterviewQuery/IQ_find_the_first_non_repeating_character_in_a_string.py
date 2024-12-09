from collections import Counter


def first_uniq_char(s: str) -> int:
    char_occur = Counter(s)
    return next((idx for idx, char in enumerate(s) if char_occur[char] == 1), -1)

    # for idx, char in enumerate(s):
    #     if char_occur[char] == 1:
    #         return idx
    
    # return -1