from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        seen = dict()
        out = []
        for i in range(len(s) - 9):
            cur = s[i:i+10]
            if cur not in seen:
                seen[cur] = 1
            else:
                seen[cur] += 1
                if seen[cur] == 2:
                    out.append(cur)
        return out
