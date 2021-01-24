class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        result = [d for d in num[k:]]
        for i in reversed(range(k)):
            largest = num[i]
            pos = 0
            for j in range(len(result)):
                if result[j] >= largest:
                    largest = result[j]
                    pos = j
                else:
                    break
            if num[i] < result[pos]:
                result.pop(pos)
                result.insert(0, num[i])
        while len(result) > 1 and result[0] == '0':
            result.pop(0)
        return ''.join(result)
        
