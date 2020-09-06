from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                j = i - c
                if j >= 0 and dp[j] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
