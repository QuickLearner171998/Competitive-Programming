"""Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes:

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # find all 1 coords in A and B

        onesA = [(i, j) for i in range(len(A))
                 for j in range(len(A[0])) if A[i][j] == 1]
        onesB = [(i, j) for i in range(len(B))
                 for j in range(len(B[0])) if B[i][j] == 1]

        # we place each 1 from A to the top of each 1 in B. And keep a count of all translations.
        # translation defned as --> ((ax-bx), (ay-by))

        trans = {}
        for oneA in onesA:
            for oneB in onesB:
                t = ((oneA[0] - oneB[0]), (oneA[1] - oneB[1]))
                if t in trans:
                    trans[t] += 1
                else:
                    trans[t] = 1
        if len(trans):
            return max(trans.values())
        # if no translation was possible i.e empty trans
        else:
            return 0
