# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        def reverse(node):
            if node.next is not None:
                first, last = reverse(node.next)
                last.next = node
                node.next = None
                return first, node
            return node, node
            
        first, last = reverse(head)
        return first
            
