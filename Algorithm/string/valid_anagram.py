class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        each_char_occur_in_s = {}
        for c in s:
            each_char_occur_in_s[c] = each_char_occur_in_s.get(c, 0) + 1
        
        for c in t:
            if c not in each_char_occur_in_s:
                return False
            
            each_char_occur_in_s[c] -= 1
            
            if each_char_occur_in_s[c] < 0:
                return False
        
        return (
            all(char_occur == 0 for char_occur in each_char_occur_in_s.values())
        )
