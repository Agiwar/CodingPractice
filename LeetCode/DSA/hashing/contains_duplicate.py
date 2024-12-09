from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        occur = set()
        for num in nums:
            if num in occur:
                return True

            occur.add(num)
        
        return False