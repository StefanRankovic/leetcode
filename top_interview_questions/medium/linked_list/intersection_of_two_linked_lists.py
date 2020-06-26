# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        currA = headA
        while currA:
            lenA += 1
            currA = currA.next
        lenB = 0
        currB = headB
        while currB:
            lenB += 1
            currB = currB.next
        while lenA > lenB:
            lenA -= 1
            headA = headA.next
        while lenB > lenA:
            lenB -= 1
            headB = headB.next
        currA = headA
        currB = headB
        while currA != currB and currA is not None:
            currA = currA.next
            currB = currB.next
        return currA
