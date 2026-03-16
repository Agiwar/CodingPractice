from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        time = O(n * k * log k), k is max length of each word
        space = O(n * k), store n words, each word has maximum length of k
        """
        
        from collections import defaultdict
        
        str_occurs = defaultdict(list)

        for word in strs:
            group = "".join(sorted(word))
            str_occurs[group].append(word)
        
        return list(str_occurs.values())

groupAnagrams = Solution().groupAnagrams

def test_groupAnagrams():
    # LeetCode examples
    result = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert sorted([sorted(g) for g in result]) == sorted([sorted(g) for g in expected])

    result = groupAnagrams([""])
    assert result == [[""]]

    result = groupAnagrams(["a"])
    assert result == [["a"]]

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_groupAnagrams()
