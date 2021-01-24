from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while True:
            twosum = numbers[i] + numbers[j]
            if twosum == target:
                return [i+1, j+1]
            elif twosum > target:
                j -= 1
            else:
                i += 1
