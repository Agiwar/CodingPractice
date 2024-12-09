from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    for item in matrix:
        L = 0
        R = len(item) - 1

        while L <= R:
            m = L + (R - L) // 2

            if item[m] < target:
                L = m + 1
            elif item[m] > target:
                R = m - 1
            else:
                return True

    return False
