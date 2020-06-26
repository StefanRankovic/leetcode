class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        start = 0
        jump = nums[start]
        while jump > 0:
            if start + jump >= len(nums) - 1:
                return True
            nmax = -1
            imax = -1
            for i in range(start, start+jump+1):
                if nums[i] + i >= nmax + imax:
                    nmax = nums[i]
                    imax = i
            start = imax
            jump = nums[start]
        return False
                
        
