class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zeroes += 1
                del nums[i]
            else:
                i += 1
        nums.extend([0] * zeroes)
