# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left-right) > 1:
                return float('-inf')
            return 1 + max(left, right)

        val = dfs(root)
        if val == float('-inf'):
            return False
        else:
            return True

            