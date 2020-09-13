from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == '1':
                grid[i][j] = '2'
                mark(i + 1, j)
                mark(i - 1, j)
                mark(i, j + 1)
                mark(i, j - 1)
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    mark(i, j)
        return cnt
