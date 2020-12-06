class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        shift = 1
        while shift <= N:
            shift <<= 1
        return shift + ~N
