from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(res, cur, op, cl, n):
            if op < n:
                gen(res, cur + '(', op + 1, cl, n)
            if cl < op:
                gen(res, cur + ')', op, cl + 1, n)
            if len(cur) == 2 * n:
                res.append(cur)
        res = []
        gen(res, '(', 1, 0, n)
        return res
