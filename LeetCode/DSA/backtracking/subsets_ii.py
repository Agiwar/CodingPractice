class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        like the problem subset, when traversing, decide to pick current number or not,
            but subset 2, the input array may have duplicates, and duplicated subset is not solution,
            so in order to guarantee not hitting the same subset,
            we need to do sorting to skip the adjacent duplicates
            e.g., [1, 2, 2] -> [1, 2]:
                pick first 2 then skip second 2 is identical to
                skip first 2 then pick the second 2
        
        in order to keep subset are unique, using set to collect them,
            at the same time, transform subset (list type) to tuple type,
            cuz (1, 2) and (2, 1) are the same, so needed to maintain mutability and hashable,
            using tuple to carry all subset which is a list
        
        time: O(n * 2^n) — sort is O(n log n); the recursion explores all 2^n
            pick/skip paths, and each pick copies the current subset into a
            tuple (O(n)) for hashing into the set
        space: O(n * 2^n) — the set holds up to 2^n tuples of length up to n;
            auxiliary space is O(n) for the recursion stack and running subset
        """
        
        nums.sort()
        
        subsets = {()}
        subset = []
        
        def collect_uqe_subset(idx: int) -> None:
            if idx == len(nums):
                return
            
            subset.append(nums[idx])
            subsets.add(tuple(subset))
            
            collect_uqe_subset(idx + 1)
            subset.pop()
            
            collect_uqe_subset(idx + 1)
        
        collect_uqe_subset(0)
        return [list(subset) for subset in subsets]


subsetsWithDup = Solution().subsetsWithDup


def normalize(subsets: list[list[int]]) -> list[list[int]]:
    # order of subsets and order within a subset don't matter,
    # but duplicate subsets DO matter — exact multiset comparison catches them
    return sorted(sorted(s) for s in subsets)


def test_subsetsWithDup():
    # LeetCode Example 1: nums = [1,2,2]
    assert normalize(subsetsWithDup([1, 2, 2])) == normalize(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    )

    # LeetCode Example 2: nums = [0]
    assert normalize(subsetsWithDup([0])) == normalize([[], [0]])

    # Edge cases

    # All elements identical — result size is n+1, not 2^n
    assert normalize(subsetsWithDup([2, 2, 2])) == normalize(
        [[], [2], [2, 2], [2, 2, 2]]
    )

    # Unsorted input with duplicates — dedup must still work
    assert normalize(subsetsWithDup([4, 4, 1, 4])) == normalize(
        [[], [1], [4], [1, 4], [4, 4], [1, 4, 4], [4, 4, 4], [1, 4, 4, 4]]
    )

    # All distinct — dedup logic must not over-prune (full 2^n subsets)
    assert normalize(subsetsWithDup([1, 2, 3])) == normalize(
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    )

    # Negative values with duplicates
    assert normalize(subsetsWithDup([-1, -1, 0])) == normalize(
        [[], [-1], [-1, -1], [0], [-1, 0], [-1, -1, 0]]
    )

    # Two duplicate groups — 3 choices of 1s x 3 choices of 2s = 9 subsets
    assert normalize(subsetsWithDup([1, 1, 2, 2])) == normalize(
        [[], [1], [1, 1], [2], [2, 2], [1, 2], [1, 1, 2], [1, 2, 2], [1, 1, 2, 2]]
    )

    print("All tests passed")


if __name__ == "__main__":
    test_subsetsWithDup()
