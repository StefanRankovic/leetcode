# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.deepest = []
        self.level = 0
        self.queue = []
        def bfs():
            if len(self.queue) == 0:
                return
            node, i = self.queue.pop(0)
            if node.left:
                self.queue.append((node.left, i+1))
            if node.right:
                self.queue.append((node.right, i+1))
            if i > self.level:
                self.level = i
                self.deepest = []
            if i == self.level:
                self.deepest.append(node)
            bfs()
            if len(self.deepest) == 1:
                return
            else:
                removed = False
                if node.left in self.deepest:
                    self.deepest.remove(node.left)
                    removed = True
                if node.right in self.deepest:
                    self.deepest.remove(node.right)
                    removed = True
                if removed:
                    self.deepest.append(node)
        self.queue.append((root, 0))
        bfs()
        return self.deepest[0]
