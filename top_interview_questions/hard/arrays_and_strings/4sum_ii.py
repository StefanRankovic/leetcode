from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countab = Counter([x+y for x in A for y in B])
        countcd = Counter([x+y for x in C for y in D])
        total = 0
        for each in countab:
            if -each in countcd:
                total += countab[each] * countcd[-each]
        return total
