from collections import deque
from itertools import product


class Solution:
    
    DIRS = (
        (1, 0), (0, 1), (-1, 0), (0, -1)
    )
    
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        only a rotten orange can rot its fresh neighbors, a fresh one can't start by itself,
            so scan once to count fresh and push every rotten orange into the queue,
            they all spread at the same time (multi-source BFS), one level is one minute

        flip the fresh orange to 2 and fresh -= 1 right when pushing it,
            the grid state itself works as visited, no seen set needed,
            and the same orange can't be counted twice in the same minute

        loop only while there's rotten to spread and fresh left,
            so no empty minute gets counted after the last one rots,
            fresh still left after the loop means it can't be reached, return -1

        time: O(m * n), every cell is scanned once and pushed at most once
        space: O(m * n), the queue in the worst case, grid is modified in place
        """
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
