from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        The input array nums is already sorted, and we can only keep the seen number twice.
            the nums.length has at least value of 1, if is one, return 1
            and can be 2, it means we can directly return two
            regardless of these two number are the same.
        
        Cuz nums is sorted,
            if the current number is not equal to the seen number's previous two's value
            then, this number must not be the seen number's position's previous one.

        So we can just get started at the 3rd number (2-idx)
            to check the current number should be re-written
        
        Define writer (idx_w) and reader (idx_r), respectively
            idx_w handles the current position's number should be re-written or not
            idx_r goes through entire array until we find out the unseen number
        
        time = O(n)
        space = (1), in-place manipulation
        """
        
        n = len(nums)
        if n <= 2:
            return n

        idx_w = 2
        for idx_r in range(2, n):
            if nums[idx_r] != nums[idx_w - 2]:
                nums[idx_w] = nums[idx_r]
                idx_w += 1
        
        return idx_w





removeDuplicates = Solution().removeDuplicates


def test_removeDuplicates():
    # LeetCode examples
    assert removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
    assert removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7

    # Edge cases (write your own)
    assert removeDuplicates([1]) == 1
    assert removeDuplicates([1, 1]) == 2
    assert removeDuplicates([1, 1, 2]) == 3
    assert removeDuplicates([1, 1, 1, 2]) == 3
    assert removeDuplicates([1, 1, 2, 2]) == 4
    assert removeDuplicates([-2, -1, -1, -1, 0, 0, 0, 0, 1, 2]) == 7
    assert removeDuplicates([-1, -1]) == 2
    assert removeDuplicates([0]) == 1
    assert removeDuplicates([0, 0]) == 2

    print("All tests passed")


if __name__ == "__main__":
    test_removeDuplicates()
