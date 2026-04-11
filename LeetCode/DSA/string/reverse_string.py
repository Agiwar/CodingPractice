from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        in-place reverse the list of string,
            use two pointers representing the first and last char from list of string,
            for each iteration, swap the current left and right's chars,
            and move forward left pointer, and move back right pointer at the same time,
            until the left and right pointer meet each other, or be neighborhood

        time = O(n), n is s.length
        space = O(1), in-place manipulation
        """

        l_pt, r_pt = 0, len(s) - 1
        while l_pt <= r_pt:
            s[l_pt], s[r_pt] = s[r_pt], s[l_pt]
            l_pt += 1
            r_pt -= 1


reverseString = Solution().reverseString

def test_reverseString():
    s1 = ["h","e","l","l","o"]
    reverseString(s1)
    assert s1 == ["o","l","l","e","h"]

    s2 = ["H","a","n","n","a","h"]
    reverseString(s2)
    assert s2 == ["h","a","n","n","a","H"]

    # Edge cases
    s3 = ['L', 'e', 'e', 't', 'C', 'o', 'd', 'e']
    reverseString(s3)
    assert s3 == ['e', 'd', 'o', 'C', 't', 'e', 'e', 'L']

    s4 = ['C', 'h', 'a', 't', 'G', 'P', 'T']
    reverseString(s4)
    assert s4 == ['T', 'P', 'G', 't', 'a', 'h', 'C']

    s5 = ['C', 'l', 'a', 'u', 'd', 'e', '.', 'a', 'i', '_', 'O', 'p', 'u', 's', '4', '.', '6']
    reverseString(s5)
    assert s5 == ['6', '.', '4', 's', 'u', 'p', 'O', '_', 'i', 'a', '.', 'e', 'd', 'u', 'a', 'l', 'C']


    print("All tests passed")

if __name__ == "__main__":
    test_reverseString()
