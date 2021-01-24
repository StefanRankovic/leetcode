from typing import List

class Solution:
    def inc(self, digits, i, carry):
        plus_one = digits[i] + carry
        digit = plus_one % 10
        carry = plus_one // 10
        digits[i] = digit
        return carry
        
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while carry != 0:
            if i == -1:
                digits.insert(0, carry)
                break
            carry = self.inc(digits, i, carry)
            i -= 1
        return digits
            
