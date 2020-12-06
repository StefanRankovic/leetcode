from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = dict()
        for t in trips:
            if t[1] in stops:
                stops[t[1]] += t[0]
            else:
                stops[t[1]] = t[0]
            if t[2] in stops:
                stops[t[2]] -= t[0]
            else:
                stops[t[2]] = -t[0]
        running = 0
        for s in sorted(stops.keys()):
            running += stops[s]
            if running > capacity:
                return False
        return True
