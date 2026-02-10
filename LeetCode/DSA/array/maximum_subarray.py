from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        The given array nums is not ordered and may contain negative or zero value,
            nums has at least length of 1, e.g., [9] return 9, cuz nums is itself subarray
            so the base case is max summation of subarray is nums[0]

        Cuz we want the max summation of subarray, so avoid the negative as possible as we can,
            which means when looping if the current summation of subarray is negative, skip it
            until the current sum is positive, and each loop, record the max sum comparing curr sum & last max sum

        time = O(n)
        space = O(1)
        """

        if len(nums) == 1:
            return nums[0]
        
        curr_sum = 0
        max_sum = nums[0]
        idx = 0
        
        while idx < len(nums):
            curr_sum += nums[idx]
            max_sum = max(max_sum, curr_sum)
            
            if curr_sum < 0:
                curr_sum = 0
                idx += 1
                continue
            
            idx += 1
        
        return max_sum

maxSubArray = Solution().maxSubArray

def test_maxSubArray():
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5,4,-1,7,8]) == 23

    # Edge cases
    assert maxSubArray([0]) == 0
    assert maxSubArray([-1]) == -1
    assert maxSubArray([-1, 4]) == 4
    assert maxSubArray([-2, 3, 1, 1, 5]) == 10
    assert maxSubArray([-2, 3, 1, -1, 3]) == 6
    assert maxSubArray([-2, -1, 0, 0, 5]) == 5
    assert maxSubArray([-3, -1, -2]) == -1
    assert maxSubArray([-3, -2, -1]) == -1
    assert maxSubArray([-3, -2, 3]) == 3


    print("All tests passed")

if __name__ == "__main__":
    test_maxSubArray()
