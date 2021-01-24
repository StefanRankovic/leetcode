from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1 = i2 = cur1 = cur2 = 0
        while cur1 < len(word1) and cur2 < len(word2):
            if word1[cur1][i1] != word2[cur2][i2]:
                return False
            i1 += 1
            if i1 >= len(word1[cur1]):
                i1 = 0
                cur1 += 1
            i2 += 1
            if i2 >= len(word2[cur2]):
                i2 = 0
                cur2 += 1
        return cur1 == len(word1) and cur2 == len(word2)
