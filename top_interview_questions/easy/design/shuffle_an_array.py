import random

class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.current = list(nums)

    def reset(self):
        self.current = list(self.nums)
        return self.current
        

    def shuffle(self):
        for i in range(len(self.current)):
            j = random.randrange(i, len(self.current))
            self.current[i], self.current[j] = self.current[j], self.current[i]
        return self.current
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
