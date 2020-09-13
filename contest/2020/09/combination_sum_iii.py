from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combos = [[i] for i in range(1, 10)]
        for _ in range(k-1):
            current = []
            for c in combos:
                for i in range(10):
                    if i > c[-1]:
                        current.append([*c, i])
            combos = current
        return [c for c in combos if sum(c) == n]
