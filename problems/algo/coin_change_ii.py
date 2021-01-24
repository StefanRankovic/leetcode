class Solution:
    def change(self, amount: int, coins) -> int:
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        dp = [0] * (amount + 1)
        for c in coins:
            for i in range(1, len(dp)):
                if i == c:
                    dp[i] += 1
                if i-c > 0:
                    dp[i] += dp[i-c]
        return dp[-1]
