from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = i = 0
        j = len(nums) - 1
        best = len(nums) + 1
        while i < len(nums) and total + nums[i] <= x:
            total += nums[i]
            i += 1
        if total == x:
            best = i
        while i >= 0 and j >= 0:
            total += nums[j]
            while total > x and i > 0:
                total -= nums[i-1]
                i -= 1
            if total == x:
                best = min(best, i + len(nums) - j)
            j -= 1
        return -1 if best > len(nums) else best
