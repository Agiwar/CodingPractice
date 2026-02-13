from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Input is unsorted, but it doesn't matter,
            we only wanna remove the specific number from array
        
        If nums.length has min value of zero, so directly return 0 anyway
        Think about what if nums.length is one, and the number is equal to val,
            which means this number must be removed from nums, so return zero as well
        
        Based on these situations above, we need to check whether or not
            the first number with zero index is needed to be removed.
        
        Define a writer (idx_w) and reader (idx_r) pointer, respectively
            idx_w handles the current position's number should be re-written or not,
            idx_r is a pointer to just go through the entire array,
            checking the current number can be a re-written number for those idx_w
        
        time = O(n)
        space = O(1), in-place manipulation
        """

        idx_w = 0
        for idx_r in range(len(nums)):
            if nums[idx_r] != val:
                nums[idx_w] = nums[idx_r]
                idx_w += 1
        
        return idx_w



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
