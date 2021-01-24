class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1,1,1,1,1]]
        for i in range(1, n):
            new = []
            oc = 0
            for j in range(5):
                oc += dp[-1][j]
                new.append(oc)
            dp.append(new)
        return sum(dp[-1])
