"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        graph = {}
        seen = set()
        def dfs(node):
            if node and node in seen:
                return
            graph[node] = Node(node.val)
            seen.add(node)
            for n in node.neighbors:
                dfs(n)
                graph[node].neighbors.append(graph[n])
        dfs(node)
        return graph[node]
