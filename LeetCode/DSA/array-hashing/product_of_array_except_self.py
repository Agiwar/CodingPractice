from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        the number in nums may be negative, zero, positive number
            when traversing array, the current index value should be the product value of all numbers
            excluding current number

        as number may be zero, zero multiples any number will return zero, so if there's one zero in nums,
            the product values are all zero across those index excluding the zero-value index, if multiple zeroes,
            then directly return [0] with length of nums.length

        the main idea behind code is if at index i, then nums[i] should be the value
            which is product of numbers before i multiply product of numbers after i,
            nums[i] = product of nums[:i] * product of nums[i + 1:],
            i.e., prefix product * suffix product at i position
            note that at the both ends, there's no prefix product at beginning, also no suffix product at the end

        time = O(n)
        space = O(1)
        """

        n = len(nums)
        res = [1] * n

        L_product = 1
        for L in range(n):
            res[L] = L_product
            L_product *= nums[L]

        R_product = 1
        for R in range(n - 1, -1, -1):
            res[R] *= R_product
            R_product *= nums[R]

        return res


productExceptSelf = Solution().productExceptSelf

def test_productExceptSelf():
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

    # Edge cases
    assert productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert productExceptSelf([10, 20, 30]) == [600, 300, 200]
    assert productExceptSelf([-1, 2, 9, 0, 1, 0]) == [0, 0, 0, 0, 0, 0]
    assert productExceptSelf([-1, 2, 9, 0, 1, -2]) == [0, 0, 0, 36, 0, 0]
    assert productExceptSelf([0, 1]) == [1, 0]
    assert productExceptSelf([0, 0, 1]) == [0, 0, 0]
    assert productExceptSelf([0, 1, -4, 2]) == [-8, 0, 0, 0]
    assert productExceptSelf([10, 1, -4, 2]) == [-8, -80, 20, -40]
    assert productExceptSelf([0, 0]) == [0, 0]
    assert productExceptSelf([-1, -2, -3, -4]) == [-24, -12, -8, -6]
    assert productExceptSelf([-1, -2, 0, -3, -4]) == [0, 0, 24, 0, 0]



    print("All tests passed")

if __name__ == "__main__":
    test_productExceptSelf()
