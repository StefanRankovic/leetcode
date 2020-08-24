from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def check(grid, i, j):
            return int(not(0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1))
        perimiter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimiter += check(grid, i-1, j)
                    perimiter += check(grid, i+1, j)
                    perimiter += check(grid, i, j-1)
                    perimiter += check(grid, i, j+1)
        return perimiter                
        
