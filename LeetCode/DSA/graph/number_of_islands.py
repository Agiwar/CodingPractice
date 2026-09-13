class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        the main idea is using DFS to collect all "1" land
            until they can't be connected each other,
            scan every cell, a land cell that is not seen yet means a new island,
            so count it first and then flood its whole region into seen_land,
            after the flood the scan won't count the same island again

        use an explicit stack instead of recursion,
            cuz the grid can be 300 x 300 and the longest path blows python's limit,
            and mark the cell as seen when pushing not when popping,
            so the same cell never sits in the stack twice

        time: O(m * n), m is grid.length and n is grid[0].length
        space: O(m * n), seen_land plus the stack,
            cuz seen_land blocks revisits, neither one can hold a cell twice
        """
        
        row = len(grid)
        col = len(grid[0])
        
        seen_land = set()
        
        def mark_island(r: int, c: int) -> None:
            stack = [(r, c)]
            seen_land.add((r, c))
            
            while stack:
                r, c = stack.pop()
                
                for nr, nc in (
                    (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)
                ):
                    if (
                        nr in range(row) and
                        nc in range(col) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in seen_land
                    ):
                        stack.append((nr, nc))
                        seen_land.add((nr, nc))
                        
        ct = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in seen_land:
                    ct += 1
                    mark_island(r, c)
        
        return ct
        

numIslands = Solution().numIslands

def test_numIslands():
    # LeetCode Example 1
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"],
    ]
    assert numIslands(grid) == 1

    # LeetCode Example 2
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
    ]
    assert numIslands(grid) == 3

    # Edge: all water, and single land cell
    assert numIslands([["0","0"],["0","0"]]) == 0
    assert numIslands([["1"]]) == 1

    # Edge: diagonal land is not connected, 4-directional only
    assert numIslands([
        ["1","0","1"],
        ["0","1","0"],
        ["1","0","1"],
    ]) == 5

    # Edge: single row and single column
    assert numIslands([["1","0","1","1","0","1"]]) == 3
    assert numIslands([["1"],["0"],["1"],["1"]]) == 2

    # Edge: snake shaped island, one island that needs the full path walked
    assert numIslands([
        ["1","1","1","1"],
        ["0","0","0","1"],
        ["1","1","1","1"],
        ["1","0","0","0"],
    ]) == 1

    # Edge: max size grid from constraints, 300 x 300 all land is one island
    assert numIslands([["1"] * 300 for _ in range(300)]) == 1

    print("All tests passed")

if __name__ == "__main__":
    test_numIslands()
