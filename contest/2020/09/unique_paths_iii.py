from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.plen = 1
        self.result = 0
        visited = [None] * len(grid)
        for i in range(len(grid)):
            visited[i] = [False] * len(grid[0])
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    self.plen += 1
        def visit(i, j, pathlen):
            if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0]) or
                grid[i][j] == -1 or visited[i][j]):
                return
            elif grid[i][j] == 2 and pathlen == self.plen:
                self.result += 1
            else:
                pathlen += 1
                visited[i][j] = True
                visit(i + 1, j, pathlen)
                visit(i - 1, j, pathlen)
                visit(i, j + 1, pathlen)
                visit(i, j - 1, pathlen)
                pathlen -= 1
                visited[i][j] = False
        visit(start[0], start[1], 0)
        return self.result
