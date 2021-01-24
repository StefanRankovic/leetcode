class Solution:
    def simplifyPath(self, path: str) -> str:
        levels = path.split('/')
        stack = []
        for each in levels:
            if each == '' or each == '.':
                continue
            elif each == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(each)
        return '/' + '/'.join(stack)
