class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = dict()
        for each in nums1:
            if each in seen:
                seen[each] = seen[each] + 1
            else:
                seen[each] = 1
        result = []
        for each in nums2:
            if each in seen and seen[each] > 0:
                result.append(each)
                seen[each] = seen[each] - 1
        return result
