from typing import List


def fill_none(input_list: List[int]) -> List[int]:
    if not input_list: return []
    
    input_list[0] = 0 if input_list[0] is None else input_list[0]

    pointer = 0
    for idx in range(1, len(input_list)):
        if input_list[idx] is None:
            input_list[idx] = input_list[pointer]
        else:
            pointer = idx
    
    return input_list