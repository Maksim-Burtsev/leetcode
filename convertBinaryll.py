class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums_list = []

        while head:
            nums_list.append(str(head.val))
            head = head.next

        return int("".join(nums_list), 2)
