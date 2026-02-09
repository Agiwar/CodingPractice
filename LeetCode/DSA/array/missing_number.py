from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Given n number, then we have a int series in [0, n], [ and ] means included,
            so given 6, the series is 0, 1, 2, 3, 4, 5, 6

        Now the nums array contains the int series, but just misses a int number which is in this series,
            and the nums array is not sorted, no any duplicates, find out that missing number
            e.g., given 8 -> 0, 1, 2, 3, 4, 5, 6, 7, 8 -> [4, 1, 8, 2, 3, 6, 7, 0] -> 5

        And the n value is equal to nums.length,
            n has minimum value of 1, series is 0, 1, if nums = [1, 0], then missing number is 2
            so the nums array has at least length of 2, this guarantees the returned result must have a missing number

        The main idea behind code is I do summation of given series, and given input nums array,
            the missing number is just the series summation minus nums summation

        time = O(n)
        space = O(1)
        """

        return sum(range(len(nums) + 1)) - sum(nums)


missingNumber = Solution().missingNumber

def test_missingNumber():
    assert missingNumber([3,0,1]) == 2
    assert missingNumber([0,1]) == 2
    assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8

    # Edge cases
    assert missingNumber([1, 0]) == 2
    assert missingNumber([1, 2]) == 0
    assert missingNumber([2, 5, 3, 6, 0, 4]) == 1
    assert missingNumber([4, 1, 8, 2, 3, 6, 7, 0]) == 5


    print("All tests passed")

if __name__ == "__main__":
    test_missingNumber()
