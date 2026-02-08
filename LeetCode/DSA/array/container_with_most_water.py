from typing import List

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        time = O(n)
        space = O(1)
        """
        # [1,8,6,2,5,4,8,3,7]-> 49
        # [1, 1] -> 1
        # [0, 1, 2, 3, 4, 5] -> 6
        # [0, 0, 4, 4, 2] -> 4
        # [1, 2, 3, 4, 3, 2, 1] -> 8

        y_L = 0
        y_R = len(height) - 1
        max_area = 0

        while y_L < y_R:
            valid_y = min(height[y_L], height[y_R])
            interval = y_R - y_L
            max_area = max(max_area, interval * valid_y)

            if height[y_L] <= height[y_R]:
                y_L += 1
            else:
                y_R -= 1

        return max_area


maxArea = Solution().maxArea

def test_maxArea():
    # LeetCode examples
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,1]) == 1

    # Edge cases (write your own)
    assert maxArea([0, 1, 2, 3, 4, 5]) == 6
    assert maxArea([0, 0, 4, 4, 2]) == 4
    assert maxArea([1, 2, 3, 4, 3, 2, 1]) == 8

    print("All tests passed")

if __name__ == "__main__":
    test_maxArea()
