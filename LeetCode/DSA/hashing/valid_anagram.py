from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s and t must have a minimum length of 1, so if both of them are 1, s[0] != t[0], then False
            and obviously, if s.length is not equal to t.length, return False directly

        The main idea behind my code is calculate the occurrence of each char for s and t,
            if the different type of char of occurrence in s and t is the same,
            it means t can be re-arranged in somewhat way to be s

        s = "anagram", t = "nagaram" -> True
        s = "rat", t = "car" -> False
        
        using Counter:
        time = O(n)
        space = O(k), k is number of unique char, but can say O(1),
            cuz letter only contains lowercase english
            
        Follow up: What if the inputs contain Unicode characters?
            How would you adapt your solution to such a case?
        time = O(n)
        space = O(k), k is number of unique char, Counter handles it gracefully
        """

        from collections import Counter
        return Counter(s) == Counter(t)



isAnagram = Solution().isAnagram

def test_isAnagram():
    assert isAnagram("anagram", "nagaram") == True
    assert isAnagram("rat", "car") == False

    # Edge cases
    assert isAnagram("a", "b") == False
    assert isAnagram("ab", "b") == False
    assert isAnagram("aab", "abb") == False
    assert isAnagram("google", "elgoog") == True
    assert isAnagram("xxx", "xxx") == True


    print("All tests passed")

if __name__ == "__main__":
    test_isAnagram()
