class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        for i in range(10):
            digs = 9 * (i+1) * 10 ** i
            if n - digs > 0:
                n -= digs
            else:
                num = 10 ** i + (n-1) // (i+1)
                return int(str(num)[(n-1) % (i+1)])
        
