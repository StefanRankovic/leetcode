import math

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if n > math.ceil(len(flowerbed) / 2):
            return False
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n-=1
                flowerbed[i] = 1
                if n == 0:
                    return True
        return False
