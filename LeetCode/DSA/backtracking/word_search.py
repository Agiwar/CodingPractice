class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        the main idea is start at row = 0 and col = 0, to check this char is current s from word,
            the boundary conditions contain when the row index is out of len(board) or
            col index is out of len(board[0]) or current char is not the current s from word,
            or the coordinate cell has been seen, cuz each letter can only be used once.
        
        the solution criteria is when the current index is len(word),
            for each recursive call, if current status are not in any if boundary conditions,
            so that we can move index idx by one (only happen when char match word[idx])
        
        the logic is when starting finding char, if none of boundary conditions happens,
            each coordinate cell is needed to put in the set, and update the idx
        
        time: O(m * n * 4^L), where m * n is the board size and L is len(word),
                every cell can be a starting point, so there are m * n starts,
                each call branches to 4 neighbors and the depth goes up to L,
                so one start costs 4^L, total is O(m * n * 4^L)
        space: O(L), recursive call is O(L) where depth <= L,
                the auxiliary space is O(L) for seen_cell, cuz it only holds
                the current path, not the whole board,
                so O(L) + O(L), total is O(L), the board doesn't count
        """
        
        row = len(board)
        col = len(board[0])
        n = len(word)
        
        seen_cell = set()
        
        def board_has_word(r: int, c: int, idx: int) -> bool:
            if idx == n:
                return True
            
            if (
                r not in range(row) or
                c not in range(col) or
                board[r][c] != word[idx] or
                (r, c) in seen_cell
            ):
                return False
            
            seen_cell.add((r, c))
            idx += 1
            
            found = (
                board_has_word(r + 1, c, idx) or
                board_has_word(r - 1, c, idx) or
                board_has_word(r, c + 1, idx) or
                board_has_word(r, c - 1, idx)
            )
            
            seen_cell.remove((r, c))
            return found
        
        return any(board_has_word(r, c, 0) for r in range(row) for c in range(col))


exist = Solution().exist


def test_exist():
    # LeetCode Example 1
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED") is True

    # LeetCode Example 2
    assert exist(board, "SEE") is True

    # LeetCode Example 3
    assert exist(board, "ABCB") is False

    # Edge cases

    # Minimum grid, single-cell match / mismatch
    assert exist([["A"]], "A") is True
    assert exist([["A"]], "B") is False

    # A cell cannot be reused: only 2 cells, word needs 3
    assert exist([["A", "A"]], "AAA") is False

    # Long snaking path that dead-ends on the first E branch and must
    # unwind — guards against forgetting to restore visited state
    board2 = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    assert exist(board2, "ABCESEEEFS") is True

    # Path turns left and up — guards against only searching right/down
    assert exist([["A", "B", "C"], ["F", "E", "D"]], "ABCDEF") is True

    # All letters present but no adjacent path connects them
    assert exist([["A", "B", "C", "D"]], "ABDC") is False

    print("All tests passed")


if __name__ == "__main__":
    test_exist()
