from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                c1 = dp[i-1] + costs[0]
                c7 = dp[i-7] + costs[1] if i > 7 else costs[1]
                c30 =  dp[i-30] + costs[2] if i > 30 else costs[2]
                dp[i] = min(c1, c7, c30)
        return dp[-1]
