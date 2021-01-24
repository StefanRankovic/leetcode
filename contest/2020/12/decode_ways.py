class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, len(s)):
            if s[i-1] == '1' or (s[i-1] == '2' and '0' <= s[i] <= '6'):
                if s[i] == '0':
                    dp.append(dp[-2])
                else:
                    dp.append(dp[-1] + dp[-2])
            elif s[i] == '0':
                return 0
            else:
                dp.append(dp[-1])
        return dp[-1]
