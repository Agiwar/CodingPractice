class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        s = "".join(filter(str.isalnum, s.lower()))
        return s == s[::-1]