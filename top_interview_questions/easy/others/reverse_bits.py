class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        power = 31
        while n > 0:
            if n & 1 > 0:
                result += 1 << power
            n = n >> 1
            power -= 1
        return result
