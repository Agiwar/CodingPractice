from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given a sorted array, each number can only seen once,
            and the nums.length has at lease value of one,
            it means the return result has at least one (this only number must be unique).

        So we can directly get started at 2nd number (1-idx) to check
            the current number should be removed or not,
            and use the different number value to replace the needed-removed number
        
        The key is that array is already sorted,
            so if the current number is not equal to seen number's previous one
            it guarantees the current number is the unseen number.
        
        Define the writer (idx_w) and reader (idx_r), respectively
            idx_w defines the current position's number should be re-written or not
            idx_r goes through entire array until find out the unseen number
        
        time = O(n)
        space = O(1), in-place manipulation
        """

        idx_w = 1
        for idx_r in range(1, len(nums)):
            if nums[idx_r] != nums[idx_w - 1]:
                nums[idx_w] = nums[idx_r]
                idx_w += 1
        
        return idx_w


removeDuplicates = Solution().removeDuplicates


def test_removeDuplicates():
    # LeetCode examples
    assert removeDuplicates([1, 1, 2]) == 2
    assert removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5

    assert removeDuplicates([1]) == 1
    assert removeDuplicates([0, 1, 4, 4, 5, 6, 6]) == 5
    assert removeDuplicates([-3, -3, -1, 0, 0, 3, 5, 5]) == 5


    print("All tests passed")


if __name__ == "__main__":
    test_removeDuplicates()
