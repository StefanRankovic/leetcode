class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        result = 0
        for i in range(32):
            pos = 1 << i
            abit = a & pos
            bbit = b & pos
            result |= carry ^ abit ^ bbit
            carry = (abit & bbit | abit & carry | bbit & carry) << 1
        return result | -(result & 0x80000000)
            
            
        
