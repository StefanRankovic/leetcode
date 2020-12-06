class Solution:
    def maxPower(self, s: str) -> int:
        prev = ''
        longest = current = 1
        for letter in s:
            if letter == prev:
                current += 1
            else:
                current = 1
                prev = letter
            longest = max(longest, current)
        return longest
