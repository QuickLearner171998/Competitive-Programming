"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Optimized


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        self.ans = 0

        def dfs(root, val):
            if not root:
                return
            # ex. 111 --> 7 --> 2^2 + 2^1 + 1 --> 2*(2^1 +1) + root.val
            val = 2 * val + root.val
            if not root.left and not root.right:
                self.ans += val
            else:
                dfs(root.left, val)
                dfs(root.right, val)
        dfs(root, 0)
        return self.ans


# class Solution:
#     # self.ans = 0
#     def convertToDec(self, b):
#         ans = 0
#         bitVal = 1
#         for i in range(len(b) - 1, -1, -1):
#             if b[i] == "1":
#                 ans += bitVal
#             bitVal = bitVal * 2
#         return ans

#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         self.ans = 0

#         def dfs(root, stri):
#             if not root:
#                 return
#             stri += str(root.val)
#             if not root.left and not root.right:
#                 dec = self.convertToDec(stri)
#                 self.ans += dec
#             else:
#                 dfs(root.left, stri)
#                 dfs(root.right, stri)
#         dfs(root, "")
#         return self.ans
