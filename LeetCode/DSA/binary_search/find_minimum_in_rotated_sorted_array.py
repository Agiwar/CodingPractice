class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        using binary search the min number from nums,
            if middle pointer's number > right pointer's number,
            then the min number must be in right halve side,
            so left pointer = middle pointer + 1
            if middle pointer's number < right pointer's number,
            then the min number must be in left halve side,
            so right pointer = middle pointer, note that this middle pointer's value may be minimum

        time = O(log n), n is nums.length
        space = O(1)
        """
        
        l_pt = 0
        r_pt = len(nums) - 1
        
        while l_pt < r_pt:
            m_pt = (r_pt - l_pt) // 2 + l_pt
            
            if nums[m_pt] > nums[r_pt]:
                l_pt = m_pt + 1
            
            elif nums[m_pt] < nums[r_pt]:
                r_pt = m_pt
        
        return nums[l_pt]



findMin = Solution().findMin

def test_findMin():
    # LeetCode examples
    assert findMin([3, 4, 5, 1, 2]) == 1
    assert findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert findMin([11, 13, 15, 17]) == 11

    # Edge cases
    assert findMin([7, 1, 3, 5]) == 1
    assert findMin([1]) == 1
    assert findMin([1, 2]) == 1
    assert findMin([2, 1]) == 1
    assert findMin([1, 2, 3, 4]) == 1
    assert findMin([99, 10, 55, 62]) == 10
    assert findMin([11, 22, 33, 1, 2, 3]) == 1


    print("All tests passed")

if __name__ == "__main__":
    test_findMin()
