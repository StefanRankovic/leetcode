# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = prehead = ListNode(next = head)
        while cur is not None:
            while cur.next is not None and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return prehead.next
