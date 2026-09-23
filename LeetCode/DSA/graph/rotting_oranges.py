from collections import deque
from itertools import product


class Solution:
    
    DIRS = (
        (1, 0), (0, 1), (-1, 0), (0, -1)
    )
    
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        rotten_oranges = deque()
        fresh = 0
        
        for r, c in product(range(row), range(col)):
            if grid[r][c] == 1:
                fresh += 1
                
            elif grid[r][c] == 2:
                rotten_oranges.append((r, c))
        
        minute = 0
        while rotten_oranges and fresh:
            for _ in range(len(rotten_oranges)):
                r, c = rotten_oranges.popleft()
                
                for dr, dc in self.DIRS:
                    nr = r + dr
                    nc = c + dc
                    
                    if (
                        0 <= nr < row
                        and 0 <= nc < col
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        
                        rotten_oranges.append((nr, nc))
            
            minute += 1
        
        return -1 if fresh else minute
    

orangesRotting = Solution().orangesRotting

def test_orangesRotting():
    # LeetCode Example 1
    assert orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4

    # LeetCode Example 2
    assert orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1

    # LeetCode Example 3
    assert orangesRotting([[0,2]]) == 0

    # Edge cases
    # No oranges at all -> nothing to rot, answer is 0 (not -1)
    assert orangesRotting([[0]]) == 0

    # Fresh orange but no rotten source -> queue starts empty
    assert orangesRotting([[1]]) == -1

    # Two sources spread simultaneously (sequential per-source BFS would give 4)
    assert orangesRotting([[2,1,1,1,2]]) == 2

    # Rot spreads 4-directionally only (diagonal spread would give 1)
    assert orangesRotting([[2,1],[1,1]]) == 2

    # Non-square single column (guards row/col mix-ups)
    assert orangesRotting([[2],[1],[1],[1]]) == 3

    print("All tests passed")

if __name__ == "__main__":
    test_orangesRotting()
