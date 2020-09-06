from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        letters = { chr(i + 97):[-1,-1] for i in range(26) }
        for i,s in enumerate(S):
            if letters[s][0] == -1:
                letters[s][0] = i
            letters[s][1] = i + 1
        letters  = {x:letters[x] for x in letters if letters[x][0] != -1}
        ranges = []
        seen = set()
        for x in S:
            if x in seen:
                continue
            seen.add(x)
            merged = False
            for r in ranges:
                c1 = letters[x][0] >= r[0] and letters[x][0] < r[1]
                c2 = letters[x][1] > r[0] and letters[x][1] <= r[1]
                c3 = letters[x][0] < r[0] and letters[x][1] > r[1]
                if c1 or c2 or c3:
                    r[0] = min(r[0], letters[x][0])
                    r[1] = max(r[1], letters[x][1])
                    merged = True
                    break
            if not merged:
                ranges.append(letters[x])
        return [x[1] - x[0] for x in ranges]
