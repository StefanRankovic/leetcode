# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(next = head)
        cur = prev.next
        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                prev.next = cur
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
