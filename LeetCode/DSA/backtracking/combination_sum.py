class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        to find out the all combination sum is equal to target, first i do sorting,
            after sorting, can directly guarantee every number (when it's larger than target)
            after current number, no need to execute program anymore
        
        i define this question has two tasks (branch), which is yes/no,
            when deciding to select current number,
            need to compare the current sum is equal to target or not,            
            if less than, keep selecting, which is "i want it",
            if greater, stop and then en pop for next task which is
            "i don't want the previous one", "i want the current"
        
        the main idea is reframe target sum to subtract number which is remaining,
            when remaining hits zero, this is the one of the solution combination candidate
            so append it's snapshot copy to output
        
        the guard condition needs to come after solution condition,
            if not, when get solution which is remaining is equal to zero,
            the number is always larger than zero,
            so current number > remaining will directly return when remaining is zero,
            so the solution combination is never be collected

        time = O(n^(t/m + 1)), n is number of candidates, t is target, m is smallest candidate,
                every pick burns at least m from remaining, so a path has at most t/m picks,
                the decision tree has up to n^(t/m) nodes, each O(1),
                and each found combination is copied at cost up to O(t/m),
                the output itself can be exponential, so no algorithm can beat this floor
        space = O(n + t/m) auxiliary, recursion depth is at most n rightward moves
                plus t/m picks, and the working combination holds at most t/m values,
                the output stores s combinations of length up to t/m, so O(s * t/m) on top
        """
        
        candidates.sort()
        
        combinations = []
        combination = []
        
        def collect_combination(idx: int, remaining: int) -> None:
            if remaining == 0:
                combinations.append(combination.copy())
                return
            
            if idx == len(candidates) or candidates[idx] > remaining:
                return
            
            combination.append(candidates[idx])
            collect_combination(idx, remaining - candidates[idx])
            
            combination.pop()
            collect_combination(idx + 1, remaining)
        
        collect_combination(0, target)
        return combinations        
        

combinationSum = Solution().combinationSum

def test_combinationSum():
    # LeetCode Example 1: candidates = [2,3,6,7], target = 7
    result = combinationSum([2, 3, 6, 7], 7)
    expected = [[2, 2, 3], [7]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])

    # LeetCode Example 2: candidates = [2,3,5], target = 8
    result = combinationSum([2, 3, 5], 8)
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])

    # LeetCode Example 3: candidates = [2], target = 1
    assert combinationSum([2], 1) == []

    # Edge cases

    print("All tests passed")

if __name__ == "__main__":
    test_combinationSum()
