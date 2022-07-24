from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
    
        node = head
        while node:
            node_list.append(node)
            node = node.next

        return node_list[int(len(node_list)/2)]