from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = arr[0]-1
        if counter>=k:
            return arr[0]-(counter-k)-1        
        for i in range(len(arr)-1):
            counter += arr[i+1]-arr[i]-1
            if counter>=k:
                return arr[i+1]-(counter-k)-1
        return k-counter+arr[-1]
