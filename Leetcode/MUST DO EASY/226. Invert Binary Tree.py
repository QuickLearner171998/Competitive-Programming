# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def util(root):

            if not root :
                return root
            
            util(root.left)
            util(root.right)
            
            root.left, root.right = root.right, root.left

        util(root)
        return root