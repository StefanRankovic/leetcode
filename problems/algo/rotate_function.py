from typing import List

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        total = sum(A)
        result = F = sum(A[i] * i for i in range(len(A)))
        for i in range(len(A)):
            F = F - total + A[i] * len(A)
            result = max(result, F)
        return result
