# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 or not root2:
            return root1 or root2
        result = TreeNode(root1.val + root2.val)
        result.left  = self.mergeTrees(root1.left, root2.left)
        result.right  = self.mergeTrees(root1.right, root2.right)
        return result
