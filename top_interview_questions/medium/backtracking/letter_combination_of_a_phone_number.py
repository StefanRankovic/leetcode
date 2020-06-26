class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        pads = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        combos = 1
        for i in range(1, len(digits)):
            combos *= len(pads[digits[i]])
        res = pads[digits[0]] * combos
        res.sort()
        for i in range(1, len(digits)):
            cur = pads[digits[i]]
            for j in range(len(res)):
                res[j] += cur[j % len(cur)]
            res.sort()
        return res
