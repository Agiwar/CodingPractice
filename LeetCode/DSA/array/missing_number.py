from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pass

missingNumber = Solution().missingNumber

def test_missingNumber():
    # LeetCode examples
    assert missingNumber([3,0,1]) == 2
    assert missingNumber([0,1]) == 2
    assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8

    # Edge cases (write your own)

    print("All tests passed")

if __name__ == "__main__":
    test_missingNumber()
