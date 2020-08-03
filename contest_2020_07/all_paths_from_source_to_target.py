from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def visit(i, current, graph, result):
            current.append(i)
            if i == len(graph) - 1:
                result.append(current)
            for node in graph[i]:
                visit(node, current.copy(), graph, result)
        result = []
        visit(0, [], graph, result)
        return result
    
