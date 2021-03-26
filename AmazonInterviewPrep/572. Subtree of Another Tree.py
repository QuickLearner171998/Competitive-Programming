"""572. Subtree of Another Tree"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMatch(self, s, t):
        if not s and t or not t and s:
            return False
        if not s and not t:
            return True
        return (s.val == t.val and 
                self.isMatch(s.left, t.left) and 
                self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
#     def find(self, s,t):
#         if s is None :
#             return 0
#         if s.val == t.val and self.checkSame(s, t):
#             return 1

#         return self.find(s.left, t) or self.find(s.right, t)
        
        
#     def checkSame(self, s, t):

#         if not s and t or not t and s:
#             return False
#         if not s and not t:
#             return True
#         if s.val == t.val and self.checkSame(s.left, t.left) and self.checkSame(s.right, t.right):
#             return True
#         return False
        
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         if not t:
#             return True

        
#         return self.find(s,t)
        
