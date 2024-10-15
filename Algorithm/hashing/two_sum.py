from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_hash = {}

        for idx, num in enumerate(nums):
            if num in diff_hash:
                return [diff_hash[num], idx]
                
            diff = target - num
            diff_hash[diff] = idx