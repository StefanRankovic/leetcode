from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0] - coordinates[1][0] == 0:
            for c in coordinates:
                if c[0] != coordinates[0][0]:
                    return False
        else:
            a = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
            b = coordinates[0][1] - coordinates[0][0] * a
            for c in coordinates:
                if c[1] != a * c[0] + b:
                    return False
        return True
