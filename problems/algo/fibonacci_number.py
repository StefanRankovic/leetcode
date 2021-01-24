class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        n -= 1
        while n > 0:
            a, b = b, a+b
            n -= 1
        return b
