from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            price_diff = price - min_price
            max_profit = max(max_profit, price_diff)
            min_price = min(min_price, price)
        
        return max_profit
