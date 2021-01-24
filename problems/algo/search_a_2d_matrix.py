from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i = 0
        while i+1 < len(matrix) and matrix[i+1][0] <= target:
            i += 1
        for num in matrix[i]:
            if num == target:
                return True
            if num > target:
                return False
        return False
