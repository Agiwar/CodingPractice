from typing import List


def merge_two_sorted_list(list1: List[int], list2: List[int]) -> List[int]:
    if not list1: return list2
    elif not list2: return list1

    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        
        else:
            merged_list.append(list2[j])
            j += 1
    
    merged_list.extend(list1[i:] or list2[j:])
    return merged_list


def sort_lists(lists: List[List[int]]) -> List[int]:
    # N = size of list, K = number of lists
    # time = O(K * N * log K)
    # space = O(K * N)
    if not lists: return []

    while len(lists) > 1:
        merged_list = []

        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if (i + 1) < len(lists) else []
            merged_list.append(merge_two_sorted_list(list1, list2))
        
        lists = merged_list
    
    return lists[0]
