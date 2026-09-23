from collections import deque


class Solution:
    
    DIRS = (
        (1, 0), (0, 1), (-1, 0), (0, -1),
        (1, 1), (-1, 1), (1, -1), (-1, -1),
    )
    
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        every step costs the same, so shortest path means fewest levels,
            BFS level by level, the first time the end cell gets popped is the answer,
            DFS only finds a path, not the shortest one

        8 directions cuz diagonal counts as adjacent,
            length starts at 1 cuz the path counts cells not edges, so [[0]] is 1,
            start or end blocked means -1 right away

        mark visited when pushing not when popping,
            so the same cell never sits in the queue twice,
            queue runs dry before reaching the end means no path, return -1

        time: O(n^2), every cell is pushed at most once and checks 8 neighbors
        space: O(n^2), visited_cell plus the queue
        """
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
