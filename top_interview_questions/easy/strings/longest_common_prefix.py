class Solution:
    def maxsubstr(str1, str2):
        for i in range(len(
    def longestCommonPrefix(self, strs):
        lcp = ''
        i=0
        while True:
            char = None
            for each in strs:
                if i >= len(each):
                    return lcp
                if not char:
                    char = each[i]
                elif char != each[i]:
                    return lcp
            if not char:
                return lcp
            lcp += char
            i += 1
        return lcp
