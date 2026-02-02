from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        time = O(n)
        space = O(n)
        """
        n = len(nums)
        ans = [0] * (n * 2)
        for idx in range(n):
            ans[idx], ans[idx + n] = nums[idx], nums[idx]
        
        return ans


getConcatenation = Solution().getConcatenation


def test_getConcatenation():
    # LeetCode examples
    assert getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]

    # Edge cases (write your own)
    assert getConcatenation([1]) == [1, 1]
    assert getConcatenation([1, 2]) == [1, 2, 1, 2]
    assert getConcatenation([9, 2, 8, 1, 1]) == [9, 2, 8, 1, 1, 9, 2, 8, 1, 1]

    print("All tests passed")


if __name__ == "__main__":
    test_getConcatenation()
