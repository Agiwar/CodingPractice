class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        to collect all subsets, during traversal, can decide to pick the current number or not,
            e.g., [1, 2, 3] is a subset, so is [1, 3], which means deciding not to pick 2
        
        all subsets come from two scenarios, pick or not pick, so each index has two tasks,
            in pick situation, if done, pop the subset to rollback for the next task which is not pick
            
        the recursive call exit criteria is when idx runs past the end of nums,
            and then store a snapshot copy of the current subset
        
        time = O(n * 2^n), there are 2^n subsets, and copying each snapshot costs up to O(n),
                n is total number of int values in nums,
                the output size alone already forbids anything faster than this
        space = O(n) auxiliary, recursion depth is n plus the working subset holds up to n,
                but the output stores every subset's contents, n * 2^(n-1) values in total,
                so O(n * 2^n) counting the output
        """
        
        n = len(nums)
        
        subsets = []
        subset = []
        
        def collect_subset(idx: int) -> None:
            if idx == n:
                subsets.append(subset.copy())
                return
            
            subset.append(nums[idx])
            collect_subset(idx + 1)
            
            subset.pop()
            collect_subset(idx + 1)
        
        collect_subset(0)
        return subsets


subsets = Solution().subsets

def test_subsets():
    # LeetCode Example 1: nums = [1,2,3]
    result = subsets([1, 2, 3])
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])

    # LeetCode Example 2: nums = [0]
    result = subsets([0])
    expected = [[], [0]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_subsets()
