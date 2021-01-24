from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[1] <= arr[0]:
            return False
        rising = True
        for i in range(2, len(arr)):
            if rising:
                if arr[i] < arr[i-1]:
                    rising = False
            else:
                if arr[i] >= arr[i-1]:
                    return False
        return not rising
