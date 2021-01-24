from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = []
        result = []
        for i in range(len(nums)):
            if len(dq) >= k:
                dq.pop(0)
            for j in reversed(range(len(dq))):
                if dq[j] < nums[i]:
                    dq[j] = nums[i]
                else:
                    break
            dq.append(nums[i])
            if i >= k-1:
                result.append(dq[0])
        return result
