"""
64. Minimum Path Sum

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        if r==0:
            return 0
        
        c = len(grid[0])
        if c==0:
            return 0
        for i in range(1, c):
            grid[0][i] += grid[0][i-1]
        for i in range(1, r):
            grid[i][0] += grid[i-1][0]

        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[r-1][c-1]