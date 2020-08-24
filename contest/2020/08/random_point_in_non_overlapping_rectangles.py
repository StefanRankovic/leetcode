from typing import List
from random import randint
from random import choices

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = [(r[2] - r[0] + 1) * (r[3] - r[1] + 1) for r in rects]

    def pick(self) -> List[int]:
        rect = choices(self.rects, weights=self.areas, k=1)[0]
        rx = randint(rect[0], rect[2])
        ry = randint(rect[1], rect[3])
        return [rx, ry]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
