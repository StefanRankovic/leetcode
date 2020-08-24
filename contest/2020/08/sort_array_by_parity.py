from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            while i < len(A) and A[i] % 2 == 0:
                i += 1
            while j >= 0 and A[j] % 2 != 0:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        return A
