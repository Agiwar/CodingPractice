from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_adj_list = {c: [] for c in range(numCourses)}
        for cus, pre in prerequisites:
            pre_adj_list[cus].append(pre)
        
        cus_order = []
        cus_added = set()
        cus_cycle = set()

        def dfs(cus: int) -> bool:
            if cus in cus_cycle:
                return False
            
            if cus in cus_added:
                return True
            
            cus_cycle.add(cus)
            for pre in pre_adj_list[cus]:
                if not dfs(pre):
                    return False
            
            cus_cycle.remove(cus)
            cus_added.add(cus)
            cus_order.append(cus)

            return True
        

        for cus in range(numCourses):
            if not dfs(cus):
                return []
        
        return cus_order
