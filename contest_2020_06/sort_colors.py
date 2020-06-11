class Solution:
    def sortColors(self, nums) -> None:
        i0 = i = 0
        i2 = len(nums) - 1
        while i <= i2:
            if nums[i] == 0:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[i2] = nums[i2], nums[i]
                i2 -= 1
        
