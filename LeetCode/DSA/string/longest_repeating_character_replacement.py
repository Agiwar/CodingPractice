class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        define two pointers, one is traversing input string,
            the other is used for representing the current repeating char's index,
            during traversal, store each char's occur,
            and select the most common appeared char to be substring's membership,
            and using that two pointers to determine the current window size which is r_pt - l_pt + 1,
            the current window size minus the most common appeared char's occur's value,
            this result represents the cost, i.e., how many non-most-common-appeared chars there are,
            that we need to do replacement, this cost depends on k value,
            if cost <= k, perfect, we can replace them all,
            if cost > k, which means we do replacements too many times,
            so need to reduce window size (this means how many efforts we do replacement)
            if window size is smaller, we can do fewer times replacements,
            and the r_pt always increases, so the only one way to reduce window size is
            make l_pt smaller as possible as we can,
            cuz can't guarantee reduce l_pt by one is already in our expected window size,
            and as long as moving l_pt one step, after moving, need to subtract that char's occur by one
            
        time = O(n), n is s.length
        space = O(1), all keys are uppercase english chars which is 26
        """
        
        from collections import defaultdict
        
        
        char_occur = defaultdict(int)
        l_pt = 0
        max_len = 0
        max_occur = 0
        
        for r_pt, char in enumerate(s):
            char_occur[char] += 1
            max_occur = max(max_occur, char_occur[char])
            
            while (window_size := r_pt - l_pt + 1) - max_occur > k:
                char_occur[s[l_pt]] -= 1
                l_pt += 1
            
            max_len = max(max_len, window_size)
        
        return max_len
        

characterReplacement = Solution().characterReplacement

def test_characterReplacement():
    # LeetCode examples
    assert characterReplacement("ABAB", 2) == 4
    assert characterReplacement("AABABBA", 1) == 4

    # Edge cases
    assert characterReplacement("ABAB", 0) == 1
    assert characterReplacement("A", 0) == 1
    assert characterReplacement("ABAB", 1) == 3
    assert characterReplacement("AABABBA", 0) == 2
    assert characterReplacement("AABABBA", 2) == 5
    assert characterReplacement("BAAAB", 1) == 4
    assert characterReplacement("AABCAAD", 1) == 3
    assert characterReplacement("AABCAAD", 2) == 6
    assert characterReplacement("BCCB", 1) == 3


    print("All tests passed")

if __name__ == "__main__":
    test_characterReplacement()
