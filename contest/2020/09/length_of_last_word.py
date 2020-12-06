class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rstripped = s.rstrip()
        total = 0
        for i in reversed(range(len(rstripped))):
            if rstripped[i].isspace():
                break
            total += 1
        return total
