from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        The input array is not sorted, but the requirement is siple
            just move all even coming before all odd
        
        Define writer (idx_w) and reader (idx_r), respectively
            idx_w keeps tracking the current value is odd or not
            idx_r goes through entire array until find out the even number
            to replace the current odd value
        
        The main idea behind code is using swap to change the position of odd and even
        If input array has length of 1, can directly the original input

        time = O(n)
        space = O(1)
        """

        n = len(nums)
        if n == 1:
            return nums
        
        idx_w = 0
        for idx_r in range(n):
            if nums[idx_r] % 2 == 0:
                nums[idx_w], nums[idx_r] = nums[idx_r], nums[idx_w]
                idx_w += 1
        
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
