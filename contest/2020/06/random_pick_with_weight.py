from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w) - 1
        self.mapping = dict()
        prev = 0
        for i in range(len(w)):
            self.mapping[i] = range(prev, w[i] + prev)
            prev += w[i]

    def pickIndex(self) -> int:
        rand = random.randint(0, self.total)
        for key, value in self.mapping.items():
            if rand in value:
                return key
