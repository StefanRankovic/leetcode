from typing import List

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        A.sort()
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            cmax = max(A[i] + K, A[-1] - K)
            cmin = min(A[0] + K, A[i+1] - K)
            res = min(res, cmax - cmin)
        return res
