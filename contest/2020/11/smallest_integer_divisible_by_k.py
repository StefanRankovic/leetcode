class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 10 not in {1,3,7,9}:
            return -1
        seen = set()
        rem = 0
        for i in range(K):
            rem = (rem * 10 + 1) % K
            if rem in seen:
                return -1
            if rem == 0:
                return i + 1
            seen.add(rem)
