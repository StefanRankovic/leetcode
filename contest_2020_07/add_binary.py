class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(x, y, carry):
            res = int(x) + int(y) + carry
            if res == 0:
                return '0', 0
            elif res == 1:
                return '1', 0
            elif res == 2:
                return '0', 1
            else:
                return '1', 1
        if len(a) < len(b):
            diff = len(b) - len(a)
            a = '0' * diff + a
        elif len(b) < len(a):
            diff = len(a) - len(b)
            b = '0' * diff + b
        carry = 0
        result = ''
        for i in reversed(range(len(a))):
            digit, carry = add(a[i], b[i], carry)
            result = digit + result
        if carry == 1:
            result = '1' + result
        return result
                          
                          
            
