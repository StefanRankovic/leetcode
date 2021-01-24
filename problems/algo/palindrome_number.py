class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        stack = []
        while x > 0:
            stack.append(x % 10)
            x //= 10
        for i in range(len(stack) // 2):
            if stack[i] != stack[-i-1]:
                return False
        return True
