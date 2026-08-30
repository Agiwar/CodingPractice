from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return next(val for val, ct in Counter(nums).items() if ct == 1)


singleNumber = Solution().singleNumber


def test_singleNumber():
    # LeetCode Example 1
    assert singleNumber([2, 2, 1]) == 1

    # LeetCode Example 2
    assert singleNumber([4, 1, 2, 1, 2]) == 4

    # LeetCode Example 3
    assert singleNumber([1]) == 1

    # Edge cases

    # Negative single — guards against abs() / sign assumptions
    assert singleNumber([-1, -1, -2]) == -2

    # Zero is the single — guards against treating 0 as "not found"
    assert singleNumber([1, 1, 0]) == 0

    # Zero appears as a pair, single is elsewhere
    assert singleNumber([0, 0, 5]) == 5

    # Single sits at the very front / very back — position independence
    assert singleNumber([3, 7, 7]) == 3
    assert singleNumber([7, 7, 3]) == 3

    # Mixed signs
    assert singleNumber([-3, 5, -3]) == 5

    # Larger input: 1000 pairs plus one unique, interleaved
    nums = [v for v in range(1, 1001) for _ in range(2)] + [12345]
    assert singleNumber(nums) == 12345

    print("All tests passed")


if __name__ == "__main__":
    test_singleNumber()
