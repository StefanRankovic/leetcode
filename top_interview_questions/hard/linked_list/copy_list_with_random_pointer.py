"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next
        current = head
        while current:
            copy = current.next
            if current.random:
                copy.random = current.random.next
            current = copy.next
        current = head
        head2 = head.next
        while current:
            temp = current.next
            if current.next:
                current.next = temp.next
            current = temp
        return head2
