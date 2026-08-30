class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        this question's solution is get all rearranged array where they are all unique,
            the task is not pick/not pick the current number,
            cuz each permutation has the length(nums), so no exclude branch,
            instead, check the current number is used or not, if not, fill it in
        
        time: O(n * n!), when checking number is used or not, at first check n times,
                once one checked, then need to check (n - 1) times, until 1, so n!,
                and each copy takes O(n) time, so total is O(n * n!)
        space: O(n), recursive call is O(n) where depth <= n,
                the auxiliary space is O(n) for permutation, O(n) for used_nums,
                so O(n) + O(n) + O)(n), total is O(n), the output doesn't count
        """
        
        n = len(nums)
        used_nums = [False] * n
        
        permutations = []
        permutation = []
        
        def collect_permute() -> None:
            if len(permutation) == n:
                permutations.append(permutation.copy())
                return
            
            for idx in range(n):
                if used_nums[idx]:
                    continue
                
                permutation.append(nums[idx])
                used_nums[idx] = True
                
                collect_permute()
                
                permutation.pop()
                used_nums[idx] = False
        
        collect_permute()
        return permutations


permute = Solution().permute


def normalize(perms: list[list[int]]) -> list[list[int]]:
    # order of the permutations doesn't matter, but order WITHIN each
    # permutation does — so sort the outer list only, never the inner lists
    return sorted(perms)


def test_permute():
    # LeetCode Example 1
    assert normalize(permute([1, 2, 3])) == normalize(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )

    # LeetCode Example 2
    assert normalize(permute([0, 1])) == normalize([[0, 1], [1, 0]])

    # LeetCode Example 3
    assert normalize(permute([1])) == normalize([[1]])

    # Edge cases

    # Negative values
    assert normalize(permute([-1, 5])) == normalize([[-1, 5], [5, -1]])

    # n = 4 structural check: 4! results, all distinct, each a rearrangement
    # of the input (guards against missed branches / duplicated paths at depth)
    perms = permute([1, 2, 3, 4])
    assert len(perms) == 24
    assert len({tuple(p) for p in perms}) == 24
    assert all(sorted(p) == [1, 2, 3, 4] for p in perms)

    print("All tests passed")


if __name__ == "__main__":
    test_permute()
