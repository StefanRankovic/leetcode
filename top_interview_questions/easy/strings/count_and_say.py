class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        low = self.countAndSay(n - 1)
        seen_last = None
        seen_times = 0
        result = ''
        for x in low:
            if x != seen_last:
                if seen_last:
                    result += str(seen_times) + str(seen_last)
                seen_last = x
                seen_times = 1
            else:
                seen_times += 1
        result += str(seen_times) + str(seen_last)
        return result
            
