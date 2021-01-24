from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = []
        maxc = 0
        for i in range(len(grid)):
            dp.append([])
            for _ in range(len(grid[0])):
                dp[i].append([0] * len(grid[0]))
            for j in range(min(i+1, len(grid[0]))):
                for k in range(max(0, len(grid[0])-i-1), len(grid[0])):
                    if k != j:
                        new = grid[i][j] + grid[i][k]
                    else:
                        new = grid[i][j]
                    prev = 0
                    if i > 0:
                        for p1 in range(j-1, j+2):
                            for p2 in range(k-1, k+2):
                                if 0 <= p1 < len(grid[0]) and 0 <= p2 < len(grid[0]):
                                    prev = max(prev, dp[i-1][p1][p2])
                    dp[i][j][k] = max(dp[i][j][k], new + prev)
                    maxc = max(maxc, dp[i][j][k])
        return maxc
