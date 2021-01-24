from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        need = {}
        cnt = 0
        for n in nums:
            if need.get(n, 0) > 0:
                need[n] -= 1
                cnt += 1
            elif k-n in need:
                need[k-n] += 1
            else:
                need[k-n] = 1
        return cnt
