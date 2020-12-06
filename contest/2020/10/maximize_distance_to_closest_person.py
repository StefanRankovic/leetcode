from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        cur = inf
        dist1 = [inf] * len(seats)
        dist2 = [inf] * len(seats)
        for i in range(len(seats)):
            if seats[i] == 1:
                cur = 0
            else:
                cur += 1
            dist1[i] = cur
        cur = inf
        for i in reversed(range(len(seats))):
            if seats[i] == 1:
                cur = 0
            else:
                cur += 1
            dist2[i] = cur
        return max([min(dist1[i], dist2[i]) for i in range(len(dist1))])
