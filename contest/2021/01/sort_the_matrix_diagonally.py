from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort(start_i, start_j):
            i, j = start_i, start_j
            elements = []
            while i < len(mat) and j < len(mat[0]):
                elements.append(mat[i][j])
                i += 1
                j += 1
            elements.sort()
            i, j = start_i, start_j
            for e in elements:
                mat[i][j] = e
                i += 1
                j += 1
        for i in range(len(mat)):
            sort(i, 0)
        for j in range(1, len(mat[0])):
            sort(0, j)
        return mat
