class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for each in nums:
            if each in seen:
                seen[each] += 1
            else:
                seen[each] = 1
        for each in seen:
            if seen[each] == 1:
                return each
