from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        word_seen = set()
        
        
        def dfs(r: int, c: int, idx=0) -> bool:
            # base cases for dfs recursion call
            if idx == len(word):
                return True
            
            if (
                r not in range(rows) or  # make sure r is inbound
                c not in range(cols) or  # make sure c is inbound
                word[idx] != board[r][c] or
                (r, c) in word_seen
            ):
                return False

            # cuz found the word we want, keep looking for next word
            word_seen.add((r, c))
            idx_next_word = idx + 1

            # four directions
            can_find_path = (
                dfs(r + 1, c, idx_next_word) or
                dfs(r - 1, c, idx_next_word) or
                dfs(r, c + 1, idx_next_word) or
                dfs(r, c - 1, idx_next_word)
            )

            # if not found next word by all directions, this current path doesn't work
            word_seen.remove((r, c))

            return can_find_path
            

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    return True
        
        return False
