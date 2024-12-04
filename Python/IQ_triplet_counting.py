from typing import List


def count_triplets(nums: List[int], k: int) -> int:
    if not nums or len(nums) < 3: return 0
    
    nums.sort()

    ct = 0
    for idx in range(len(nums)):
        left = idx + 1
        right = len(nums) - 1

        while left < right:
            if (three_sums := nums[idx] + nums[left] + nums[right]) < k:
                left += 1
            elif three_sums > k:
                right -= 1
            else:
                ct += 1
                left += 1
    
    return ct