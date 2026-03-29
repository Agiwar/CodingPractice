from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        this question is asking how bucket sort algorithm works,
            if the input array is bounded, and numbers in array is within a specific range,
            create a bucket to store the number's occurrence,
            then looping these occurrences, in-place modify input array by index with number's occurrence

        time = O(n),
        space = O(3), 3 represents three types of color, so it's constant memory
        """

        buckets = [0, 0, 0]
        for num in nums:
            buckets[num] += 1

        w_pt = 0
        for bucket in range(3):
            for _ in range(buckets[bucket]):
                nums[w_pt] = bucket
                w_pt += 1


sortColors = Solution().sortColors

def test_sortColors():
    # LeetCode examples
    nums1 = [2, 0, 2, 1, 1, 0]
    sortColors(nums1)
    assert nums1 == [0, 0, 1, 1, 2, 2]

    nums2 = [2, 0, 1]
    sortColors(nums2)
    assert nums2 == [0, 1, 2]

    # Edge cases
    nums = [0]
    sortColors(nums)
    assert nums == [0]

    nums = [1]
    sortColors(nums)
    assert nums == [1]

    nums = [2]
    sortColors(nums)
    assert nums == [2]

    nums = [2, 1, 0]
    sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [0, 1, 2]
    sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [0, 1, 2, 1, 0]
    sortColors(nums)
    assert nums == [0, 0, 1, 1, 2]


    print("All tests passed")

if __name__ == "__main__":
    test_sortColors()
