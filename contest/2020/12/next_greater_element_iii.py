class Solution:
    def nextGreaterElement(self, n: int) -> int:
        d = list(str(n))
        for i in reversed(range(len(d)-1)):
            if d[i] < d[i+1]:
                j = d.index(min([x for x in d[i+1:] if x > d[i]]), i+1)
                d[i], d[j] = d[j], d[i]
                break
        else:
            return -1
        d[i+1:] = sorted(d[i+1:])
        res = int(''.join(d))
        return res if res < 2 ** 31 else -1 
