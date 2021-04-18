"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans= [[0]*(n) for _ in range(m)]
        def doBFS(matrix, i, j):
            visited = set()
            visited.add((i,j))
            q = [((i,j), 0)]
            visited.add((i, j))
            while q:
                p = q.pop(0)
                (p1, p2) , dist= p
                if matrix[p1][p2] == 0:
                    return dist
                neighbours = [(p1-1, p2), (p1+1, p2),(p1, p2-1),(p1, p2+1)]
                for neigh in neighbours:
                    n1, n2 = neigh
                    if n1>=0 and n1<m and n2 >=0 and n2<n:
                        if (n1, n2) not in visited:
                            visited.add((n1, n2))
                            q.append(((n1, n2), dist+1))
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    ans[i][j] = doBFS(matrix,  i, j)
                    
        return ans