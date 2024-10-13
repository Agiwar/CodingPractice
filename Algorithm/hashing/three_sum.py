from typing import List


class Solution:
    # space = O(n * log n) + O(n^2) = O(n^2)
    # space = O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # In order to use two pointer
        res = []
        
        # i != j and j != k and k != i
        for idx in range(len(nums)):
            
            # avoid duplicate when iterating
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            L = idx + 1
            R = len(nums) - 1
            
            while L < R:
                three_sums = nums[idx] + nums[L] + nums[R]
                
                if three_sums < 0:
                    L += 1
                elif three_sums > 0:
                    R -= 1
                else:
                    ans = [nums[idx], nums[L], nums[R]]
                    res.append(ans)
                    
                    L += 1  # continue to check if there's the other candidates
                    
                    # make sure L is inbound, and if nums[L] == nums[L - 1], this means duplicate
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        
        return res