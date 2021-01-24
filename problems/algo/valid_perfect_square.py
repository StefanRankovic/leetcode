class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num
        while True:
            n = (lo + hi) // 2
            if n*n == num:
                return True
            elif n*n < num:
                lo = n
            else:
                hi = n
            if lo+1 == hi:
                return False
            
