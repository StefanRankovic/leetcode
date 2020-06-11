class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        last = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return last
            i += 1
            last = i
        return last
