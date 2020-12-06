from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        upath = dpath = longest = 0
        ldir = None
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if ldir is not True:
                    if upath != 0 and dpath != 0:
                        longest = max(longest, upath + dpath + 1)
                    upath = 0
                ldir = True
                upath += 1
            elif A[i] < A[i-1]:
                if ldir is not False:
                    dpath = 0
                ldir = False
                dpath += 1
            else:
                if ldir is False and upath != 0 and dpath != 0:
                    longest = max(longest, upath + dpath + 1)
                ldir = None
                upath = dpath = 0
        if ldir is False and upath != 0 and dpath != 0:
            longest = max(longest, upath + dpath + 1)
        return longest
