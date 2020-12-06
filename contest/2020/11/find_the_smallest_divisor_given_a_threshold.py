from typing import List
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo = 1
        hi = max(nums)
        while lo != hi:
            div = (lo + hi) // 2
            total = sum([ceil(n / div) for n in nums])
            if total <= threshold:
                hi = div
            else:
                lo = div + 1
        return lo
