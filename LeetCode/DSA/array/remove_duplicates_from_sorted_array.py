from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [1, 1, 2]  >>  k = 2, nums = [1, 2]
        # nums = [0,0,1,1,1,2,2,3,3,4]  >>  k = 5, nums = [0, 1, 2, 3, 4]
        
        # len(nums) must be greater or equal to 1, so if nums = [1]  >>  k = 1, nums = [1]
        # must have k = 1

        # nums is orders, if nums = [0, 1, 4, 4, 5, 6, 6]  >>  k = 5, nums = [0, 1, 4, 5, 6]
        # nums = [-3, -3, -1, 0, 0, 3, 5, 5]  >>  k = 5, nums = [-3, -1, 0, 3, 5]

        # below ia not counting correct, cuz below is only do DEDUPLICATE
        # if len(nums) == 1:
        #     return 1

        # k = 1
        # for idx in range(1, len(nums)):
        #     if nums[idx - 1] != nums[idx]:
        #         nums[k] = nums[idx]
        #         k += 1

        # return run
        
        # below is the generic pattern for such remove duplicates question
        if len(nums) == 1:
            return 1
        
        k = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[k - 1]:
                nums[k] = nums[idx]
                k += 1
        
        return k


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
