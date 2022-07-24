from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, node: TreeNode, res: List):
        if node:
            self.traversal(node.left, res)
            res.append(node.val)
            self.traversal(node.right, res)
