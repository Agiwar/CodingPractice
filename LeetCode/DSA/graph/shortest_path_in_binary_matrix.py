from collections import deque


class Solution:
    
    DIRS = (
        (1, 0), (0, 1), (-1, 0), (0, -1),
        (1, 1), (-1, 1), (1, -1), (-1, -1),
    )
    
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        sr, sc = 0, 0
        er, ec = n - 1, n - 1
        
        if grid[sr][sc] == 1 or grid[er][ec] == 1:
            return -1
        
        visited_cell = {(sr, sc)}
        queue = deque([(sr, sc)])
        
        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                if (r, c) == (er, ec):
                    return length
                
                for dr, dc in self.DIRS:
                    nr = r + dr
                    nc = c + dc
                    
                    if (
                        not sr <= nr <= er
                        or not sc <= nc <= ec
                        or grid[nr][nc] != 0
                        or (nr, nc) in visited_cell
                    ):
                        continue
                    
                    visited_cell.add((nr, nc))
                    queue.append((nr, nc))
            
            length += 1
        
        return -1


shortestPathBinaryMatrix = Solution().shortestPathBinaryMatrix

def test_shortestPathBinaryMatrix():
    # LeetCode Example 1
    assert shortestPathBinaryMatrix([[0,1],[1,0]]) == 2

    # LeetCode Example 2
    assert shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]) == 4

    # LeetCode Example 3
    assert shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]) == -1

    # Edge cases
    # Minimum size, open -> start is also the end
    assert shortestPathBinaryMatrix([[0]]) == 1

    # Minimum size, blocked
    assert shortestPathBinaryMatrix([[1]]) == -1

    # End cell blocked
    assert shortestPathBinaryMatrix([[0,0],[0,1]]) == -1

    # Fully open grid -> pure diagonal walk
    assert shortestPathBinaryMatrix([[0,0,0],[0,0,0],[0,0,0]]) == 3

    # Forced detour through a single gap (greedy/diagonal-only fails here)
    assert shortestPathBinaryMatrix([[0,1,0],[0,1,0],[0,0,0]]) == 4

    # Longer detour: row of walls with one opening
    assert shortestPathBinaryMatrix([[0,0,0,0],[1,1,1,0],[0,0,0,0],[0,1,1,0]]) == 6

    print("All tests passed")

if __name__ == "__main__":
    test_shortestPathBinaryMatrix()
