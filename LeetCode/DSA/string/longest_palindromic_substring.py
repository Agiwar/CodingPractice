class Solution:
    def _get_palindrome(self, s: str, l_pt: int, r_pt: int) -> str:
        while l_pt >= 0 and r_pt < len(s) and s[l_pt] == s[r_pt]:            
            l_pt -= 1
            r_pt += 1
        
        return s[(l_pt + 1):r_pt]
    
    
    def longestPalindrome(self, s: str) -> str:
        """
        to determine a string is palindrome string or not,
            when traversing the string s, define the current char as center,
            and expand left and right respectively,
            to check continue traversing char is keeping the same char,
            so define two pointers to represent the expanding pointer from center,
            the boundary of stopping expanding is when these two are out of index,
            there're two cases, one is if the length of substring is odd, the other is even,
            if odd, the two pointers start at the same point which is center,
            if even, left and right are next to each other not at the same center,
            so both of them needed to be compared,
            do determine the length of palindrome is based on substring not input s

        time = O(n^2), n is s.length
        space = O(m), m is longestPalindromeSubstring.length, worst case is m = n
        """
        
        n = len(s)
        max_palindrome = s[0]
        
        for idx in range(n):
            odd_palindrome = self._get_palindrome(s, idx, idx)
            even_palindrome = self._get_palindrome(s, idx, idx + 1)
            
            max_palindrome = max(
                max_palindrome,
                odd_palindrome,
                even_palindrome,
                key=len,
            )
        
        return max_palindrome


longestPalindrome = Solution().longestPalindrome

def test_longestPalindrome():
    assert longestPalindrome("babad") in ["bab", "aba"]
    assert longestPalindrome("cbbd") == "bb"

    # Edge cases

    print("All tests passed")
    assert longestPalindrome("0") == "0"
    assert longestPalindrome("101") == "101"
    assert longestPalindrome("ba1aB") == "a1a"
    assert longestPalindrome("Google") == "oo"
    assert longestPalindrome("aabba") == "abba"


if __name__ == "__main__":
    test_longestPalindrome()
