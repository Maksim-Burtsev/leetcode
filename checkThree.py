from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.dfs(root, res)
        return (sum(res) - root.val) == root.val

    def dfs(self, root: TreeNode, res: list):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
