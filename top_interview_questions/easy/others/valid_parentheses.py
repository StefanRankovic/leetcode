class Solution:
    def isValid(self, s: str) -> bool:
        o_parens = {'(' : 1, '{' : 2, '[' : 3}
        c_parens = {')' : 1, '}' : 2, ']' : 3}
        stack = []
        for each in s:
            if each in o_parens:
                stack.append(each)
            elif each in c_parens:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if o_parens[last] != c_parens[each]:
                    return False
        return len(stack) == 0
        
