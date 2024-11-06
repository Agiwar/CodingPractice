from typing import List


class Solution1:
    def rob(self, nums: List[int]) -> int:
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