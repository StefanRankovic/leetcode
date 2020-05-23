class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = dict()
        for i, x in enumerate(s):
            if x not in seen:
                seen[x] = i
            else:
                seen[x] = None
        return min([e for e in seen.values() if e is not None], default = -1)
