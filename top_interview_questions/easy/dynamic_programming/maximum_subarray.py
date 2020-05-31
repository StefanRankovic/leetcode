class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        top = nums[0]
        running = 0
        for i in nums:
            running += i
            if running > top:
                top = running
            if running < 0:
                running = 0
        return top
