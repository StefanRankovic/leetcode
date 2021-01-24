from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[triangle[0][0]]]
        for i in range(1, len(triangle)):
            dp.append([])
            for j in range(len(triangle[i])):
                l = dp[i-1][j-1] if j > 0 else inf
                r = dp[i-1][j] if j < len(triangle[i-1]) else inf
                dp[i].append(min(l, r) + triangle[i][j])
        return min(dp[-1])
