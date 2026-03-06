from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass

generateParenthesis = Solution().generateParenthesis

def test_generateParenthesis():
    # LeetCode examples
    assert sorted(generateParenthesis(3)) == sorted(["((()))","(()())","(())()","()(())","()()()"])
    assert generateParenthesis(1) == ["()"]

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_generateParenthesis()
