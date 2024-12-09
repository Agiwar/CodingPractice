from collections import Counter, defaultdict
from typing import Dict


class Solution1:
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


class Solution2:
    # Use Python's built-in defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_occur: Dict[str, int] = defaultdict(int)
        for c in s:
            char_occur[c] += 1
        
        for c in t:
            if c not in char_occur:
                return False
            
            char_occur[c] -= 1
            
            if char_occur[c] < 0:
                return False
        
        return (
            all(occur == 0 for occur in char_occur.values())
        )

class Solution3:
    # Use Python's built-in Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        main_string_occur = dict(Counter(s))
        
        for char in t:
            if char not in main_string_occur:
                return False
            
            main_string_occur[char] -= 1
            
            if main_string_occur[char] < 0:
                return False
        
        return all(occur == 0 for occur in main_string_occur.values())


class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)