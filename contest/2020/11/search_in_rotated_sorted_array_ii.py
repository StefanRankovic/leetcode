from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for each in nums:
            if each == target:
                return True
        return False
