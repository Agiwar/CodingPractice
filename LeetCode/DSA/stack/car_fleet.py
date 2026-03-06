from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass

carFleet = Solution().carFleet

def test_carFleet():
    # LeetCode examples
    assert carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
    assert carFleet(10, [3], [3]) == 1
    assert carFleet(100, [0,2,4], [4,2,1]) == 1

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_carFleet()
