from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def toposort(courses, i, order, visited):
            visited[i] = 1
            for c in courses[i]:
                if visited[c] == 0:
                    toposort(courses, c, order, visited)
                if visited[c] == 1:
                    raise Exception()
            visited[i] = 2
            order.insert(0, i)
        courses = { x: [] for x in range(numCourses) }
        for p in prerequisites:
            courses[p[1]].append(p[0])
        order = []
        visited = { x: 0 for x in range(numCourses) }
        try:
            for i in range(numCourses):
                if not visited[i]:
                    toposort(courses, i, order, visited)
            return order
        except:
            return []
