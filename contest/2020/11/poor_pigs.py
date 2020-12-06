class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        num = 0
        while (minutesToTest // minutesToDie + 1) ** num < buckets:
            num += 1
        return num
