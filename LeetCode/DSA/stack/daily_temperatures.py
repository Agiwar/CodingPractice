from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass

dailyTemperatures = Solution().dailyTemperatures

def test_dailyTemperatures():
    # LeetCode examples
    assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    assert dailyTemperatures([30,60,90]) == [1,1,0]

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_dailyTemperatures()
