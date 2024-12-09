from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L = 0
        R = len(matrix[0])
        T = 0
        B = len(matrix)

        res = []
        while L < R and T < B:
            for i in range(L, R):
                res.append(matrix[T][i])
            T += 1

            for i in range(T, B):
                res.append(matrix[i][R - 1])
            R -= 1

            if L >= R or T >= B:
                break
            
            for i in range(R - 1, L - 1, -1):
                res.append(matrix[B - 1][i])
            B -= 1
            
            for i in range(B - 1, T - 1, -1):
                res.append(matrix[i][L])
            L += 1
        
        return res