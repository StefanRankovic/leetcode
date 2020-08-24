class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextRow(row):
            new = [0] * 8
            for i in range(1, 7):
                if row[i - 1] == row[i + 1]:
                    new[i] = 1
                else:
                    new[i] = 0
            return new
        cache = [cells]
        loopstart = -1
        while True:
            N -= 1
            row = nextRow(cache[-1])
            if N == 0:
                return row
            if row in cache:
                loopstart = cache.index(row)
                break
            cache.append(row)
        loopsize = len(cache) - loopstart
        N %= loopsize
        return cache[loopstart + N]
        
