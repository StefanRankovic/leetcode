from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = nums[0]
        j = nums[nums[0]]
        while i != j:
            i = nums[i]
            j = nums[nums[j]]
        i = 0
        while i != j:
            i = nums[i]
            j = nums[j]
        return i
            
            
            
