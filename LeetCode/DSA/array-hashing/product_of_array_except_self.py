from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass

productExceptSelf = Solution().productExceptSelf

def test_productExceptSelf():
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_productExceptSelf()
