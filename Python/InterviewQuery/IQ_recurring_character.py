from collections import Counter
from typing import Optional


def recurring_char(input: str) -> Optional[str]:
    char_occur = Counter(input)
    return next((char for char, occur in char_occur.items() if occur > 1), None)