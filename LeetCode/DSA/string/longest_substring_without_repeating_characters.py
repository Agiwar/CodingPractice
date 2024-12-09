class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        length = 0

        for c in s:
            if c in sub:
                sub = sub.split(c)[1]
            sub += c
            length = max(len(sub), length)

        return length