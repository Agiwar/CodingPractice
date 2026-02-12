from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        nums.length must have minimum length of 2, and there must be one exact one solution,
            os if len(nums) == 2, answer is nums[1, 2] anyway

        nums array is ordered asc, return is return the expectation number of what order, first, second, etc not index

        the main idea behind code is using two pointer from both ends, cuz nums is sorted, calculate the current value
            if larger, move right backfowrad, if less move left forward, if equal to, this is answer

        time = O(n)
        space = O(1)
        """

        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1

            elif numbers[left] + numbers[right] < target:
                left += 1

            else:
                return [left + 1, right + 1]


twoSum = Solution().twoSum

def test_twoSum():
    assert twoSum([2,7,11,15], 9) == [1,2]
    assert twoSum([2,3,4], 6) == [1,3]
    assert twoSum([-1,0], -1) == [1,2]

    # Edge cases
    assert twoSum([-1, 0, 1], 0) == [1, 3]
    assert twoSum([-1, -1, -1, 0, 1], 0) == [1, 5]
    assert twoSum([-1, -1, -1, 0, 1], -2) == [1, 3]
    assert twoSum([1, 2], 3) == [1, 2]


    print("All tests passed")

if __name__ == "__main__":
    test_twoSum()
