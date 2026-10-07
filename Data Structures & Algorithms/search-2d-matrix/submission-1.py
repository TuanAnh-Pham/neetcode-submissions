class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        r = 0 
        c = maxCol - 1

        while r < maxRow and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True

        return False