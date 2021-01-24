from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x: x[0])
        out = []
        i = 1
        cur = intervals[0]
        while i < len(intervals):
            if cur[1] >= intervals[i][0]:
                cur[1] = max(cur[1], intervals[i][1])
            else:
                out.append(cur)
                cur = intervals[i]
            i += 1
        out.append(cur)
        return out
