from typing import List


def bubble_sort_1(nums: List[int]) -> List[int]:
    n = len(nums) - 1
    
    if n <= 0:
        return nums
    
    while n > 0:
        need_to_swap = False
        for i in range(n):
            if nums[i] > nums[i + 1]:
                need_to_swap = True
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        if not need_to_swap:
            break
        
        n -= 1
    
    return nums


def bubble_sort_2(nums: List[int]) -> List[int]:
    n = len(nums)
    
    if n <= 1:
        return nums
    
    while n > 1:
        need_to_swap = False
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                need_to_swap = True
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        
        if not need_to_swap:
            break
        
        n -= 1
    
    return nums
