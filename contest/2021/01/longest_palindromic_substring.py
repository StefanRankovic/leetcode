class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ''
        for i in range(len(s)):
            j = k = i
            while j >= 0 and k < len(s):
                if s[j] != s[k]:
                    break
                if len(best) < k-j+1:
                    best = s[j:k+1]
                j -= 1
                k += 1
            j, k = i, i+1
            while j >= 0 and k < len(s):
                if s[j] != s[k]:
                    break
                if len(best) < k-j+1:
                    best = s[j:k+1]
                j -= 1
                k += 1
        return best
