from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[List[str]]:
        """
        time = O(n * k * log k), k is max length of each word
        space = O(n * k), store n words, each word has maximum length of k
        """
        
        anagrams = defaultdict(list)

        for word in strs:
            group = "".join(sorted(word))
            anagrams[group].append(word)
        
        return list(anagrams.values())

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
