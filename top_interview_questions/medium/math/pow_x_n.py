class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        invert = n < 0
        n = abs(n)
        current = x
        while n > 0:
            if n & 1:
                res *= current
            current *= current
            n >>= 1
        if invert:
            return 1 / res
        else:
            return res
