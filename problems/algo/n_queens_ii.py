class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if 2 <= n <= 3:
            return 0
        self.count = 0
        stack = []
        def gen_num():
            for i in range(n):
                if len(stack) == 0:
                    stack.append(i)
                    gen_num()
                    stack.pop()
                elif i not in stack:
                    for j in range(len(stack)):
                        if abs(stack[j] - i) == abs(len(stack) - j):
                            break
                    else:
                        stack.append(i)
                        if len(stack) == n:
                            self.count += 1
                        else:
                            gen_num()
                        stack.pop()
        gen_num()
        return self.count
