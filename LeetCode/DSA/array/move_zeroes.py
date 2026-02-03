from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[k] = nums[idx]
                k += 1
        
        nums[k:] = [0] * (len(nums) - k)


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
