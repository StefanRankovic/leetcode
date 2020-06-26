class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n //= 10
            return result
        fast = getSum(getSum(n))
        slow = getSum(n)
        while fast != 1 and fast != slow:
            fast = getSum(getSum(fast))
            slow = getSum(slow)
        return fast == 1
            
            
