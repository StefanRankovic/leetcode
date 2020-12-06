from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        queue = []
        for ast in asteroids:
            if ast >= 0:
                queue.append(ast)
            else:
                destroyed = False
                while len(queue) > 0 and queue[-1] >= 0:
                    if queue[-1] == abs(ast):
                        queue.pop()
                        destroyed = True
                        break
                    elif queue[-1] < abs(ast):
                        queue.pop()
                    else:
                        destroyed = True
                        break
                if not destroyed:
                    queue.append(ast)
        return queue
