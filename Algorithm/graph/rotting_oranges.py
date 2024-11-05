from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        fresh = 0
        rotten = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1

                elif grid[r][c] == 2:
                    rotten.append((r, c))
        
        minute = 0
        dirs = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    
                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        rotten.append((nr, nc))
                        fresh -= 1
            
            minute += 1
        
        return minute if fresh == 0 else -1