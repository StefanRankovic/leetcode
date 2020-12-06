from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        total = duration
        for i in range(len(timeSeries) - 1):
            diff = timeSeries[i+1] - timeSeries[i]
            total += diff if diff < duration else duration
        return total
