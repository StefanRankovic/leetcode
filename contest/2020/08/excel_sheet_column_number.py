class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        for each in s:
            total = total * 26 + ord(each) + 1 - ord('A')
        return total
