class Solution:
    def _binary_search(self, nums: list[int], target: int, left: bool) -> int:
        l_pt, r_pt = 0, len(nums) - 1
        idx = -1
        
        while l_pt <= r_pt:
            m_pt = (r_pt - l_pt) // 2 + l_pt
            
            if nums[m_pt] > target:
                r_pt = m_pt - 1
            
            elif nums[m_pt] < target:
                l_pt = m_pt + 1
            
            else:
                idx = m_pt
                
                if left:
                    r_pt = m_pt - 1
                else:
                    l_pt = m_pt + 1
            
        return idx
                    
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        use binary search to find the target value in the array,
            need to return the first and last index of target value,
            there may be target value appearing many times,
            means when doing binary searching to get target index,
            this index may be in the middle, not be always at the both end,
            and the continuous target values must be a sequence with the same values,
            if current value is less than target,
            searching range becomes current index's next one until to last one,
            if current value is greater than target, it becomes zero-index to current index's previous one
            if current value is target, using current index to be cut half, left and right one,
            do twice binary search to get the leftmost index and rightmost one,
            for leftmost one, continue narrowing down right pointer,
            for rightmost one, narrowing down the left one.

        time = O(lon n), n is nums.length
        space = O(1), starting and end index is O(2)
        """

        min_pt = self._binary_search(nums, target, True)
        max_pt = self._binary_search(nums, target, False)
        return [min_pt, max_pt]


searchRange = Solution().searchRange

def test_searchRange():
    # LeetCode examples
    assert searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert searchRange([5,7,7,8,8,10], 6) == [-1,-1]
    assert searchRange([], 0) == [-1,-1]

    # Edge cases
    assert searchRange([1], 1) == [0, 0]
    assert searchRange([1, 1], 1) == [0, 1]
    assert searchRange([-1, 2], 2) == [1, 1]
    assert searchRange([-1, 0, 0, 0, 1, 1, 2], 0) == [1, 3]
    assert searchRange([-1, 0, 1, 1, 1, 1, 2], 1) == [2, 5]
    
    print("All tests passed")


if __name__ == "__main__":
    test_searchRange()
