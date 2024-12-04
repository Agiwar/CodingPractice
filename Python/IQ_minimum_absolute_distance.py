from typing import List


def min_distance(test_input: List[int]) -> List[List[int]]:
    test_input.sort()

    min_value = float("inf")
    pairs = []
    for subtrahend, minuend in zip(test_input, test_input[1:]):
        if minuend - subtrahend == min_value:
            pairs.append([subtrahend, minuend])
        
        elif minuend - subtrahend < min_value:
            min_value = minuend - subtrahend
            pairs = [[subtrahend, minuend]]
    
    return pairs