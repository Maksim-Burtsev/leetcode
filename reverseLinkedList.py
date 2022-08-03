from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        curr = next_node = head

        while curr is not None:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node

        head = previous

        return head
