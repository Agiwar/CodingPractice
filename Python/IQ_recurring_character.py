from typing import Optional


def recurring_char(input: str) -> Optional[str]:
    char_existed = set()
    for char in input:
        if char in char_existed:
            return char
        char_existed.add(char)
    
    return None