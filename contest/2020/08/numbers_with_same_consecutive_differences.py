from typing import List

class Solution:
    def old(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        mapping = { i:[] for i in range(10) }
        for i in range(10):
            if i + K < 10:
                mapping[i].append(i + K)
            if i - K >= 0:
                mapping[i].append(i - K)
        result = set()
        def createNumber(num, digit, i):
            if i == N:
                result.add(num)
                return
            num = num * 10 + digit
            for next in mapping[digit]:
                createNumber(num, next, i + 1)
        for digit in range(1, 10):
            createNumber(0, digit, 0)
        return list(result)
