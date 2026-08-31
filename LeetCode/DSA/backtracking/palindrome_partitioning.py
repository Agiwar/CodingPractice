class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        the solution is collect all palindrome sets, and the task has just only one, traversing s,
            to determine each current substring is palindrome or not,
            we cannot use pick/not pick branch to solve it, cuz each char in s is needed to be considered,
            and this is not can pick char multiple times which is non-sense for this question,
            and also we don't need a global string to maintain the dynamic non-fixed length string,
            e.g., string = "a", next char is "b", so string += char == "ab",
            instead, using the start index to derive where's the end index to determine
            how much size we want, and it is a palindrome, this looping recursive call
            acts the same mechanism of creating a string accumulator, so the next start is the end from for loops,
            e.g., "a", "b", "c" -> "abc", need to continuing checking the rests,
            after "c" is "b", "a", so string becomes "abcba", that's the main idea
        
        time: O(n^2 * 2^n) for this version, n is length of s,
                there are n - 1 gaps between chars and each gap is either cut or not,
                so up to 2^(n-1) partitions in the worst case when every substring
                is a palindrome, e.g. "aaaa",
                the recursion tree has O(2^n) nodes, each node loops up to n end positions,
                and each slice + reverse costs O(n), so one node costs O(n^2),
                so total is O(n^2 * 2^n),
                if the palindrome check is precomputed into a table it becomes O(1),
                and then the whole thing drops to O(n * 2^n), which is the usual quoted bound
        space: O(n), the recursive call is O(n) where depth <= n,
                cuz each level consumes at least one char,
                and the auxiliary space is O(n) for the partition buffer,
                which holds at most n pieces summing to n chars,
                so total is O(n), the output doesn't count
        """
        
        n = len(s)
        partitions = []
        partition = []
        
        def collect_palindrome(start: int) -> None:
            if start == n:
                partitions.append(partition.copy())
                return
            
            for end in range(start + 1, n + 1):
                if (slices := s[start:end]) != slices[::-1]:
                    continue
                
                partition.append(slices)
                collect_palindrome(end)
                partition.pop()
        
        collect_palindrome(0)
        return partitions


partition = Solution().partition


def normalize(parts: list[list[str]]) -> list[list[str]]:
    # order of the partitions doesn't matter, but the order of pieces WITHIN
    # each partition does — they must concatenate back to s, so sort the outer
    # list only, never the inner lists
    return sorted(parts)


def test_partition():
    # LeetCode Example 1
    assert normalize(partition("aab")) == normalize([["a", "a", "b"], ["aa", "b"]])

    # LeetCode Example 2
    assert normalize(partition("a")) == normalize([["a"]])

    # Edge cases

    # Every substring is a palindrome — all 2^(n-1) cut positions are valid
    assert normalize(partition("aaa")) == normalize(
        [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]
    )

    # No multi-char palindrome — only the all-singles partition survives
    assert normalize(partition("abc")) == normalize([["a", "b", "c"]])

    # Even-length palindrome — guards against odd-center-only checking
    assert normalize(partition("abba")) == normalize(
        [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
    )

    # Odd-length palindrome
    assert normalize(partition("aba")) == normalize([["a", "b", "a"], ["aba"]])

    # Structural check: 2^(n-1) partitions, all distinct, every piece a
    # palindrome, and every partition concatenates back to the input
    s = "aaaa"
    parts = partition(s)
    assert len(parts) == 8
    assert len({tuple(p) for p in parts}) == 8
    assert all("".join(p) == s for p in parts)
    assert all(piece == piece[::-1] for p in parts for piece in p)

    print("All tests passed")


if __name__ == "__main__":
    test_partition()
