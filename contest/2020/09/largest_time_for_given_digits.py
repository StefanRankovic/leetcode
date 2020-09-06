from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        combos = [sum([x * (10 ** i) for i,x in enumerate(a)]) for a in permutations(A)]
        valids = [c for c in combos if c % 100 <= 59 and c // 100 <= 23]
        if not valids:
            return ''
        res = f'{max(valids)}'.zfill(4)
        return res[:2] + ':' + res[2:]
            
