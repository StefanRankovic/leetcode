class MinStack:
    def __init__(self):
        self.backing = []
        

    def push(self, x: int) -> None:
        top = self.util()
        if not top:
            self.backing.append((x, x))
        else:
            self.backing.append((x, x if x < top[1] else top[1]))

    def pop(self) -> None:
        if self.util():
            self.backing.pop()

    def top(self) -> int:
        return self.util()[0]

    def getMin(self) -> int:
        return self.util()[1]

    def util(self):
        if len(self.backing) > 0:
            return self.backing[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
