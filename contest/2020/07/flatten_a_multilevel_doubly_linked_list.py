"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        stack = []
        while node is not None:
            if node.child is not None:
                if node.next is not None:
                    stack.append(node.next)
                node.next = node.child
                node.child.prev = node
                node.child = None
            elif node.next is None and stack:
                next = stack.pop()
                node.next = next
                next.prev = node
            node = node.next
        return head
        
