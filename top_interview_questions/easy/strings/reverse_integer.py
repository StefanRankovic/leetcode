class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        numstr = str(x)[::-1]
        if numstr[-1] == '-':
            numstr = '-' + numstr[:-1]
        result = int(numstr)
        if (-1 << 31) < result < (1 << 31) - 1:
            return result
        else:
            return 0
    
