class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        current = 0
        for letter in t:
            if s[current] == letter:
                current += 1
                if current == len(s):
                    return True
        return False
