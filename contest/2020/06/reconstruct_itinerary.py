from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def visit(node):
            self.order.append(node)
            for s in self.graph[node]:
                if not s[1]:
                    s[1] = True
                    done = visit(s[0])
                    if done:
                        return True
                    s[1] = False
            if len(self.order) == self.total:
                return True
            self.order.pop()
            return False
                    
        self.total = len(tickets) + 1
        self.order = []
        airports = set()
        for t in tickets:
            airports.add(t[0])
            airports.add(t[1])
        self.graph = { a: [] for a in airports }
        for t in tickets:
            self.graph[t[0]].append([t[1], False])
        for s in self.graph.values():
            s.sort(key=lambda x: x[0])
        visit('JFK')
        return self.order
