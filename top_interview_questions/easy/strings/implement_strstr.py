class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def cmp(haystack, needle, i):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    return False
            return True
        
        if needle == '':
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if cmp(haystack, needle, i):
                return i
        return -1
