class Solution:
    
    mappings = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    
    def letterCombinations(self, digits: str) -> list[str]:
        """
        to get all cartesian product combinations,
            create the digit to letter mappings in class level to avoid re-building it on every call,
            and when traversing digits, each digit can reference its letters

        the recursive part is move idx by one until idx hits len(digits),
            combination is a shared buffer holding the letters chosen so far,
            append picks a letter for position idx, and pop undoes that pick
            so the next sibling letter starts from the same prefix

        the criteria exit is when idx hits len(digits), which means the buffer holds
            a full combination, so "".join freezes a snapshot into an immutable string

        time: O(n * 4^n) in worst case, n is length of digits,
                the depth is n, and each node branches into at most 4 letters (only 7 and 9),
                so there are at most 4^n leaves,
                and each leaf costs O(n) for the "".join,
                so total time is O(n * 4^n)
        space: O(n), the recursive call is O(n) where depth <= n,
                and the auxiliary space is O(n) for the combination buffer,
                so total is O(n), the output doesn't count
        """
        
        if not digits:
            return []
        
        n = len(digits)
        combinations = []
        combination = []
        
        def collect_digit_to_letter(idx: int) -> None:
            if idx == n:
                combinations.append("".join(combination))
                return
            
            for letter in self.mappings[digits[idx]]:
                combination.append(letter)
                collect_digit_to_letter(idx + 1)
                combination.pop()
        
        collect_digit_to_letter(0)
        return combinations


letterCombinations = Solution().letterCombinations


def normalize(combos: list[str]) -> list[str]:
    # order of the combinations doesn't matter, but the order of letters
    # WITHIN each combination does — sort the list, never the strings
    return sorted(combos)


def test_letterCombinations():
    # LeetCode Example 1
    assert normalize(letterCombinations("23")) == normalize(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )

    # LeetCode Example 2 — empty input is allowed by the constraints
    assert letterCombinations("") == []

    # LeetCode Example 3
    assert normalize(letterCombinations("2")) == normalize(["a", "b", "c"])

    # Edge cases

    # Digits mapping to 4 letters — guards against assuming 3 per digit
    assert normalize(letterCombinations("7")) == normalize(["p", "q", "r", "s"])
    assert normalize(letterCombinations("9")) == normalize(["w", "x", "y", "z"])

    # Repeated digit: letters ARE reusable across positions, unlike word search
    assert normalize(letterCombinations("22")) == normalize(
        ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
    )

    # Two 4-letter digits: 4 * 4 = 16 combinations
    combos = letterCombinations("79")
    assert len(combos) == 16
    assert len(set(combos)) == 16
    assert all(len(c) == 2 for c in combos)

    # Max length input: 3 * 3 * 4 * 4 = 144, all distinct, all length 4
    combos = letterCombinations("2379")
    assert len(combos) == 144
    assert len(set(combos)) == 144
    assert all(len(c) == 4 for c in combos)

    print("All tests passed")


if __name__ == "__main__":
    test_letterCombinations()
