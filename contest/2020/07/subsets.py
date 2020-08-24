from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_res = []
            for row in res:
                new_res.append(row)
                new_res.append([*row, num])
            res = new_res
        return res
