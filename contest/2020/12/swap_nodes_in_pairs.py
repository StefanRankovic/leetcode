# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(next=head)
        cur = head
        while cur:
            next = cur.next
            if next:
                cur.next = next.next
                next.next = cur
                prev.next = next
            prev = cur
            cur = cur.next
        return dummy.next
