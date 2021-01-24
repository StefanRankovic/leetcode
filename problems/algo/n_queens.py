class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]
        if 2 <= n <= 3:
            return []
        row = '.' * n
        table = [row[:i] + 'Q' + row[i+1:] for i in range(n)]
        result = []
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
                            result.append([table[s] for s in stack])
                        else:
                            gen_num()
                        stack.pop()
        gen_num()
        return result
                    
