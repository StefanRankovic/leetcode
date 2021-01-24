from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        up = True
        n = len(matrix)
        m = len(matrix[0])
        result = []
        i = j = 0
        for _ in range(n * m):
            result.append(matrix[i][j])
            if up:
                if i-1 < 0:
                    if j+1 >= m:
                        i += 1
                    else:
                        j += 1
                    up = False
                elif j+1 >= m:
                    i += 1
                    up = False
                else:
                    i -= 1
                    j += 1
            else:
                if j-1 < 0:
                    if i+1 >= n:
                        j += 1
                    else:
                        i += 1
                    up = True
                elif i+1 >= n:
                    j += 1
                    up = True
                else:
                    i += 1
                    j -= 1
        return result
                
