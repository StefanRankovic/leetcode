from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(res, cur, rem):
            for each in rem:
                nrem = list(rem)
                nrem.remove(each)
                ncur = list(cur)
                ncur.append(each)
                if not nrem:
                    res.append(ncur)
                else:
                    backtrack(res, ncur, nrem)
        res = []
        backtrack(res, [], nums)
        return res
