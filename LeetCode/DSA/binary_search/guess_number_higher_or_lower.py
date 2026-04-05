# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


pick: int = 0


def guess(n: int) -> int:
    if n > pick:
        return -1
    elif n < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        the number range [1, n] represents two pointers,
            and use guess API to determine the guessed number correct or not

        time = O(log n)
        space = O(1)
        """
        
        one, two = 1, n
        while one <= two:
            num = (two - one) // 2 + one
            result = guess(num)
            
            if result == -1:
                two = num - 1
            
            elif result == 1:
                one = num + 1
            
            elif result == 0:
                return num

guessNumber = Solution().guessNumber


def test_guessNumber():
    global pick
    
    # LeetCode Example 1: pick = 6, n = 10
    pick = 6
    assert guessNumber(10) == 6

    # LeetCode Example 2: pick = 1, n = 1
    pick = 1
    assert guessNumber(1) == 1

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_guessNumber()
