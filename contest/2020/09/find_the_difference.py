import string

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = dict.fromkeys(string.ascii_lowercase, 0)
        for letter in t:
            freq[letter] += 1
        for letter in s:
            freq[letter] -= 1
        for letter in freq:
            if freq[letter] == 1:
                return letter
