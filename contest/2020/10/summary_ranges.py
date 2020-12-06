from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def append(a, b, result):
            if a is None:
                return
            if a != b:
                result.append(f'{a}->{b}')
            else:
                result.append(f'{a}')
        result = []
        a = b = None
        for each in nums:
            if a is None:
                a = b = each
                continue
            if b + 1 == each:
                b = each
            else:
                append(a, b, result)
                a = b = each
        append(a, b, result)
        return result
