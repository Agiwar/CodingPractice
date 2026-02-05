from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time = O(n)
        space = O(1)
        """
        if len(prices) == 1:
            return 0
        
        buy = prices[0]
        profit = 0
        for sell_day in range(1, len(prices)):
            if (sell := prices[sell_day]) < buy:
                buy = sell
            
            profit = max(profit, sell - buy)
        return profit or 0
        

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
