from typing import nums

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisect(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    return bisect(start, mid-1)
                else:
                    return bisect(mid+1, end)
            else:
                if nums[mid] < target <= nums[end]:
                    return bisect(mid+1, end)
                else:
                    return bisect(start, mid-1)
        return bisect(0, len(nums)-1)
