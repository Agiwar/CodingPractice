from typing import List, Optional, Tuple


def find_bigrams(sentence: str) -> Optional[List[Tuple]]:
    if not sentence: return None
    
    words_list = sentence.split()

    res = []
    for idx in range(1, len(words_list)):
        bigram = (words_list[idx - 1].lower(), words_list[idx].lower())
        res.append(bigram)

    return res