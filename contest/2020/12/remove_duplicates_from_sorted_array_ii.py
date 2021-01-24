from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = j = seen = 0
        cur = None
        while i < len(nums):
            if nums[i] == cur:
                seen += 1
            else:
                cur = nums[i]
                seen = 1
            if seen <= 2:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
