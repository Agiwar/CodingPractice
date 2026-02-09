from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Given a height array which is representing the wall's height at specific position

        There must be 2 walls but the wall's hright may be zero,
            which means there's no any water could be stored.

        The max area the container can store is
            calculate the area by wall's height * wall's interval for the current two walls
        
        Define two walls' index, left wall (wall_L) and right wall (wall_w), respectively
            initial max_area is zero
            and when wall_L's height i strictly less than wall_R's,
            then move wall_L by one interval, cuz there's an chance to get higher wall_L
            otherwise move wall_R by minus one interval 
            for each looping, calculate the max_area which is 
            compared with current max_area and the current_area
        
        Note that wall_L cannot be overlapped with wall_R
        """

        wall_L = 0
        wall_R = len(height) - 1
        max_area = 0

        while wall_L < wall_R:
            wall_height = min(height[wall_L], height[wall_R])
            interval = wall_R - wall_L
            max_area = max(max_area, wall_height * interval)

            if height[wall_L] < height[wall_R]:
                wall_L += 1
            else:
                wall_R -= 1
        
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
