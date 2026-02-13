from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        The key concept behind the code is
        calculate the difference between current number and target.
        
        For each current number while looping, store its difference by target in a hashmap,
        and if the current which is the seen number's difference in hashmap, that's the answer.

        nums.length is at least 2, must have an exactly solution (num1 + num2)

        time = O(n)
        space = O(n) cuz need to return number's index, so need a hashmap to store index
            regardless of sorted input array < sorting takes O(n * log n) >
        
        follow-up: what if input array is sorted, consider using two-pointer,
            so the time = O(n), space(1) due to unnecessary index hashmap 
        """

        diff_map = {}
        for idx, num in enumerate(nums):
            if num in diff_map:
                return [diff_map[num], idx]
            diff_map[target - num] = idx



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
