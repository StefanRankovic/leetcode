from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for each in strs:
            s = ''.join(sorted(each))
            if s not in res:
                res[s] = [each]
            else:
                res[s].append(each)
        return res.values()
