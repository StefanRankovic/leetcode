from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boats = 0
        while i <= j:
            if people[j] + people[i] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats
