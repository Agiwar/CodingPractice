from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        time = O(n * log k), k is number of unique number
        space = O(n)
        """
        from collections import Counter
        
        nums_freq = Counter(nums)
        return [x[0] for x in nums_freq.most_common(k)]

topKFrequent = Solution().topKFrequent

def test_topKFrequent():
    assert sorted(topKFrequent([1,1,1,2,2,3], 2)) == [1, 2]
    assert topKFrequent([1], 1) == [1]

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_topKFrequent()
