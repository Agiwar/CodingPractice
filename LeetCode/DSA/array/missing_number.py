from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Given an array nums containing n distinct numbers in the range [0, n]  << included both sides
        # but there's a missing number in nums, find out it.

        expected_sum = sum(range(len(nums) + 1))  # time = O(n)
        actual_sum = sum(nums)  # time = O(n)
        
        # overall time = O(n)
        # space = O(1)

        return expected_sum - actual_sum