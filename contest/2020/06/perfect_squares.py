from math import sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        x = int(sqrt(n))
        dp = [2 ** 31] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, x + 1):
                sq = j ** 2
                if i == sq:
                    dp[i] = 1
                elif i > sq:
                    dp[i] = min(dp[i], dp[i - sq] + 1)
                else:
                    break
        return dp[n]
