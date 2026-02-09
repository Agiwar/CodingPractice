from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pass

subarraySum = Solution().subarraySum

def test_subarraySum():
    # LeetCode examples
    assert subarraySum([1,1,1], 2) == 2
    assert subarraySum([1,2,3], 3) == 2

    # Edge cases (write your own)

    print("All tests passed")

if __name__ == "__main__":
    test_subarraySum()
