# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def checkAdjecent(self, good, bad, n):
        if good + 1 == bad:
            return bad
        candidate = isBadVersion(n)
        if candidate:
            bad = n
        else:
            good = n
        return self.checkAdjecent(good, bad, (bad + good) // 2)
        
    def firstBadVersion(self, n):
        return self.checkAdjecent(0, n, n // 2)
        
