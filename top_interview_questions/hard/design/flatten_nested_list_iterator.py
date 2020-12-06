# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.ind = 0
        self.cur = nestedList
    
    def next(self) -> int:
        print(self.ind, self.cur)
        if self.ind >= len(self.cur):
            self.ind, self.cur = self.stack.pop()
        while not self.cur[self.ind].isInteger():
            self.stack.append((self.ind + 1, self.cur))
            self.cur = self.cur[self.ind].getList()
            self.ind = 0
        result = self.cur[self.ind].getInteger()
        self.ind += 1
        return result
    
    def hasNext(self) -> bool:
         return self.ind < len(self.cur) or len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
