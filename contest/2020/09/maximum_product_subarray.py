from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        pmax = pmin = 1
        for n in nums:
            if n < 0:
                pmax, pmin = pmin, pmax
            pmax = max(n, n * pmax)
            pmin = min(n, n * pmin)
            best = max(best, pmax)
        return best
