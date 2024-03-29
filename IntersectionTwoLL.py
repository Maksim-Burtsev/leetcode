from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        ptr1 = headA
        ptr2 = headB

        while ptr1 is not ptr2:
            ptr1 = headB if ptr1 is None else ptr1.next
            ptr2 = headA if ptr2 is None else ptr2.next

        return ptr1
