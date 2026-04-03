class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        the input matrix's each row is sorted ascending,
            but there may be duplicated num in each row,
            but it guarantees the first num of each row is greater than previous's row's last num,
            so duplicates don't matter, just check if the target is in the matrix or not,
            note duplicates won't happen across all rows in matrix

        it guarantees the first num of each row is greater than this row's previous one,
            the requirement is just checking the target in this matrix or not,
            so index [i, j] isn't what we want,
            instead, treat this matrix as the non-decreasing sequence,
            so do a basic binary search the current k-th number is equal to target or not,
            the first num is k = 1 and the last num is k = m * n ,
            where k represents what k-th number in this matrix

        time = O(log(m * n)), cuz there're m * n nums
        space = O(1)
        """
        
        m, n = len(matrix), len(matrix[0])
        one, two = 0, m * n - 1
        
        while one <= two:
            k = (two - one) // 2 + one
            r, c = divmod(k, n)
            # r, c = k // n, k % n
            
            if matrix[r][c] > target:
                two = k - 1
            
            elif matrix[r][c] < target:
                one = k + 1
            
            else:
                return True
        
        return False


searchMatrix = Solution().searchMatrix

def test_searchMatrix():
    # LeetCode examples
    assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
    assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False

    # Edge cases
    assert searchMatrix([[3]], 3) == True
    assert searchMatrix([[3]], -1) == False
    assert searchMatrix([[3, 5]], 5) == True
    assert searchMatrix([[3, 5]], -2) == False
    assert searchMatrix([[-2, -1, 3, 5]], -2) == True
    assert searchMatrix([[3, 5], [6, 6]], 6) == True
    assert searchMatrix([[3, 5], [6, 6]], 0) == False
    assert searchMatrix([[3, 5, 5], [6, 6, 6], [7, 8, 9]], 9) == True
    assert searchMatrix([[3, 5, 5], [6, 6, 6], [7, 8, 9]], 3) == True
    assert searchMatrix([[-4, -3, -2], [-1, 0, 1], [2, 3, 4]], 3) == True
    assert searchMatrix([[-4, -3, -2], [-1, 0, 1], [2, 3, 4]], 5) == False


    print("All tests passed")

if __name__ == "__main__":
    test_searchMatrix()
