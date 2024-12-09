from typing import Dict, List


def closest_key(dictionary: Dict[str, List[str]], input: str) -> str:
    input_ord = ord(input)
    
    difference = {}
    for key, val in dictionary.items():
        difference[key] = abs(input_ord - ord(val[0])) if val else float("inf")
    
    return min(difference, key=difference.get)
