from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tcounter = Counter(tasks)
        occurances = max(tcounter.values())
        occuring = len([t for t in tcounter.values() if t == occurances])
        return max(len(tasks), (occurances - 1) * (n + 1) + occuring)
