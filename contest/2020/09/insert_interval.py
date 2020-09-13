from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert = len(intervals)
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                insert = i
                break
        intervals.insert(insert, newInterval)
        while insert + 1 < len(intervals):
            val = intervals[insert+1]
            if newInterval[1] >= val[0]:
                newInterval[0] = min(newInterval[0], val[0])
                newInterval[1] = max(newInterval[1], val[1])
                intervals.pop(insert+1)
            else:
                break
        return intervals
