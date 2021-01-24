class Solution:
    def countArrangement(self, n: int) -> int:
        nums = set(range(1, n+1))
        stack = []
        def calc(nums):
            ways = 0
            for each in nums:
                if (len(stack) + 1) % each == 0 or each % (len(stack) + 1) == 0:
                    if (len(stack) + 1) == n:
                        return 1
                    new = set(nums)
                    new.remove(each)
                    stack.append(each)
                    ways += calc(new)
                    stack.pop()
            return ways
        return calc(nums)
        
