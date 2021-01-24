from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                low = prices[i]
            if prices[i] <= low:
                low = prices[i]
            else:
                current = prices[i] - low
                if current > profit:
                    profit = current
        return profit
