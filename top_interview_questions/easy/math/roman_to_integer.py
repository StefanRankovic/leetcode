class Solution:
    def romanToInt(self, s: str) -> int:
        tokens = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            }
        prev = 1001
        integer = 0
        for each in s:
            i = tokens[each]
            if i <= prev:
                integer += i
            else:
                integer += i - 2*prev
            prev = i
        return integer
