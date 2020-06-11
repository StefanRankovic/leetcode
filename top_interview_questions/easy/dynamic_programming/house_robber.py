class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        best = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            best.append(max(best[i-2] + nums[i], best[i-1]))
        return best[-1]
