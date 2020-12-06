class Solution:
    def decodeString(self, s: str) -> str:
        def unroll(s, i):
            result = ''
            repeat = 0
            while i < len(s):
                if s[i].isalpha():
                    result += s[i]
                elif s[i].isnumeric():
                    repeat = repeat * 10 + int(s[i])
                elif s[i] == '[':
                    inner, i = unroll(s, i + 1)
                    result += repeat * inner
                    repeat = 0
                else:
                    break
                i += 1
            return result, i
        return unroll(s, 0)[0]
