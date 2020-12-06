from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = []
        def fill(cur):
            stack.append(candidates[cur])
            if sum(stack) == target:
                result.append(list(stack))
            elif sum(stack) < target:
                for i in range(cur, len(candidates)):
                    fill(i)
            stack.pop()
        return result
