import sys


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        scan every cell, when hitting an unseen land cell,
            dfs from it to count the whole island, keep the max

        dfs helper returns 0 when out of bounds, water, or already seen,
            otherwise marks the cell seen and returns 1 + the 4 neighbors' areas

        seen_cell keeps the input grid untouched,
            trade-off: extra memory vs sinking the island in place

        recursion depth can reach m * n on a full grid (2500 at the constraint max),
            python's default limit is 1000, leetcode raises it, a local run doesn't.
            iterative stack / bfs is the interview-safe answer,
            maxAreaOfIslandPython below is the python band-aid

        time: O(m * n), every cell is entered once and rejected at most 4 times as a neighbor,
                m and n are the grid dimensions
        space: O(m * n) for seen_cell plus the recursion stack in the worst case,
                output doesn't count
        """
        row = len(grid)
        col = len(grid[0])
        
        seen_cell = set()
        
        def get_island_area(r: int, c: int) -> int:
            if (
                r not in range(row) or
                c not in range(col) or
                grid[r][c] != 1 or
                (r, c) in seen_cell
            ):
                return 0
            
            seen_cell.add((r, c))
            area = 1
            
            area += (
                get_island_area(r + 1, c) +
                get_island_area(r - 1, c) +
                get_island_area(r, c + 1) +
                get_island_area(r, c - 1)
            )
            
            return area
        
        max_area = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in seen_cell:
                    max_area = max(max_area, get_island_area(r, c))
        
        return max_area

    def maxAreaOfIslandPython(self, grid: list[list[int]]) -> int:
        # recursive dfs can go m * n deep, python's default limit is 1000
        sys.setrecursionlimit(max(sys.getrecursionlimit(), len(grid) * len(grid[0]) + 100))
        return self.maxAreaOfIsland(grid)


maxAreaOfIsland = Solution().maxAreaOfIsland
maxAreaOfIslandPython = Solution().maxAreaOfIslandPython

def test_maxAreaOfIsland():
    # LeetCode Example 1
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0],
    ]
    assert maxAreaOfIsland(grid) == 6

    # LeetCode Example 2
    assert maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0

    # Edge cases

    # Single land cell
    assert maxAreaOfIsland([[1]]) == 1

    # Single water cell
    assert maxAreaOfIsland([[0]]) == 0

    # Diagonal-only neighbors are NOT connected (4-directional, not 8)
    assert maxAreaOfIsland([[1, 0], [0, 1]]) == 1

    # Several islands, largest is not the first one scanned
    assert maxAreaOfIsland([
        [1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0],
    ]) == 4

    # Max constraint: 50x50 all land — one island of 2500 cells.
    # A recursive DFS chains through every cell, so depth reaches ~2500,
    # past python's default limit of 1000. The wrapper raises the limit first.
    assert maxAreaOfIslandPython([[1] * 50 for _ in range(50)]) == 2500

    print("All tests passed")

if __name__ == "__main__":
    test_maxAreaOfIsland()
