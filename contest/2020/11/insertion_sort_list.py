# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        new = ListNode()
        while head:
            cur = new
            while cur.next and head.val > cur.next.val:
                cur = cur.next
            temp1 = head
            head = head.next
            temp2 = cur.next
            cur.next = temp1
            temp1.next = temp2
        return new.next
