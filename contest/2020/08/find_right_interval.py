from typing import List
import bisect
                
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        d = { x[0]:i for i,x in enumerate(intervals) }
        result = [-1] * len(intervals)
        s = sorted(list(d.keys()))
        for i in range(len(intervals)):
            j = bisect.bisect_left(s, intervals[i][1])
            result[i] = d[s[j]] if j < len(intervals) else -1
        return result
