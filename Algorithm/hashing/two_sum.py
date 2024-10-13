from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx, num in enumerate(nums):
            if num not in hash_map:
                diff = target - num
                hash_map[diff] = idx
            else:
                return [hash_map[num], idx]