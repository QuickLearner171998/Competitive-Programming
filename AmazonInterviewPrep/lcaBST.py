"""235. Lowest Common Ancestor of a Binary Search Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        
        r2 = root
        if not p or not q or not root:
            return 
        while root:
            path1.append(root)
            if root.val == p.val:
                break
            if root.val < p.val:
                root = root.right
            else:
                root = root.left
        # if not root:
        #     return 
        root = r2
        
        while root:
            path2.append(root)
            if root.val == q.val:
                break
            if root.val < q.val:
                root = root.right
            else:
                root = root.left        
        # if not root:
        #     return
        
        n = min(len(path1), len(path2))
        # print(path1, path2)
        for i in range(n-1, -1, -1):
            if path1[i].val==path2[i].val: return path1[i]
            



# alternate soln           
class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root        