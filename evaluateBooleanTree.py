class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        if root.val in [0, 1]:
            return root.val

        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)

             


left = TreeNode(val=1)
right = TreeNode(val=3, left=TreeNode(val=0), right=TreeNode(val=1))
root= TreeNode(val=2, left=left, right=right)

solution = Solution()
print(solution.evaluateTree(root))