import re
from collections import Counter
from typing import List, Tuple


def n_frequent_words(posting: str, N: int) -> List[Tuple[str, int]]:
    posting = re.sub(r'[^a-zA-Z0-9]', " ", posting.lower())
    
    return Counter(posting.split()).most_common(N)