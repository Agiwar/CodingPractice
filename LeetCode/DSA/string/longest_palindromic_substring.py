class Solution1:
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

                # check this sub string length
                if (R - L + 1) > res_len:
                    res = s[L:R+1]
                    res_len = R - L + 1
                
                L -= 1
                R += 1
            
            # even length: same code with odd length part, just control the pointer
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if (R - L + 1) > res_len:
                    res = s[L:R+1]
                    res_len = R - L + 1
                
                L -= 1
                R += 1

        return res


class Solution2:
    def find_out_longest_palindromic_substring(
        self,
        s: str,
        left_pointer: int,
        right_pointer: int
    ) -> str:
        sub_string = ""
        max_sub_string_length = 0
        
        while (
            left_pointer >= 0 and 
            right_pointer < len(s) and
            s[left_pointer] == s[right_pointer]
        ):
            if (right_pointer - left_pointer + 1) >  max_sub_string_length:
                sub_string = s[left_pointer:(right_pointer + 1)]
                max_sub_string_length = len(sub_string)
            
            left_pointer -= 1
            right_pointer += 1
        
        return sub_string

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        max_palindromic = ""
        for idx in range(len(s)):
            odd_palindromic = self.find_out_longest_palindromic_substring(s, idx, idx)
            even_palindromic = self.find_out_longest_palindromic_substring(s, idx, idx + 1)
            max_palindromic = max(
                max_palindromic,
                odd_palindromic,
                even_palindromic,
                key=len
            )
        
        return max_palindromic