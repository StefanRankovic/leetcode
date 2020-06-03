class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda i: i[0] - i[1])
        half = len(costs) // 2
        return sum([i[0] for i in costs[:half]]) + sum([i[1] for i in costs[half + 1:]])
