class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern):
            return False
        d1 = dict()
        d2 = dict()
        for i,w in enumerate(words):
            if w not in d1:
                if pattern[i] not in d2:
                    d1[w] = pattern[i]
                    d2[pattern[i]] = w
                else:
                    return False
            elif d1[w] != pattern[i]:
                return False
        return True
