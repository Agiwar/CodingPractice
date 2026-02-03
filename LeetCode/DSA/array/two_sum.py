from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_diff = {}
        for idx, num in enumerate(nums):
            if num in target_diff:
                return [target_diff[num], idx]
            target_diff[target - num] = idx



twoSum = Solution().twoSum


def test_twoSum():
    # LeetCode examples
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]

    # Edge cases (write your own)

    print("All tests passed")


if __name__ == "__main__":
    test_twoSum()
