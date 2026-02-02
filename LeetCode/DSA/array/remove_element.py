from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        time = O(n)
        space = O(1)
        """
        if not nums:
            return 0
        
        k = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[k] = nums[idx]
                k += 1
        
        return k


removeElement = Solution().removeElement


def test_removeElement():
    # LeetCode examples
    assert removeElement([3, 2, 2, 3], 3) == 2
    assert removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5

    # Edge cases (write your own)
    assert removeElement([], 3) == 0
    assert removeElement([3], 3) == 0
    assert removeElement([3, 2, 2, 3], 1) == 4
    assert removeElement([3, 3], 3) == 0

    print("All tests passed")


if __name__ == "__main__":
    test_removeElement()
