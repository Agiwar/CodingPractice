class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        traverse whole given string, using dict to store the seen chars,
            define two pointers, one is the start fixed pointer,
            the other is pointer traversing the given string s,
            using dict to store any seen unique char,
            if current char has already existed,
            make sure the first duplicate is in what index
            if it is equal or greater than current fixed pointer, update it by plus one
            cuz exclude the current char, every chars before current char is unique

        time = O(n), n is s.length
        space = O(m), m is longestsubstring.length
        """
        
        if len(s) <= 1:
            return len(s)
        
        seen = {}
        pt = 0
        max_len = 0
        
        for idx, char in enumerate(s):
            if char in seen and seen[char] >= pt:
                pt = seen[char] + 1
                
            seen[char] = idx
            max_len = max(max_len, idx - pt + 1)
        
        return max_len



lengthOfLongestSubstring = Solution().lengthOfLongestSubstring

def test_lengthOfLongestSubstring():
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3

    # Edge cases
    assert lengthOfLongestSubstring("") == 0
    assert lengthOfLongestSubstring(" ") == 1
    assert lengthOfLongestSubstring("  ") == 1
    assert lengthOfLongestSubstring(" $@") == 3
    assert lengthOfLongestSubstring("#$b1b$#") == 4
    assert lengthOfLongestSubstring("LeetCode") == 5
    assert lengthOfLongestSubstring("ChatGPT") == 7
    assert lengthOfLongestSubstring("Google") == 4


    print("All tests passed")

if __name__ == "__main__":
    test_lengthOfLongestSubstring()
