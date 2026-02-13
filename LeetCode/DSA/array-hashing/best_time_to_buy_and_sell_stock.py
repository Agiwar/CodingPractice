from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The max profit from investing stock is buy in with low price, sell out with high price

        The main idea behind code is that
            we track the current price is strictly less than the last buy's price,
            if yes, a lower price we found, so need to pick this value to buy
            and there's a sell pointer going through entire prices
            before the next day coming, calculate the current profit is max or not
            note buy and sell can't happen on the same day,
            so if prices.length is 1, which we can only buy, can't sell, no profit get
            initialize the max profit is zero
        
        time = O(n)
        space = O(1)
        """

        n = len(prices)
        if n == 1:
            return 0
        
        buy = prices[0]
        max_profit = 0

        for sell_day in range(1, n):
            if (sell := prices[sell_day]) < buy:
                buy = sell
            
            max_profit = max(max_profit, sell - buy)
        return max_profit
        

maxProfit = Solution().maxProfit

def test_maxProfit():
    # LeetCode examples
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([7,6,4,3,1]) == 0

    # Edge cases (write your own)
    assert maxProfit([1, 3, 4, 6, 7]) == 6
    assert maxProfit([7, 1, 8, 3, 2]) == 7
    assert maxProfit([4, 3, 2, 10]) == 8
    assert maxProfit([5, 5, 5]) == 0
    assert maxProfit([1, 1, 5, 5]) == 4
    assert maxProfit([2, 5, 1, 8]) == 7

    print("All tests passed")

if __name__ == "__main__":
    test_maxProfit()
