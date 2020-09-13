from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [nums[0]] * len(nums)
        rprod = [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            lprod[i] = lprod[i-1] * nums[i]
        for i in range(len(nums)-2, 0, -1):
            rprod[i] = rprod[i+1] * nums[i]
        out = [0] * len(nums)
        out[0] = rprod[1]
        out[-1] = lprod[-2]
        for i in range(1, len(nums)-1):
            out[i] = lprod[i-1] * rprod[i+1]
        return out
