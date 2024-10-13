from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_adj_list = {i: [] for i in range(numCourses)}
        for cus, pre in prerequisites:
            pre_adj_list[cus].append(pre)
        
        cus_done = set()

        # check if each cus can be done
        def dfs(cus: int) -> bool:
            # the same cus can't be done twice
            if cus in cus_done:
                return False
            
            # if cus has no any pre, this cus can be done
            if pre_adj_list[cus] == []:
                return True
            
            cus_done.add(cus)
            for pre in pre_adj_list[cus]:
                if not dfs(pre):
                    return False
            
            cus_done.remove(cus)
            pre_adj_list[cus] = []
            return True
        

        for cus in range(numCourses):
            if not dfs(cus):
                return False
        
        return True