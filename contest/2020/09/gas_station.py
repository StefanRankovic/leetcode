from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = total = start = lap = 0
        while lap < 3:
            if i == 0:
                lap += 1
            total += gas[i] - cost[i]
            i = (i + 1) % len(gas)
            if total < 0:
                total = 0
                start = i
            elif start == i:
                return start
        return -1
