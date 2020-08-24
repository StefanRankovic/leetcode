class Solution:
    def nthUglyNumber(self, n: int) -> int:
        twos = []
        threes = []
        fives = []
        current = 1
        while n > 1:
            twos.append(current * 2)
            threes.append(current * 3)
            fives.append(current * 5)
            current = min(twos[0], threes[0], fives[0])
            if current >= twos[0]:
                twos.pop(0)
            if current >= threes[0]:
                threes.pop(0)
            if current >= fives[0]:
                fives.pop(0)
            n -= 1
        return current
