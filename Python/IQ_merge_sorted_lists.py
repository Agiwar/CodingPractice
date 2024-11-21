from typing import List


def merge_list(test_input_list1: List[int], test_input_list2: List[int]) -> List[int]:
    if not test_input_list1 and not test_input_list2:
        return []

    merged_list = []
    idx_1, idx_2 = 0, 0

    while (
        idx_1 < len(test_input_list1) and 
        idx_2 < len(test_input_list2)
    ):
        if test_input_list1[idx_1] <= test_input_list2[idx_2]:
            merged_list.append(test_input_list1[idx_1])
            idx_1 += 1
        else:
            merged_list.append(test_input_list2[idx_2])
            idx_2 += 1
    
    if idx_1 < len(test_input_list1):
        merged_list.extend(test_input_list1[idx_1:])
    elif idx_2 < len(test_input_list2):
        merged_list.extend(test_input_list2[idx_2:])
    
    return merged_list