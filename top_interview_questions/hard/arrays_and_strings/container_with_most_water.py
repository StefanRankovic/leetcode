from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0
        while i < j:
            area = max(area, (j-i) * min(height[i], height[j]))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return area