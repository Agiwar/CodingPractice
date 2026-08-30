from itertools import product


class Solution:
    
    mappings = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    
    def letterCombinations(self, digits: str) -> list[str]:
        """
        in this question, it's purpose is to collect all cartesian combinations,
            so i just use python build-in module to finish
        """
        
        if not digits:
            return []
        
        candidates = [self.mappings[digit] for digit in digits]
        return ["".join(letter) for letter in product(*candidates)]


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
