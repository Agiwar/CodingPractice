from collections import defaultdict, Counter
from typing import Dict, List


def word_frequency(sentences: List[str]) -> Dict[str, List[str]]:
    word_occur = Counter()
    
    for line in sentences:
        word_occur += Counter(line.lower().split())
    
    word_occur_agg = defaultdict(list)
    for word, occur in word_occur.items():
        word_occur_agg[occur].append(word)
    
    return word_occur_agg