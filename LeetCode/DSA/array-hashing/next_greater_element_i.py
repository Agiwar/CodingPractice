from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        there's no duplicate in nums1, nums2 either, each num has its exact index which isn't ambiguous
            and nums1 is a subset of nums2, so num in nums1 must be in nums2

        the main idea behind the code is initialize ans[-1] * len(nums1), then traversing nums1,
            to check if curr num1 from nums1 hits max(nums2)
            or the index of num1 in nums2 hits its max, if one of them is yes, do nothing
            otherwise, traversing that index plus by one, to get the subarray, say, subnums2
            trying to find out the first number value is greater than num1,
            if get it, replace curr num1's index corresponding to the index in ans with this "greater value",
            otherwise do nothing

        time = O(m * n), m is nums1.length, n is nums2.length
        space = O(n)
        """

        max_num2 = max(nums2)
        max_num2_idx = len(nums2) - 1
        nums2_idx_map = {val: idx for idx, val in enumerate(nums2)}

        ans = [-1] * len(nums1)
        for idx1, num1 in enumerate(nums1):
            if num1 == max_num2 or nums2_idx_map[num1] == max_num2_idx:
                continue

            for num in nums2[nums2_idx_map[num1] + 1:]:
                if num > num1:
                    ans[idx1] = num
                    break

        return ans


nextGreaterElement = Solution().nextGreaterElement

def test_nextGreaterElement():
    assert nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
    assert nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]

    # Edge cases
    assert nextGreaterElement([0], [0]) == [-1]
    assert nextGreaterElement([0], [1, 0]) == [-1]
    assert nextGreaterElement([0], [0, 1]) == [1]
    assert nextGreaterElement([0, -1, 2], [2, 0, -1]) == [-1, -1, -1]
    assert nextGreaterElement([-1, 0, 2], [2, 0, -1]) == [-1, -1, -1]
    assert nextGreaterElement([-1, 0, 2], [-1, 0, 2]) == [0, 2, -1]
    assert nextGreaterElement([-1, 0, 2], [2, 0, -1]) == [-1, -1, -1]
    assert nextGreaterElement([-1, -2, -3], [-3, 3, 2, -2, -1]) == [-1, -1, 3]
    assert nextGreaterElement([-3, -2, -1], [-3, 3, 2, -2, -1]) == [3, -1, -1]
    assert nextGreaterElement([-2, -1, -3], [-3, 3, 2, -2, -1]) == [-1, -1, 3]


    print("All tests passed")

if __name__ == "__main__":
    test_nextGreaterElement()
