from typing import List


def find_pivot_index(nums: List[int]) -> int:
    L = 0
    R = len(nums) - 1

    while L < R:
        m = L + (R - L) // 2

        if nums[m] > nums[R]:
            L = m + 1
        
        elif nums[m] < nums[R]:
            R = m    
    
    return L


def binary_search(nums: List[int], target: int) -> int:
    L = 0
    R = len(nums) - 1

    while L <= R:
        m = L + (R - L) // 2

        if nums[m] > target:
            R = m - 1
        elif nums[m] < target:
            L = m + 1
        else:
            return m
    
    return -1


def target_value_search(rotated_input: List[int], target_value: List[int]) -> int:
    """
    time: overall is O(n)
        • find_pivot_index = O(log n)
        • split array to left and right parts = O(n)
        • binary_search = O(log n) + O(log n)
    space: O(n)
    """
    if not rotated_input: return -1

    m = find_pivot_index(rotated_input)

    left_half = rotated_input[:m]
    right_half = rotated_input[m:]

    left_idx = binary_search(left_half, target_value)
    right_idx = binary_search(right_half, target_value)

    if left_idx > right_idx:
        return left_idx
    elif left_idx < right_idx:
        return right_idx + m
    else:
        return -1

    

# (-1, 2) -> 2 + m
# (3, -1) -> 3
# (0, -1) -> 0
# (-1, -1) -> -1

# [0, 1, 2, 3, 4, 5, 6, 7]
# [7, 0, 1, 2, 3, 4, 5, 6]
# [6, 7, 0, 1, 2, 3, 4, 5]
# [5, 6, 7, 0, 1, 2, 3, 4]
# [4, 5, 6, 7, 0, 1, 2, 3]




def target_value_search(rotated_input: List[int], target_value: List[int]) -> int:
    """
    time = O(log n)
    space = O(1)
    """
    if not rotated_input: return -1
    
    L = 0
    R = len(rotated_input) - 1
    
    while L <= R:
        m = L + (R - L) // 2
        
        if rotated_input[m] == target_value:
            return m
        
        if rotated_input[m] >= rotated_input[L]:
            if rotated_input[L] <= target_value < rotated_input[m]:
                R = m - 1
            else:
                L = m + 1
        
        elif rotated_input[m] < target_value <= rotated_input[R]:
            L = m + 1
        
        else:
            R = m - 1
    
    return -1