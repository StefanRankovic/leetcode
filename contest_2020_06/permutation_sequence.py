class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k = k - 1
        
        facts = [1]
        for i in range(1, n):
            facts.insert(0, i * facts[0])
            
        fradix = []
        for fact in facts:
            choice = k // fact
            fradix.append(choice)
            k = k - choice * fact
        
        remaining = list(range(1, n+1))

        result = ''
        for each in fradix:
            result += str(remaining[each])
            remaining.pop(each)
        return result
        
