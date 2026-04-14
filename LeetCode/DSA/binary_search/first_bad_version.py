# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


bad = 0


def isBadVersion(version: int) -> bool:
    return version >= bad


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l_pt, r_pt = 1, n
        while l_pt < r_pt:
            m_pt = (r_pt - l_pt) // 2 + l_pt
            
            if not isBadVersion(m_pt):
                l_pt = m_pt + 1
            
            else:
                r_pt = m_pt
        
        return r_pt


firstBadVersion = Solution().firstBadVersion

def test_firstBadVersion():
    # LeetCode Example 1: n = 5, bad = 4
    global bad
    
    bad = 4
    assert firstBadVersion(5) == 4

    # LeetCode Example 2: n = 1, bad = 1
    bad = 1
    assert firstBadVersion(1) == 1

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_firstBadVersion()
