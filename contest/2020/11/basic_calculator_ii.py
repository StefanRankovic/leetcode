class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = ''
        for c in s:
            if c.isnumeric():
                cur += c
            else:
                if cur != '':
                    stack.append(cur)
                    cur = ''
                    if len(stack) > 2 and (stack[-2] == '*' or stack[-2] == '/'):
                        op2 = int(stack.pop())
                        sign = stack.pop()
                        op1 = int(stack.pop())
                        if sign == '*':
                            res = op1 * op2
                        else:
                            res = int(op1 / op2)
                        stack.append(str(res))
                if c == '+':
                    continue
                elif c == '-':
                    cur += c
                elif c == '*' or c == '/':
                    stack.append(c)
        if cur != '':
            stack.append(cur)
            cur = ''
            if len(stack) > 2 and (stack[-2] == '*' or stack[-2] == '/'):
                op2 = int(stack.pop())
                sign = stack.pop()
                op1 = int(stack.pop())
                if sign == '*':
                    res = op1 * op2
                else:
                    res = int(op1 / op2)
                stack.append(str(res))
        print(stack)
        return sum([int(x) for x in stack])
