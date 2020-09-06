class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2, 0, -1):
            if n % i == 0:
                sample = s[0:i]
                found = True
                for j in range(i, n, i):
                    if sample != s[j:j+i]:
                        found = False
                        break
                if found:
                    return found
        return False
