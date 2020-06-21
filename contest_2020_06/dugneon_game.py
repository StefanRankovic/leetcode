class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        if len(dungeon) == 0 or len(dungeon[0]) == 0:
            return 1
        row = [None] * len(dungeon[0])
        best = [row.copy() for i in range(len(dungeon))]
        best[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in reversed(range(len(dungeon) - 1)):
            best[i][-1] = max(1, best[i + 1][-1] - dungeon[i][-1])
        for j in reversed(range(len(dungeon[0]) - 1)):
            best[-1][j] = max(1, best[-1][j + 1] - dungeon[-1][j])
        for i in reversed(range(len(dungeon) - 1)):
            for j in reversed(range(len(dungeon[0]) - 1)):
                bestDown = max(1, best[i + 1][j] - dungeon[i][j])
                bestRight = max(1, best[i][j + 1] - dungeon[i][j])
                best[i][j] = min(bestDown, bestRight)
        return best[0][0]
