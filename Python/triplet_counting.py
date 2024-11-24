from typing import List


def count_triplets(nums: List[int], k: int) -> int:
    if not nums or len(nums) < 3: return 0

    nums.sort()
    ct = 0

    for idx in range(len(nums) - 2):
        L = idx + 1
        R = len(nums) - 1

        while L < R:
            three_sum = nums[idx] + nums[L] + nums[R]

            if three_sum > k:
                R -= 1
            elif three_sum < k:
                L += 1
            else:
                ct += 1
                L += 1

    return ct