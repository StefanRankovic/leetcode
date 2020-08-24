class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        biggest = 1 << 31
        return n > 0 and biggest % n == 0
