# https://www.youtube.com/watch?v=jCu-Pd0IjIA&ab_channel=CodingNinjasIndia
# https://www.youtube.com/watch?v=6QSLMWgBnv4

"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

"""


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        # self.val = val


class Solution:

    def createTrie(self, root, num):

        # create a trie with all the bits of the num
        # root having the left most bit
        # if we go left that means 0 bit
        # right means 1 bit
        # to find current bit do right shift
        for i in range(31, -1, -1):
            currBit = (num >> i) & 1

            if currBit:
                if not root.right:
                    root.right = Node()
                root = root.right
            else:
                if not root.left:
                    root.left = Node()
                root = root.left

    def maxXor(self, head, nums):
        ans = -1
        for num in nums:
            currXor = 0
            root = head
            for i in range(31, -1, -1):
                # print(num, root, i)
                currBit = (num >> i) & 1

                # if currBit is 1 then for max xor pair the corresponding bit in the other no. should be 0
                # we check if a left node exists then move left
                # else we have no choice move right
                # also whenever xor value becoming one construct num
                if currBit:
                    if root.left:
                        # xor becoming 1
                        currXor += pow(2, i)
                        root = root.left
                    else:
                        root = root.right
                else:
                    if root.right:
                        # currBit = 0
                        # xor becoming 1
                        root = root.right
                        currXor += pow(2, i)
                    else:
                        root = root.left
            ans = max(ans, currXor)
        return ans

    def findMaximumXOR(self, nums: List[int]) -> int:
        if not nums:
            return 0
        root = Node()

        for num in nums:
            self.createTrie(root, num)

        return self.maxXor(root, nums)
