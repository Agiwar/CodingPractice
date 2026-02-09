from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass

maxSubArray = Solution().maxSubArray

def test_maxSubArray():
    # LeetCode examples
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5,4,-1,7,8]) == 23

    # Edge cases (write your own)

    print("All tests passed")

if __name__ == "__main__":
    test_maxSubArray()
