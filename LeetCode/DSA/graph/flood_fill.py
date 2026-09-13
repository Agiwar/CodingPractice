class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        """
        the region is every 4-directional connected cell sharing the starting pixel value,
            so DFS from (sr, sc) and keep the cells that still match the original pixel,
            bounds check goes before reading image[r][c] so it never indexes out of range

        collect into seen_cell first and paint after,
            cuz seen_cell is what stops the recursion, not the recolor,
            so color == pixel terminates by itself without any extra guard

        time = O(m * n), each cell is visited at most once
        space = O(m * n), seen_cell plus the recursion stack
        """

        row = len(image)
        col = len(image[0])
        
        pixel = image[sr][sc]
        seen_cell = set()
        
        def collect_same_pixel(r: int, c: int) -> None:
            if (
                r not in range(row) or
                c not in range(col) or
                image[r][c] != pixel or
                (r, c) in seen_cell
            ):
                return
            
            seen_cell.add((r, c))
            
            collect_same_pixel(r + 1, c)
            collect_same_pixel(r - 1, c)
            collect_same_pixel(r, c  + 1)
            collect_same_pixel(r, c - 1)
        
        collect_same_pixel(sr, sc)
        for r, c in seen_cell:
            image[r][c] = color
        
        return image


floodFill = Solution().floodFill

def test_floodFill():
    # LeetCode examples
    assert floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    assert floodFill([[0,0,0],[0,0,0]], 0, 0, 0) == [[0,0,0],[0,0,0]]

    # Edge: new color equals starting color on a fillable region, must terminate
    assert floodFill([[1,1],[1,1]], 0, 0, 1) == [[1,1],[1,1]]

    # Edge: single cell grid
    assert floodFill([[5]], 0, 0, 9) == [[9]]

    # Edge: start pixel isolated, no neighbor shares its color
    assert floodFill([[1,2,1],[2,3,2],[1,2,1]], 1, 1, 7) == [[1,2,1],[2,7,2],[1,2,1]]

    # Edge: 4-directional only, diagonal same-color cells stay untouched
    assert floodFill([[1,0,1],[0,1,0],[1,0,1]], 1, 1, 4) == [[1,0,1],[0,4,0],[1,0,1]]

    # Edge: snake shaped region, fill must follow the full path not just neighbors
    assert floodFill([[1,1,1,1],[0,0,0,1],[1,1,1,1],[1,0,0,0]], 0, 0, 6) == [[6,6,6,6],[0,0,0,6],[6,6,6,6],[6,0,0,0]]

    # Edge: start on a border cell, region touches grid edges
    assert floodFill([[2,2,3],[2,3,3],[3,3,3]], 0, 2, 8) == [[2,2,8],[2,8,8],[8,8,8]]

    print("All tests passed")

if __name__ == "__main__":
    test_floodFill()
