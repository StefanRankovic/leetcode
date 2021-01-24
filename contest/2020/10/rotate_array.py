class Solution:
    def rotate(self, nums, k: int) -> None:
        if k == 0:
            return
        size = len(nums)
        if k > size:
            k = k % size
        nums.reverse()
        nums[0:k] = reversed(nums[0:k])
        nums[k:size] = reversed(nums[k:size]) 
