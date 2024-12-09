from typing import List


class Solution1:
    # Use DFS to find all possibilities of maximum money robbed.
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        rob_money_each_house = {}
        
        
        def max_total_money_robbed(i: int) -> int:
            if i >= len(nums):
                return 0
            
            elif i in rob_money_each_house:
                return rob_money_each_house[i]
            
            rob_current_house = nums[i] + max_total_money_robbed(i + 2)
            skip_current_house = max_total_money_robbed(i + 1)
            
            rob_money_each_house[i] = (
                max(rob_current_house, skip_current_house)
            )
            
            return rob_money_each_house[i]
        
        
        return max_total_money_robbed(0)


class Solution2:
    # Use dp array to store the maximum total money robbed up to the current house.
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            rob_current_house = nums[i] + dp[i - 2]
            skip_current_house = dp[i - 1]
            
            dp[i] = max(rob_current_house, skip_current_house)
        
        return dp[-1]


class Solution3:
    # Just use two variables to represent the maximum money robbed of current house 
    # is determined by the previous two houses' results.
    def rob(self, nums: List[int]) -> int:
        num_of_house = len(nums)
        
        if num_of_house == 1:
            return nums[0]
        
        elif num_of_house == 2:
            return max(nums[0], nums[1])
        
        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in range(2, num_of_house):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
        
        return rob2