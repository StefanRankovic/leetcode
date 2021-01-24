from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def check(val, i, j):
            if i >= len(matrix) or j >= len(matrix[0]):
                return True
            if matrix[i][j] == val:
                return check(val, i+1, j+1)
            else:
                return False
        for i in range(len(matrix)):
            if not check(matrix[i][0], i, 0):
                return False
        for j in range(len(matrix[0])):
            if not check(matrix[0][j], 0, j):
                return False
        return True
