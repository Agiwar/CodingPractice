from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        dirs = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        
        def dfs(r: int, c: int) -> int:
            if (
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            
            visit.add((r, c))
            area = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            
            return area
            
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, dfs(r, c))

        return max_area