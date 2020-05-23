class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = 0
        for x in nums:
            sum ^= x
        return sum
