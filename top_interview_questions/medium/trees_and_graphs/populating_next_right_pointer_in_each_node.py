"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_left(node):
            if node.left:
                node.left.next = node.right
                connect_left(node.left)
                connect_left(node.right)
        def connect_right(node):
            if node.right:
                if node.next:
                    node.right.next = node.next.left
                connect_right(node.right)
                connect_right(node.left)
        if root:
            connect_left(root)
            connect_right(root)
        return root
