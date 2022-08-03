from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_values = []
        while head:
            list_values.append(head.val)
            head = head.next

        return list_values == list_values[::-1]