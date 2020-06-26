class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zcol = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zcol = True
        zrow = False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                zrow = True
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zrow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if zcol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
