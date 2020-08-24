#class Solution:
#    def addDigits(self, num: int) -> int:
#        if num == 0:
#            return 0
#        diff = num - (num // 9) * 9
#        return diff if diff != 0 else 9

class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
