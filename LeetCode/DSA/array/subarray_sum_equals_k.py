from typing import List


class Solution1:
    # brute force
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_aub_arr_ct = 0
        
        for i in range(len(nums)):
            curr_sum = 0
            
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                
                if curr_sum == k:
                    total_aub_arr_ct += 1
        
        return total_aub_arr_ct


class Solution2:
    # use a hash map to store the cumulative we've already done,
    # to avoid re-calculating the sum of sub array inside j loop when iterating i loop
    # the curr sum of sub array can be resented as sum(arr[:b]) = sum(arr[:a]) + sum(arr[a:b])
    # if there's a sub array arr[a:b] whose sum is target number k,
    # so the previous cumulative sum of sub array sum(arr[:a]) = sum(arr[:b]) - sum(arr[a:b])
    # which is sum(arr[:a]) = curr_sum - k, and use a hash map to store the occurrence of sum(arr[:a])
    def subarraySum(self, nums: List[int], k: int) -> int:
        # there must be the key cumulative sum = 0 at the beginning 
        prev_cumulative_sum_occur = {0: 1}
        
        curr_sum = 0
        total_aub_arr_ct = 0
        
        for num in nums:
            curr_sum += num
            
            if (prev_cumulative_sum := curr_sum - k) in prev_cumulative_sum_occur:
                total_aub_arr_ct += prev_cumulative_sum_occur[prev_cumulative_sum]
                
            prev_cumulative_sum_occur[curr_sum] = prev_cumulative_sum_occur.get(curr_sum, 0) + 1
        
        return total_aub_arr_ct
