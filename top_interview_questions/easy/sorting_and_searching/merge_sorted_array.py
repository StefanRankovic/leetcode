class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m -= 1
        n -= 1
        for last in reversed(range(len(nums1))):
            if m < 0:
                nums1[last] = nums2[n]
                n -= 1
                continue
            if n < 0:
                nums1[last] = nums1[m]
                m -= 1
                continue
            if nums1[m] >= nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            elif nums1[m] < nums2[n]:
                nums1[last] = nums2[n]
                n -= 1
            
