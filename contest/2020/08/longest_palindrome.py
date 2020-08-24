from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        odd = 0
        result = 0
        for v in cnt.values():
            if v % 2 == 0:
                result += v
            else:
                result += (v - 1)
                odd = 1
        return result + odd
