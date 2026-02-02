from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        time = O(n)
        space = O(n)
        """
        if len(s) % 2 == 1:
            return False
        
        brackets_map = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        
        unpaired_brackets = []
        for bracket in s:
            if bracket in brackets_map:
                unpaired_brackets.append(bracket)
            
            elif (
                not unpaired_brackets or
                bracket != brackets_map[unpaired_brackets.pop()]
            ):
                return False
        
        return not unpaired_brackets


isValid = Solution().isValid


def test_isValid():
    # LeetCode examples
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([])") == True

    # Edge cases (write your own)
    assert isValid("(") == False
    assert isValid("(()") == False
    assert isValid("((") == False
    assert isValid("{[]]}") == False
    assert isValid("]{}()") == False
    assert isValid("{}[]()") == True
    assert isValid("{[()]}") == True
    assert isValid("(((([])))") == False

    print("All tests passed")


if __name__ == "__main__":
    test_isValid()
