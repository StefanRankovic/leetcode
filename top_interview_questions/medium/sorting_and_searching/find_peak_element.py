from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = nums[i-1] if i > 0 else -inf
            right = nums[i+1] if i < len(nums)-1 else -inf
            if left < nums[i] > right:
                return i
            
