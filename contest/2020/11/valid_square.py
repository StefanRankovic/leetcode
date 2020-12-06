from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def sq_dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4:
            return False
        points = [p1, p2, p3, p4]
        points.sort(key = lambda x: (x[0], x[1]))
        c1, c2, c3, c4 = points
        d1 = sq_dist(c1, c2)
        d2 = sq_dist(c1, c3)
        d3 = sq_dist(c2, c4)
        d4 = sq_dist(c3, c4)
        dd1 = sq_dist(c1, c4)
        dd2 = sq_dist(c2, c3)
        return d1 == d2 == d3 == d4 and dd1 == dd2
