from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums, default=0)
        def houseRobber(houses):
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(dp[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[-1]
        first = houseRobber(nums[:len(nums)-1])
        second = houseRobber(nums[1:])
        return max(first, second)
