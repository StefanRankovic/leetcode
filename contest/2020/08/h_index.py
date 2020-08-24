from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counter = [0] * (len(citations) + 1)
        for c in citations:
            counter[min(c, len(citations))] += 1
        h = len(citations)
        s = counter[h]
        while h > s:
            h -= 1
            s += counter[h]
        return h
