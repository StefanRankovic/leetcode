class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for each in tokens:
            try:
                stack.append(int(each))
            except ValueError:
                op1 = stack.pop()
                op2 = stack.pop()
                if each == '+':
                    res = op2 + op1
                elif each == '-':
                    res = op2 - op1
                elif each == '*':
                    res = op2 * op1
                else:
                    res = int(op2 / op1)
                stack.append(res)
        return stack.pop()
        
