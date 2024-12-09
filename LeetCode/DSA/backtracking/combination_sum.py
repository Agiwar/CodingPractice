from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        def dfs(i):
            if i == len(candidates):
                return
            
            if sum(subset) == target:
                result.append(subset.copy())
                return
            
            elif sum(subset) > target:
                return
            
            subset.append(candidates[i])
            dfs(i)
            
            subset.pop()
            dfs(i + 1)
        
        
        dfs(0)
        return result
