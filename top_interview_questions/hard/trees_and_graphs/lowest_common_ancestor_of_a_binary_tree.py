# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pstack = []
        qstack = []
        self.pfound = False
        self.qfound = False
        def trace(node):
            if not node or (self.pfound and self.qfound):
                return
            if not self.pfound:
                pstack.append(node)
            if not self.qfound:
                qstack.append(node)
            if node == p:
                self.pfound = True
            if node == q:
                self.qfound = True
            if node.left:
                trace(node.left)
                if not self.pfound:
                    pstack.pop()
                if not self.qfound:
                    qstack.pop()
            if node.right:
                trace(node.right)
                if not self.pfound:
                    pstack.pop()
                if not self.qfound:
                    qstack.pop()
        def lca():
            end = min(len(pstack), len(qstack))
            for i in range(end):
                if pstack[i] == qstack[i]:
                    continue
                return pstack[i-1]
            return pstack[end-1]
        trace(root)
        return lca()
