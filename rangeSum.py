from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        self.low, self.high = low, high
        self.dfs(root, res)
        return sum(res)

    def dfs(self, root: TreeNode, res: list):
        if root:
            if self.low <= root.val <= self.high:
                res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
