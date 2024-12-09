from typing import List


def equivalent_index(nums: List[int]) -> int:
    if not nums or len(nums) < 3: return -1

    for idx in range(1, len(nums) - 1):
        left = nums[:idx + 1]
        right = nums[idx + 1:]

        if sum(left) == sum(right):
            return idx
    
    return -1