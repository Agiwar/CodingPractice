from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        The s.length must have a minimum length value of 1, so if len(s) == 1, return True regardless of empty string.

        The main idea behind my code is using two pointer method,
            one is from the first alphanumeric char, the other is from the last one.
            then moving left and right pointer respectively simultaneously,
            left is move forward one, right is backforward 1
            before traversing, need to handle the input string to contain alphanumeric char only

        time = O(n)
        space = O(1)
        """

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


isPalindrome = Solution().isPalindrome

def test_isPalindrome():
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome(" ") == True

    # Edge cases
    assert isPalindrome("a") == True
    assert isPalindrome("A") == True
    assert isPalindrome("aA") == True
    assert isPalindrome("0") == True
    assert isPalindrome("A5") == False
    assert isPalindrome("2002") == True
    assert isPalindrome("20021111") == False


    print("All tests passed")

if __name__ == "__main__":
    test_isPalindrome()
