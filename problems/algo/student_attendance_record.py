class Solution:
    def checkRecord(self, s: str) -> bool:
        A = L = 0
        for r in s:
            if r == 'A':
                L = 0
                A += 1
                if A > 1:
                    return False
            elif r == 'L':
                L += 1
                if L > 2:
                    return False
            else:
                L = 0
        return True
