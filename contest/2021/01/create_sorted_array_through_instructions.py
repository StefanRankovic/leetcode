from typing import List
from bisect import *

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sa = []
        cost = 0
        for i in instructions:
            l = bisect_left(sa, i)
            r = bisect_right(sa, i)
            cost += min(l, len(sa) - r)
            sa[r:r] = [i]
        return cost % (10 ** 9 + 7)
