from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))

            while queue:
                r, c = queue.popleft()
                dirs = [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)
                ]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit
                    ):
                        queue.append((nr, nc))
                        visit.add((nr, nc))


        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands