class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        to find out the longest common prefix,
            use index pointer to represent current char for each iteration,
            if any of the string's current char is not the same with others,
            then iteration stops, return the seen chars so far

        the edge case is that if len(strs) == 1, the result is strs[0] itself regardless of empty string
            and there must not be any space or any special chars,
            each char is either lower-case english letter or empty string

        time = O(m * n), m is the min string length from strs, n is strs.length
        space = O(m)
        """
        
        if len(strs) == 1:
            return strs[0]
        
        min_str = min(strs, key=lambda x: len(x))
        idx = 0
        
        prefix = []
        while idx < len(min_str):
            char = min_str[idx]
            if all(string[idx] == char for string in strs):
                prefix.append(char)
            
            else:
                break
            
            idx += 1
        
        return "".join(prefix)
            


longestCommonPrefix = Solution().longestCommonPrefix

def test_longestCommonPrefix():
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert longestCommonPrefix(["dog","racecar","car"]) == ""

    # Edge cases
    assert longestCommonPrefix([""]) == ""
    assert longestCommonPrefix(["ai"]) == "ai"
    assert longestCommonPrefix(["", "ai"]) == ""
    assert longestCommonPrefix(["ai", "ai"]) == "ai"
    assert longestCommonPrefix(["ai", "bi"]) == ""
    assert longestCommonPrefix(["dockercompose", "dockerfile", "docker"]) == "docker"
    assert longestCommonPrefix(["devops", "mlops"]) == ""
    assert longestCommonPrefix(["devops", "develop", "devenv"]) == "dev"


    print("All tests passed")

if __name__ == "__main__":
    test_longestCommonPrefix()
