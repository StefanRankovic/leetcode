class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return
        i = 0
        k = len(s) - 1
        while i < len(s)/2:
            temp = s[i]
            s[i] = s[k]
            s[k] = temp
            i += 1
            k -= 1
        