from typing import List


class Solution1:
    # dynamic programming
    # time = O(n^2)
    # space = O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)


class Solution2:
    # binary search
    # time = O(n * log n)
    # space = O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def binary_search(arr: List[int], target: int) -> int:
            L = 0
            R = len(arr) - 1
            
            while L <= R:
                m = L + (R - L) // 2
                
                if arr[m] < target:
                    L = m + 1
                elif arr[m] > target:
                    R = m - 1
                else:
                    return m
            
            return L
            
        
        LIS = [nums[0]]
        
        for num in nums[1:]:
            if num > LIS[-1]:
                LIS.append(num)
            else:
                idx = binary_search(LIS, num)
                LIS[idx] = num
        
        return len(LIS)