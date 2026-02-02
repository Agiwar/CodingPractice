from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        time = O(n)
        space = O(1)
        """
        # [1,1,1,2,2,3]  >>  k = 5, nums = [1, 1, 2, 2, 3]
        # [0,0,1,1,1,1,2,3,3]  >>  k = 7, nums = [0, 0, 1, 1, 2, 3, 3]

        # len(nums) >= 1, so k >= 1, e.g., nums[1]  >>  k = 1, nums = [1]
        # if len(nums) != 1, so there must be 2 number  >>  k at least 2
        # nums[1, 1]  >>  k = 2, nums = [1, 1]
        # nums[1, 2]  >>  k = 2, nums = [1, 2]
        # nums[1, 1, 1]  >>  k = 2 nums = [1, 1]
        # nums[1, 1, 2]  >>  k  = 3, nums = [1, 1, 2]
        # nums[1, 1, 1, 2]  >>  k = 3, nums = [1, 1, 2]
        # nums[1, 1, 2, 2]  >>  k = 4, nums = [1, 1, 2, 2]


        if len(nums) <= 2:
            return len(nums)

        k = 2
        for idx in range(2, len(nums)):
            if nums[idx] != nums[k - 2]:
                nums[k] = nums[idx]
                k += 1

        return k





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
