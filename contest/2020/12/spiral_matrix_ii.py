from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        i = j = 0
        direction = 'R'
        for k in range(1, n*n + 1):
            matrix[i][j] = k
            if direction == 'R':
                if j+1 < n and matrix[i][j+1] == 0:
                    j += 1
                else:
                    i += 1
                    direction = 'D'
            elif direction == 'D':
                if i+1 < n and matrix[i+1][j] == 0:
                    i += 1
                else:
                    j -= 1
                    direction = 'L'
            elif direction == 'L':
                if j-1 >= 0 and matrix[i][j-1] == 0:
                    j -= 1
                else:
                    i -= 1
                    direction = 'U'
            else:
                if i-1 >= 0 and matrix[i-1][j] == 0:
                    i -= 1
                else:
                    j += 1
                    direction = 'R'
        return matrix
