from collections import deque
from typing import Deque, List, Optional, Set


class GraphNode:
    
    def __init__(self, val: int, neighbors: List = []) -> None:
        """Implementation of Graph using Adjacency List

        Args:
            val (int): Vertex's value with int type.
            neighbors (List, optional): A list stores every edges 
                which we can access all of a given vertex's neighbor. Defaults to [].
        """
        self.val = val
        self.neighbors = neighbors


grid: List[List[int]] = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]

# Matrix DFS: 
# Count the unique paths from the top left to the bottom right.
# A single path may only move along 0's and can't visit the same cell more than once.

def dfs(
    grid: List[List[int]],
    row: int = 0,
    col: int = 0,
    visit: Set = set(),                 # use set to stores the position we already visited 
) -> int:
    
    ROWS = len(grid)
    COLS = len(grid[0])
    
    # base cases here
    if (
        min(row, col) < 0 or            # cannot be negative coordinate
        (row == ROWS or col == COLS) or # row and col index cannot be out of index from list
        (row, col) in visit or          # cannot re-visit the visited position
        grid[row][col] == 1             # cannot go to vertex with value of 1
    ):
        return 0
    
    if (                                # already reach the destination
        row == ROWS - 1 and 
        col == COLS - 1
    ):
        return 1
    
    # recursive call dfs
    visit.add((row, col))
    
    count = 0
    
    # there are four directions we can go
    count += dfs(grid, row + 1, col, visit)
    count += dfs(grid, row - 1, col, visit)
    count += dfs(grid, row, col + 1, visit)
    count += dfs(grid, row, col - 1, visit)
    
    visit.remove((row, col))
    
    return count


# Matrix BFS:
# Find the length of the shortest path from top left of the grid to the bottom right.

def bfs(
    grid: List[List[int]],
    row: int = 0,
    col: int = 0,
    visit: Set = set(),    # use set to stores the position we already visited
    queue: Deque = deque() # use queue to store which layer we currently are in
) -> int:
    
    ROWS = len(grid)
    COLS = len(grid[0])
    
    visit.add((row, col))
    queue.append((row, col))
    
    length = 0
    while queue:
        
        for _ in range(len(queue)):
            row, col = queue.popleft()
            
            # already reach the destination
            if (
                row == ROWS - 1 and
                col == COLS - 1
            ):
                return length
            
            # each position has four directions it can go
            neighbors = [
                [0, 1],
                [0, -1],
                [1, 0],
                [-1, 0]
            ]
            
            for dr, dc in neighbors:
                # these four conditions will make invalid path
                if (
                    min(row + dr, col + dc) < 0 or
                    ((row + dr) == ROWS or (col + dc) == COLS) or
                    (row + dr, col + dc) in visit or
                    grid[row + dr][col + dc] == 1
                ):
                    continue
                
                # so continue choosing the different way to go
                visit.add((row + dr, col + dc))
                queue.append((row + dr, col + dc))
        
        length += 1