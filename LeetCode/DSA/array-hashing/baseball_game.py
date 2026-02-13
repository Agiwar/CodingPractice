from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        time = O(n + m + m) ~ O(n + m) ~ O(n)
            n = len(operations), m = len(scores), sum() is also O(m)
            n >> m
        
        space = O(m)
        """
        scores = []

        for item in operations:
            if item == "+":
                scores.append(scores[-1] + scores[-2])
            
            elif item == "C":
                scores.pop()
            
            elif item == "D":
                scores.append(scores[-1] * 2)
            
            else:
                scores.append(int(item))
        
        return sum(scores)
                


calPoints = Solution().calPoints


def test_calPoints():
    # LeetCode examples
    assert calPoints(["5", "2", "C", "D", "+"]) == 30
    assert calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert calPoints(["1", "C"]) == 0

    # Edge cases
    assert calPoints(["4", "D"]) == 12
    assert calPoints(["0", "D"]) == 0
    assert calPoints(["1", "D"]) == 3
    assert calPoints(["0", "0", "D", "+"]) == 0
    assert calPoints(["7", "-7", "D", "3", "+", "C", 4, "+"]) == 0

    try:
        calPoints(["C"])
        assert False, "Must be integer."
    except ValueError:
        pass

    try:
        calPoints(["D"])
        assert False, "Must be integer."
    except ValueError:
        pass

    try:
        calPoints(["5", "+"])
        assert False, "Must be integer."
    except ValueError:
        pass

    print("All tests passed")


if __name__ == "__main__":
    test_calPoints()
