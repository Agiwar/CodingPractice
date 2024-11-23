import re
from collections import Counter
from typing import List, Tuple, Optional


def n_frequent_words(posting: str, N: int) -> Optional[List[Tuple[str, int]]]:
    if not posting: return None
    
    posting = re.sub(r'[^a-zA-z0-9]', " ", posting.lower())
    return Counter(posting.split()).most_common(N)