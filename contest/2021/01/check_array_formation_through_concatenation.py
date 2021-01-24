from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for p in pieces:
            try:
                ind = arr.index(p[0])
                while p != arr[ind:ind+len(p)]:
                    ind = arr.index(p[0], ind+1)
            except:
                return False
        return True
                
