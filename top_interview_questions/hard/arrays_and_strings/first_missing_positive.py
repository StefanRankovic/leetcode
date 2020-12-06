from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            return 1 if nums[0] != 1 else 2
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[j] < 1:
                j -= 1
                continue
            if nums[i] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                continue
            i+=1
        if j == 0 and nums[0] < 1:
            return 1
        for i in range(j+1):
            pos = max(nums[i], -nums[i]) - 1
            if pos < len(nums):
                nums[pos] = min(nums[pos], -nums[pos])
        for i in range(j+1):
            if nums[i] > 0:
                return i+1
        return j+2
