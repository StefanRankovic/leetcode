class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total = len(nums)
        if total <= 1:
            return total
        current = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == current:
                del nums[i]
                total -= 1
            else:
                current = nums[i]
                i += 1
        return total
