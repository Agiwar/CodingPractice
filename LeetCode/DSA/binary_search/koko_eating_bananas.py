class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        she must eat all bananas with eating speed k within h hours,
            if the current piles of number of bananas is less than k, eat it all, and stop
            then need next hour is coming, she can continue eating the rests or the next pile,
            which means the piles of number of bananas divided by k,
            if there is mod, she needs to wait, so plus 1 hour to continue,
            if the piles of number of bananas is equal to k, no additional a hour required
            based on these criteria, derive the equation below
            the total number of sum(ceil(pile / k)) hours cost for each pile must be within h,
            and get the minimum k to satisfy that equation,
            k belongs to a range [1, max(piles)], k must not be zero, eating nothing otherwise

        the main idea behind the code is that there must be a k value in [1, max(piles)],
            so search k to eat all, where k belongs to [1, max(piles)], until k over h,
            but this is brute force to find any possibilities, time is O(max(piles) * piles),
            assume minimum k can eat all within h, then no need the value incremental by k,
            if k can't eat all, then any values are less than k can't either,
            instead, using binary search the appropriate k which belongs to [1, max(piles)],
            initialize the minimum k as max(piles), cuz this will guarantee she can eat all,
            but if set minimum k is 1, can eat all as well, but never the minimum k,
            cuz it will need more hours to eat all.
        
        time = O(log(max(n)) * n), n is piles.length
        space = O(1)
        """        
        
        n, m = 1, max(piles)
        min_k = m
        
        while n <= m:
            k = (m - n) // 2 + n
            total_hours = sum((pile // k) for pile in piles)
            total_hours += sum(bool(pile % k) for pile in piles)
            
            if total_hours <= h:  # eat may too fast, continue searching smallest one
                min_k = k
                m = k - 1
            
            else:  # eat too slow
                n = k + 1
        
        return min_k


minEatingSpeed = Solution().minEatingSpeed

def test_minEatingSpeed():
    # LeetCode examples
    assert minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

    # Edge cases
    assert minEatingSpeed([3, 6, 7, 11], 4) == 11
    assert minEatingSpeed([3, 6, 7, 11], 6) == 6
    assert minEatingSpeed([30,11,23,4,20], 8) == 15
    assert minEatingSpeed([30,11,23,4,20], 10) == 11
    assert minEatingSpeed([3], 4) == 1
    assert minEatingSpeed([3], 1) == 3
    assert minEatingSpeed([3], 1000) == 1

    print("All tests passed")


if __name__ == "__main__":
    test_minEatingSpeed()
