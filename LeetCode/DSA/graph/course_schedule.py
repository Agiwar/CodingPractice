from typing import Dict, List, Set


class Solution:
    @staticmethod
    def is_done_dfs(
        cus: int, 
        cus_adj_list: Dict[int, List[int]],
        cus_done: Set[int] = None,
    ) -> bool:
        if cus_done is None:
            cus_done = set()
        
        if cus in cus_done: return False
        elif cus_adj_list[cus] == []: return True
        
        cus_done.add(cus)
        for pre in cus_adj_list[cus]:
            if not Solution.is_done_dfs(pre, cus_adj_list, cus_done): return False
        
        cus_done.remove(cus)
        cus_adj_list[cus] = []
        
        return True
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_of_each_cus = {cus: [] for cus in range(numCourses)}
        for cus, pre in prerequisites:
            pre_of_each_cus[cus].append(pre)
        
        return all(
            Solution.is_done_dfs(cus, pre_of_each_cus) for cus in range(numCourses)
        )
