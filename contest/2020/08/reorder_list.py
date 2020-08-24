# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return
        slow = fast = head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        stack = []
        while slow is not None:
            stack.append(slow)
            slow = slow.next
        while stack:
            node = stack.pop()
            node.next = head.next
            head.next = node
            head = node.next
        head.next = None
