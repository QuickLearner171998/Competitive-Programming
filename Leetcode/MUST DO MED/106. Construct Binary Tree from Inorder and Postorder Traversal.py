# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def build(st, end, ino, post):
            if not hasattr(build, 'index'):
                build.index = len(post)-1
            
            if st > end :
                return 
            # Create a node
            root = TreeNode(post[build.index])
            # search for post[build.index] in ino
            # i = ino.index(post[build.index])
            i = ino_map[post[build.index]]
            build.index-=1
            root.right = build(i+1, end, ino, post)
            root.left = build(st, i-1, ino, post)
            return root
        ino_map = {val:i for i, val in enumerate(inorder)}
        return build(0, len(inorder)-1, inorder, postorder)