class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        to find out the first unique char of given string, need to traverse the whole string,
            we may not sure if the current char may not appear again,

        the main idea behind the code is using hashmap to store any seen char and its occurrence,
            edge case is if input string has length of 1, directly its index,
            cuz itself is a unique char as well

        time = O(n), n is s.length
        space = O(1), only storing 26 chars
        """
        
        if len(s) == 1:
            return 0


        from collections import defaultdict


        char_occur = defaultdict(int)
        for char in s:
            char_occur[char] += 1
        
        return next((idx for idx, char in enumerate(s) if char_occur[char] == 1), -1)


firstUniqChar = Solution().firstUniqChar

def test_firstUniqChar():
    assert firstUniqChar("leetcode") == 0
    assert firstUniqChar("loveleetcode") == 2
    assert firstUniqChar("aabb") == -1

    # Edge cases
    assert firstUniqChar("z") == 0
    assert firstUniqChar("chatgpt") == 0
    assert firstUniqChar("google") == 4
    assert firstUniqChar("abcdefg") == 0
    assert firstUniqChar("abab") == -1
    assert firstUniqChar("zz") == -1


    print("All tests passed")

if __name__ == "__main__":
    test_firstUniqChar()
