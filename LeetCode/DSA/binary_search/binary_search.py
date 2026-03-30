class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        the input nums is a sorted ascending array, and each num in nums is unique
            define l_pt, r_pt, and the m_pt is the middle position of nums,
            compare m_pt's value with target until find out the solution
        
        time = O(log n), n is nums.length
        space = O(1)
        """
        
        l_pt, r_pt = 0, len(nums) - 1
        
        while l_pt <= r_pt:
            m_pt = (r_pt - l_pt) // 2 + l_pt
            
            if nums[m_pt] > target:
                r_pt = m_pt - 1
            
            elif nums[m_pt] < target:
                l_pt = m_pt + 1
            
            else:
                return m_pt
        
        return -1



search = Solution().search

def test_search():
    # LeetCode examples
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1

    # Edge cases
    assert search([3], 2) == -1
    assert search([-1], 0) == -1
    assert search([-1, 0, 1], 0) == 1
    assert search([-4, -3, -2, -1], 0) == -1
    assert search([-4, -3, -2, -1], -4) == 0
    assert search([-4, -3, -2, -1], -1) == 3
    assert search([-4, -3, -2, -1], -3) == 1
    assert search([2, 4, 6, 7], 1) == -1
    assert search([2, 4, 6, 7], 6) == 2


    print("All tests passed")

if __name__ == "__main__":
    test_search()
