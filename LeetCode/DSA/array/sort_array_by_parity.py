from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        time = O(n)
        space = O(1)
        """
        # [3, 1, 2, 4] -> [2, 4, 3, 1] the order doesn’t matter, as long as even number come before odd
        # define writer pointer and reader pointer,
        # check the current reader number can replace the value of writer’s position
        # the writer position must be on the odd number, and reader position has the value of even number

        if len(nums) == 1:
            return nums
        
        idx_writer = 0
        for idx_reader in range(len(nums)):
            if nums[idx_reader] % 2 == 0:
                nums[idx_writer], nums[idx_reader] = nums[idx_reader], nums[idx_writer]
                idx_writer += 1
        
        return nums

sortArrayByParity = Solution().sortArrayByParity


def test_sortArrayByParity():
    # LeetCode examples
    result1 = sortArrayByParity([3, 1, 2, 4])
    assert all(x % 2 == 0 for x in result1[:2]) and all(x % 2 == 1 for x in result1[2:])
    
    result2 = sortArrayByParity([0])
    assert result2 == [0]

    # Edge cases (write your own)
    result3 = sortArrayByParity([0])
    assert result3 == [0]
    
    result4 = sortArrayByParity([1])
    assert result4 == [1] 

    result5 = sortArrayByParity([4])
    assert result5 == [4]

    result6 = sortArrayByParity([3, 2, 4, 1, 2, 2, 0])
    assert result6 == [2, 4, 2, 2, 0, 1, 3]
    
    result7 = sortArrayByParity([4, 4, 1, 1, 1, 2, 0, 0])
    assert result7 == [4, 4, 2, 0, 0, 1, 1, 1]

    result8 = sortArrayByParity([2, 4, 1, 1, 5, 3, 0, 0])
    assert result8 == [2, 4, 0, 0, 5, 3, 1, 1]

    print("All tests passed")


if __name__ == "__main__":
    test_sortArrayByParity()
