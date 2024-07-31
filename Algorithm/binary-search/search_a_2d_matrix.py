from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    for row in range(0, len(matrix)):
        L = 0
        R = len(matrix[row]) - 1

        while L <= R:
            m = L + (R - L) // 2

            if matrix[row][m] < target:
                L = m + 1
            elif matrix[row][m] > target:
                R = m - 1
            else:
                return True
    
    return False
