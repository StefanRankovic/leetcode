from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        nums = []
        for i in range(9):
            for j in range(i, 9):
                nums.append(int(digits[j-i:j+1]))
        return [n for n in nums if low <= n <= high]
