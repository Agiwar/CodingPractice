from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        m or n may be zero, but m + n must be greater or equal to 1,
            number in array may have negative or zero
            nums1's length is m + n which must be greater or equal to 1,
            so nums1 is never an empty list,

        the main idea behind code is the final result is only able to
            in-place modify nums1 which returns nothing, nums1 must have length m + n,
            so can directly assign value without any out of index concerns,
            and the last non-zero number must be at m -1 index,
            and no matter nums2 has zeroes or not, nums2 is sorted, zero must be at first index,
            so always get the last value to compare value and pick the greater one,
            and move backfoward -1 for that array whose last valid number is selected

        time = O(m + n)
        space = O(1)
        """

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1




merge = Solution().merge

def test_merge():
    nums1 = [1,2,3,0,0,0]
    merge(nums1, 3, [2,5,6], 3)
    assert nums1 == [1,2,2,3,5,6]

    nums1 = [1]
    merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    # Edge cases
    nums1 = [0, 0]
    merge(nums1, 0, [1, 2], 2)
    assert nums1 == [1, 2]

    nums1 = [1, 3, 7, 0, 0, 0]
    merge(nums1, 3, [2, 4, 6], 3)
    assert nums1 == [1, 2, 3, 4, 6, 7]

    nums1 = [-1, 4, 0, 0, 0, 0]
    merge(nums1, 2, [-2, 1, 3, 3], 4)
    assert nums1 == [-2, -1, 1, 3, 3, 4]

    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [-1, -1, 3], 3)
    assert nums1 == [-1, -1, 1, 2, 3, 3]

    nums1 = [-3, 3, 0, 0]
    merge(nums1, 2, [0, 0], 2)
    assert nums1 == [-3, 0, 0, 3]

    nums1 = [10, 0]
    merge(nums1, 1, [0], 1)
    assert nums1 == [0, 10]


    print("All tests passed")

if __name__ == "__main__":
    test_merge()
