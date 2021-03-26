"""103. Binary Tree Zigzag Level Order Traversal

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = [root]
        ans = []
        # odd level --> l to r
        # even level --> r to l
        l = 1
        while(len(q)):
            nodesInCurrLevel = len(q)
            level = []
            while nodesInCurrLevel:
                nd = q.pop(0)
                level.append(nd.val)
                if nd.left:
                    q.append(nd.left)
                if nd.right:
                    q.append(nd.right)
                

                nodesInCurrLevel-=1
            if l%2==0:
                level = level[::-1]
            ans.append(level)

            l+=1
        return ans
        
                
        
        
        
        