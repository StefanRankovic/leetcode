from typing import List
from collections import Counter

class Solution:     
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in reversed(sorted(Counter(nums).items(), key=lambda i: i[1]))][:k]
