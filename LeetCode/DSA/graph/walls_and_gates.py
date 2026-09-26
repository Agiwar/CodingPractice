from collections import deque
from itertools import product


class Solution:
    
    DIRS = (
        (1, 0), (0, 1), (-1, 0), (0, -1)
    )
    
    INF = 2147483647
    
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        multi-source BFS, same shape as rotting oranges: all gates go in the queue
        first, then spread out one layer per round. length is the layer, so a room
        popped in round k is k steps from its nearest gate.

        claim a room on push (seen set), write its distance on pop. the check before
        pushing uses the same set, so a room waiting in the queue is never pushed twice.

        rooms no gate can reach are never pushed, so they keep INF, which is what the
        problem wants. no counter needed, unlike rotting oranges where the leftover
        fresh count is the answer.

        Time: O(m * n), each cell is pushed at most once.
        Space: O(m * n) for the seen set and the queue.
        """
        
        m = len(rooms)
        n = len(rooms[0])
        
        gates = deque()
        for r, c in product(range(m), range(n)):
            if rooms[r][c] == 0:
                gates.append((r, c))
        
        seen_rooms = set()
        
        def get_distance() -> None:
            length = 0
            
            while gates:
                for _ in range(len(gates)):
                    r, c = gates.popleft()
                    
                    if rooms[r][c] == self.INF:
                        rooms[r][c] = length
                    
                    for dr, dc in self.DIRS:
                        nr = r + dr
                        nc = c + dc
                        
                        if (
                            not 0 <= nr < m
                            or not 0 <= nc < n
                            or rooms[nr][nc] == -1
                            or (nr, nc) in seen_rooms
                        ):
                            continue
                        
                        gates.append((nr, nc))
                        seen_rooms.add((nr, nc))
                
                length += 1
        
        get_distance()


wallsAndGates = Solution().wallsAndGates

INF = 2147483647

def test_wallsAndGates():
    # LeetCode Example 1
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    wallsAndGates(rooms)
    assert rooms == [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]

    # LeetCode Example 2
    rooms = [[-1]]
    wallsAndGates(rooms)
    assert rooms == [[-1]]

    # Edge cases

    # Single gate
    rooms = [[0]]
    wallsAndGates(rooms)
    assert rooms == [[0]]

    # No gate at all — room stays INF
    rooms = [[INF]]
    wallsAndGates(rooms)
    assert rooms == [[INF]]

    # Room walled off from the gate — stays INF
    rooms = [[0, -1, INF]]
    wallsAndGates(rooms)
    assert rooms == [[0, -1, INF]]

    # Two gates — each room takes the nearer one (multi-source)
    rooms = [[0, INF, INF, INF, 0]]
    wallsAndGates(rooms)
    assert rooms == [[0, 1, 2, 1, 0]]

    # Path must detour around a wall — Manhattan distance would say 2, real is 4
    rooms = [
        [0, -1, INF],
        [INF, INF, INF],
    ]
    wallsAndGates(rooms)
    assert rooms == [
        [0, -1, 4],
        [1, 2, 3],
    ]

    print("All tests passed")

if __name__ == "__main__":
    test_wallsAndGates()
