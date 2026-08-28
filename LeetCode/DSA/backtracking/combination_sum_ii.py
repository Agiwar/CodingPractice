class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Collect all unique combinations summing to target;
            input has duplicates, each number used at most once.

        Key insight:
            duplicates come from equal values at different
            indices building the same path (pick first 1 / skip second vs skip first / pick second).
            Sort, then the exclude branch skips all copies of the current value
        
        About this question, it's like combine:
            39's structure (record at remaining == 0, prune candidates[idx] > remaining) and 
            90's skip; include goes idx + 1, no reuse.
            Solution check before guard, or the guard swallows it.

        Time: O(2^n + s * n) — include/exclude per index, depth <= n
            (each index decided once, unlike 39 where depth is target-driven);
            s solutions copied at O(n) each; sort dominated.
        Space: O(n) auxiliary (stack + shared list); output O(s * n) separate.
        """
        
        candidates.sort()
        n = len(candidates)
        
        combinations = []
        combination = []
        
        def collect_combination(idx: int, remaining: int) -> None:
            if remaining == 0:
                combinations.append(combination.copy())
                return
            
            if idx == n or candidates[idx] > remaining:
                return
            
            combination.append(candidates[idx])
            collect_combination(idx + 1, remaining - candidates[idx])
            
            while idx + 1 < n and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            combination.pop()
            collect_combination(idx + 1, remaining)
        
        collect_combination(0, target)
        return combinations


combinationSum2 = Solution().combinationSum2


def normalize(combos: list[list[int]]) -> list[list[int]]:
    # order of combinations and order within a combination don't matter,
    # but duplicate combinations DO matter — exact multiset comparison catches them
    return sorted(sorted(c) for c in combos)


def test_combinationSum2():
    # LeetCode Example 1
    assert normalize(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == normalize(
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    )

    # LeetCode Example 2
    assert normalize(combinationSum2([2, 5, 2, 1, 2], 5)) == normalize(
        [[1, 2, 2], [5]]
    )

    # Edge cases

    # No valid combination — result must be empty
    assert combinationSum2([3, 5], 2) == []

    # Single candidate equal to target
    assert normalize(combinationSum2([7], 7)) == normalize([[7]])

    # All duplicates — [2,2] must appear exactly once, and each element
    # may be used at most once (no [2,2,2,...] beyond what's available)
    assert normalize(combinationSum2([2, 2, 2, 2], 4)) == normalize([[2, 2]])

    # Two duplicate groups — [1,2] must appear exactly once despite two 1s and two 2s
    assert normalize(combinationSum2([1, 1, 2, 2], 3)) == normalize([[1, 2]])

    # Entire array is the only combination
    assert normalize(combinationSum2([1, 2, 3], 6)) == normalize([[1, 2, 3]])

    print("All tests passed")


if __name__ == "__main__":
    test_combinationSum2()
