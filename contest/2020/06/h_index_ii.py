class Solution:
    def hIndex(self, citations) -> int:
        h = 0
        for i in reversed(range(len(citations))):
            if citations[i] < len(citations) - i:
                break
            h = min(citations[i], len(citations) - i)
        return h
