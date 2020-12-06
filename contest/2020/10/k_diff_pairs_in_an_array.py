from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = dict()
        cnt = 0
        for n in nums:
            if n in diff and not diff[n]:
                diff[n] = True
                cnt += 1
            diff[n+k] = diff.get(n+k, False)
        return cnt
