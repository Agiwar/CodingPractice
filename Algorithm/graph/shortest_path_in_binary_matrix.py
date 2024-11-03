from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        queue = deque()
        dirs = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]

        r, c = 0, 0
        visit = {(r, c)}
        queue.append((r, c))

        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (
                        nr not in range(rows) or
                        nc not in range(cols) or
                        grid[nr][nc] == 1 or
                        (nr, nc) in visit
                    ):
                        continue

                    visit.add((nr, nc))
                    queue.append((nr, nc))

            length += 1

        return -1