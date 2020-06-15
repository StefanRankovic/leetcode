class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        i = j = 0
        longest = 0
        while i < len(s) and j < len(s):
            if s[j] not in seen or seen[s[j]] == False:
                seen[s[j]] = True
                j += 1
            else:
                seen[s[i]] = False
                i += 1
            longest = max(longest, j - i)
        return longest
