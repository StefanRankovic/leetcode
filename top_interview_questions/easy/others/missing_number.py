class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        snums = sum(nums)
        sall = sum(range(len(nums) + 1))
        return sall - snums
