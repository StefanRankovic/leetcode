from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(i, j):
            if i > j or nums[i] > target or nums[j] < target:
                return [-1, -1]
            mid = (i + j) // 2
            if nums[mid] > target:
                return search(i, max(i, mid-1))
            elif nums[mid] < target:
                return search(min(j, mid+1), j)
            else:
                if i == j:
                    return [i, i]
                lres = search(i, max(i, mid-1))
                rres = search(min(j, mid+1), j)
                left = right = mid
                if lres[1] != -1:
                    left = lres[0]
                if rres[0] != -1:
                    right = rres[1]
                return [left, right]
        if len(nums) == 0:
            return [-1, -1]
        return search(0, len(nums)-1)
