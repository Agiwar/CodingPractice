class Solution:
    def binary_search(self, arr: list[int], target: int) -> int:
        l_pt, r_pt = 0, len(arr) - 1
        
        while l_pt <= r_pt:
            m_pt = (r_pt - l_pt) // 2 + l_pt
            
            if arr[m_pt] > target:
                r_pt = m_pt - 1
            
            elif arr[m_pt] < target:
                l_pt = m_pt + 1
            
            else:
                return m_pt
        
        return -1


binary_search = Solution().binary_search

def test_binary_search():
    # Basic cases
    assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
    assert binary_search([1, 2, 3, 4, 5, 6], 1) == 0
    assert binary_search([1, 2, 3, 4, 5, 6], 6) == 5

    # Not found
    assert binary_search([1, 2, 3, 4, 5, 6], 7) == -1
    assert binary_search([1, 2, 3, 4, 5, 6], 0) == -1

    # Edge cases
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1

    print("All tests passed")

if __name__ == "__main__":
    test_binary_search()
