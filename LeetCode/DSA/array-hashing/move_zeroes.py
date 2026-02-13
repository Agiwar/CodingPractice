from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        The input nums is not sorted, but the requirement is simple,
            just make all zero-value numbers come after non-zero-value numbers
            but need to keep the original relative order.
        
        Define writer (idx_w) and reader (idx_r), respectively.
            idx_w handles checking the current position's number is zero or not
            idx_r goes through entire array until we find out non-zero
            which can replace that current zero-value number
        
        time = O(n)
        space = (1), in-place manipulation
        """

        idx_w =0
        for idx_r in range(len(nums)):
            if nums[idx_r] != 0:
                nums[idx_w] = nums[idx_r]
                idx_w += 1
        
        nums[idx_w:] = [0] * (len(nums) - idx_w)
        


moveZeroes = Solution().moveZeroes


def test_moveZeroes():
    # LeetCode examples
    nums1 = [0, 1, 0, 3, 12]
    moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0]

    nums2 = [0]
    moveZeroes(nums2)
    assert nums2 == [0]

    # Edge cases (write your own)
    nums3 = [1]
    moveZeroes(nums3)
    assert nums3 == [1]
    
    nums4 = [1, 0]
    moveZeroes(nums4)
    assert nums4 == [1, 0]

    nums5 = [0, 1]
    moveZeroes(nums5)
    assert nums5 == [1, 0]

    nums6 = [-1, 0, 1]
    moveZeroes(nums6)
    assert nums6 == [-1, 1, 0]


    print("All tests passed")


if __name__ == "__main__":
    test_moveZeroes()
