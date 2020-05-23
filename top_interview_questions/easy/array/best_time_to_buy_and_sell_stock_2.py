class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            running = prices[i+1] - prices[i]
            if running > 0:
                profit += running
        return profit
