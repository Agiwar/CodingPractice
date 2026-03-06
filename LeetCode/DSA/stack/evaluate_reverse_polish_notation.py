from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pass

evalRPN = Solution().evalRPN

def test_evalRPN():
    # LeetCode examples
    assert evalRPN(["2","1","+","3","*"]) == 9
    assert evalRPN(["4","13","5","/","+"]) == 6
    assert evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_evalRPN()
