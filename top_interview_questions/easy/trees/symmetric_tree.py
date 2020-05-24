# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getNextLevel(self, level):
        res = []
        for x in level:
            res.append(x.left if x else None)
            res.append(x.right if x else None)
        return res
        
    def isSymmetric(self, root: TreeNode) -> bool:
        current = [root]
        while not all(node is None for node in current):
            current = self.getNextLevel(current)
            vals = [x.val if x else None for x in current]
            length = len(current)
            for i in range(length//2):
                if vals[i] != vals [length - i - 1]:
                    return False
        return True
                
