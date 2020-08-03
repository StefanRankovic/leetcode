class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = first = second = 0
        for num in nums:
            xor ^= num
        one = xor & (-xor)
        for num in nums:
            if one & num:
                first ^= num
            else:
                second ^= num
        return [first, second]
