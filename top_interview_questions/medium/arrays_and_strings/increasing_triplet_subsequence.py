from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = mid = float('inf')
        for n in nums:
            if low >= n:
                low = n
            elif mid >= n:
                mid = n
            else:
                return True
        return False
