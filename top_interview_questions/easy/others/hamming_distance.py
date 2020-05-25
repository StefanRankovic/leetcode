class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        top = 2 ** 31
        diff = x ^ y
        count = 0
        while top > 0:
            if top & diff:
                count += 1
            top = top >> 1
        return count
