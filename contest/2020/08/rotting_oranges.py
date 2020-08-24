from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] == 1:
                grid[i][j] = 2
                return True
            return False
        def helper(grid):
            next_grid = []
            changed = False
            for i in range(len(grid)):
                next_grid.append(grid[i].copy())
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        c1 = rot(next_grid, i-1, j)
                        c2 = rot(next_grid, i+1, j)
                        c3 = rot(next_grid, i, j-1)
                        c4 = rot(next_grid, i, j+1)
                        changed = changed or c1 or c2 or c3 or c4
            return next_grid, changed
        def rotten(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return False
            return True
        current = grid
        count = 0
        while True:
            current, changed = helper(current)
            if not changed:
                if not rotten(current):
                    count = -1
                break
            count += 1
        return count
        
