class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        res = ""
        res_len = 0

        for i in range(len(s)):
            # odd length: expand out from a center
            L, R = i, i

            # when pointers are inbound, and char are the same (cuz need to be palindromic string)
            while L >= 0 and R < len(s) and s[L] == s[R]:

                # check this sug string length
                if (R - L + 1) > res_len:
                    res = s[L:R+1]
                    res_len = R - L + 1
                
                L -= 1
                R += 1
            
            # even length: same code with odd lenth part, just control the pointer
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > res_len:
                    res = s[L:R+1]
                    res_len = R - L + 1
                
                L -= 1
                R += 1

        return res
