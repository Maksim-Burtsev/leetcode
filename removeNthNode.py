from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        ptr1 = ptr2 = dummy

        while n > 0:
            ptr2 = ptr2.next
            n -= 1

        while ptr2.next != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr1.next = ptr1.next.next

        return dummy.next
