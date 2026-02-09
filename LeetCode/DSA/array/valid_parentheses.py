from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Return True if result meets the requirements, False, otherwise.

        So if the s.length is odd, directly False, cuz the brackets never be paired

        The main idea behind code is create a stack, and go through entire s string,
            if the current bracket is open,
            add is into stack which is needed to be paired by close
            if the current bracket is close,
            check the stack's last bracket is the relevant open bracket
            if yes, then pop last bracket from stack,
            and this will also consume the current close bracket automatically,
            which means if the result if True,
            the input s will be empty and the bracket stack is empty as well.
        
        time = O(n)
        space = O(n), create a brackets paired hashmap + a stack to store bracket from s
        """

        if len(s) % 2 == 1:
            return False
        
        bracket_map = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        unpaired_brackets = []
        for bracket in s:
            if bracket in bracket_map:
                unpaired_brackets.append(bracket)
            
            elif not unpaired_brackets or bracket != bracket_map[unpaired_brackets.pop()]:
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
