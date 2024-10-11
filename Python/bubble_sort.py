from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    n = len(nums) - 1
    
    if n <= 0:
        return nums
    
    while n > 0:
        need_to_swap = False
        for i in range(n):
            if nums[i] > nums[i + 1]:
                need_to_swap = True
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        n -= 1
        
        if not need_to_swap:
            break
    
    return nums
